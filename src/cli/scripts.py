## --------------------------------------------------------------------------- #
##  Setup                                                                   ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
import ast
import re
import subprocess
import sys
from pathlib import Path
from typing import Literal, NamedTuple, Union


## --------------------------------------------------------------------------- #
##  Generic                                                                 ####
## --------------------------------------------------------------------------- #


def run_command(*command) -> None:
    print("\n", " ".join(command), sep="", flush=True)
    subprocess.run(command, check=True)


def uv_sync() -> None:
    run_command("uv", "sync", "--all-groups", "--native-tls", "--link-mode=copy")


def lint_check() -> None:
    lint()
    check()


def get_all_files(*suffixes) -> list[str]:
    return [
        str(p)
        for p in Path("./").glob("**/*")
        if ".venv" not in p.parts
        and not p.parts[0].startswith(".")
        and p.is_file()
        and p.suffix in {*suffixes}
    ]


## --------------------------------------------------------------------------- #
##  Linting                                                                 ####
## --------------------------------------------------------------------------- #


def run_black() -> None:
    run_command("black", "--config=pyproject.toml", "./")


def run_blacken_docs() -> None:
    run_command("blacken-docs", *get_all_files(".md", ".py", ".ipynb"))


def run_isort() -> None:
    run_command("isort", "--settings-file=pyproject.toml", "./")


def run_pycln() -> None:
    run_command("pycln", "--config=pyproject.toml", "src/")


def run_pyupgrade() -> None:
    run_command("pyupgrade", "--py3-plus", *get_all_files(".py"))


def lint() -> None:
    run_black()
    run_blacken_docs()
    run_isort()
    run_pycln()


## --------------------------------------------------------------------------- #
##  Checking                                                                ####
## --------------------------------------------------------------------------- #


def check_black() -> None:
    run_command("black", "--check", "--config=pyproject.toml", "./")


def check_blacken_docs() -> None:
    run_command("blacken-docs", "--check", *get_all_files(".md", ".py", ".ipynb"))


def check_mypy() -> None:
    run_command(
        "mypy",
        "--install-types",
        "--non-interactive",
        "--config-file=pyproject.toml",
        "./src/toolbox_python",
    )


def check_isort() -> None:
    run_command("isort", "--check", "--settings-file=pyproject.toml", "./")


def check_codespell() -> None:
    run_command("codespell", "--toml=pyproject.toml", "src/", "*.py")


def check_pylint() -> None:
    run_command("pylint", "--rcfile=pyproject.toml", "src/toolbox_python")


def check_pycln() -> None:
    run_command("pycln", "--config=pyproject.toml", "src/")


def check_build() -> None:
    run_command("uv", "build", "--out-dir=dist")
    run_command("rm", "--recursive", "dist")


def check_mkdocs() -> None:
    run_command("mkdocs", "build", "--site-dir=temp")
    run_command("rm", "--recursive", "temp")


def check_pytest() -> None:
    run_command("pytest", "--config-file=pyproject.toml")


def check() -> None:
    check_black()
    check_blacken_docs()
    check_mypy()
    check_isort()
    check_codespell()
    check_pylint()
    check_pycln()
    check_mkdocs()
    check_build()
    check_pytest()


## --------------------------------------------------------------------------- #
##  Pre-Commit                                                              ####
## --------------------------------------------------------------------------- #


class FunctionAndClassDetails(NamedTuple):
    item_type: Literal["function", "class"]
    name: str
    node: Union[ast.FunctionDef, ast.ClassDef]
    lineno: int


def check_docstrings(file: str) -> None:
    """
    Check docstrings in a Python file for completeness and correct formatting.

    This function performs extensive validation of docstrings according to the
    project's documentation standards.
    """
    file_path = Path(file)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file}")

    if not file_path.suffix == ".py":
        raise ValueError(f"File must be a Python file (.py): {file}")

    # Read and parse the file
    with open(file_path, mode="r", encoding="utf-8") as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        raise SyntaxError(f"Invalid Python syntax in {file}: {e}")

    # Extract all functions and classes with docstrings
    functions_and_classes: list[FunctionAndClassDetails] = []

    class DocstringVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            if node.name.startswith("_"):  # Skip private functions
                return
            functions_and_classes.append(
                FunctionAndClassDetails("function", node.name, node, node.lineno)
            )
            self.generic_visit(node)

        def visit_ClassDef(self, node):
            if node.name.startswith("_"):  # Skip private classes
                return
            functions_and_classes.append(
                FunctionAndClassDetails("class", node.name, node, node.lineno)
            )
            self.generic_visit(node)

    visitor = DocstringVisitor()
    visitor.visit(tree)

    errors = []

    for item_type, name, node, lineno in functions_and_classes:
        try:
            _check_single_docstring(item_type, name, node, lineno, file)
        except Exception as e:
            errors.append(f"Line {lineno}, {item_type} '{name}': {str(e)}")

    if errors:
        error_msg = f"Docstring validation errors in {file}:\n" + "\n".join(errors)
        raise RuntimeError(error_msg)

    print(f"✓ All docstrings in {file} are valid")


def _check_single_docstring(
    item_type: Literal["function", "class"],
    name: str,
    node: Union[ast.FunctionDef, ast.ClassDef],
    lineno: int,
    file: str,
) -> None:
    """Check a single function or class docstring."""
    docstring = ast.get_docstring(node)

    if not docstring:
        # raise ValueError(f"Missing docstring")
        return  # Skip if no docstring is present

    # Required sections in order
    required_sections = ["summary", "params", "returns_or_yields", "examples"]
    optional_sections = [
        "details",
        "raises",
        "credit",
        "equation",
        "notes",
        "references",
        "see_also",
    ]

    # Check for mandatory sections
    if not re.search(r'!!! summary "Summary"', docstring, re.IGNORECASE):
        raise ValueError('Missing mandatory Summary section: `!!! summary "Summary"`')

    # Check Params section
    if item_type == "function" and isinstance(node, ast.FunctionDef):
        # Get function parameters (excluding 'self' for methods)
        params = [arg.arg for arg in node.args.args if arg.arg != "self"]
        if params and not re.search(r"Params:", docstring):
            raise ValueError(
                "Missing mandatory Params section for function with parameters"
            )

        # Check each parameter is documented
        if params:
            for param in params:
                param_pattern = rf"{param}\s*\([^)]+\):"
                if not re.search(param_pattern, docstring):
                    raise ValueError(
                        f"Parameter '{param}' not documented or incorrectly formatted"
                    )

    # Check Returns or Yields (but not both)
    has_returns = re.search(r"Returns:", docstring)
    has_yields = re.search(r"Yields:", docstring)

    if has_returns and has_yields:
        raise ValueError("Docstring cannot have both Returns and Yields sections")

    if not has_returns and not has_yields:
        if item_type == "function":
            raise ValueError("Missing mandatory Returns or Yields section")

    # Check mandatory Examples section
    if not re.search(r'\?\?\?\+ example "Examples"', docstring, re.IGNORECASE):
        raise ValueError(
            'Missing mandatory Examples section: `???+ example "Examples"`'
        )

    # Validate section order
    _check_section_order(docstring)

    # Validate specific section formats
    _validate_section_formats(docstring, name)


def _check_section_order(docstring: str) -> None:
    """Check that sections appear in the correct order."""
    section_patterns = [
        (r'!!! summary "Summary"', "Summary"),
        (r'!!! details "Details"', "Details"),
        (r"Params:", "Params"),
        (r"Raises:", "Raises"),
        (r"Returns:", "Returns"),
        (r"Yields:", "Yields"),
        (r'\?\?\?+ example "Examples"', "Examples"),
        (r'\?\?\?\+ success "Credit"', "Credit"),
        (r'\?\?\?\+ calculation "Equation"', "Equation"),
        (r'\?\?\?\+ info "Notes"', "Notes"),
        (r'\?\?\? question "References"', "References"),
        (r'\?\?\? tip "See Also"', "See Also"),
    ]

    found_sections = []
    for pattern, section_name in section_patterns:
        match = re.search(pattern, docstring, re.IGNORECASE)
        if match:
            found_sections.append((match.start(), section_name))

    # Sort by position in docstring
    found_sections.sort(key=lambda x: x[0])

    # Check order matches expected order
    expected_order = [
        "Summary",
        "Details",
        "Params",
        "Raises",
        "Returns",
        "Yields",
        "Examples",
        "Credit",
        "Equation",
        "Notes",
        "References",
        "See Also",
    ]

    last_expected_index = -1
    for _, section_name in found_sections:
        try:
            current_index = expected_order.index(section_name)
            if current_index < last_expected_index:
                raise ValueError(f"Section '{section_name}' appears out of order")
            last_expected_index = current_index
        except ValueError:
            # Section not in expected order list - this shouldn't happen
            pass


def _validate_section_formats(docstring: str, name: str) -> None:
    """Validate the format of specific sections."""

    # Check Summary is single paragraph
    summary_match = re.search(
        r'!!! summary "Summary"\s*\n\s*(.+?)(?=\n\s*\n|\n\s*[!?])',
        docstring,
        re.DOTALL | re.IGNORECASE,
    )
    if summary_match:
        summary_text = summary_match.group(1).strip()
        # Check if summary has multiple paragraphs (contains double newlines)
        if "\n\n" in summary_text or re.search(r"\n\s*\n", summary_text):
            raise ValueError("Summary section should be a single paragraph")

    # Validate Params format
    if re.search(r"Params:", docstring):
        # Find Params section
        params_match = re.search(
            r"Params:\s*\n(.*?)(?=\n\s*(?:Raises|Returns|Yields|Examples|!!!|\?\?\?))",
            docstring,
            re.DOTALL,
        )
        if params_match:
            params_content = params_match.group(1)
            # Check each parameter follows the format: param_name (type):
            param_lines = [line for line in params_content.split("\n") if line.strip()]
            for line in param_lines:
                if not line.startswith(" "):  # Parameter name line
                    if not re.match(r"\w+\s*\([^)]+\):", line):
                        raise ValueError(
                            f"Invalid parameter format: '{line}'. Expected: 'param_name (type):'"
                        )

    # Validate Raises format
    if re.search(r"Raises:", docstring):
        raises_match = re.search(
            r"Raises:\s*\n(.*?)(?=\n\s*(?:Returns|Yields|Examples|!!!|\?\?\?))",
            docstring,
            re.DOTALL,
        )
        if raises_match:
            raises_content = raises_match.group(1)
            # Check each exception follows the format: ExceptionType:
            exception_lines = [
                line for line in raises_content.split("\n") if line.strip()
            ]
            for line in exception_lines:
                if not line.startswith(" "):  # Exception name line
                    if not re.match(
                        r"\w+Error:|TypeError:|ValueError:|RuntimeError:|Exception:",
                        line,
                    ):
                        # Allow common exception patterns
                        if not line.endswith(":"):
                            raise ValueError(
                                f"Invalid exception format: '{line}'. Expected: 'ExceptionType:'"
                            )

    # Validate Returns/Yields format
    returns_or_yields = re.search(r"(Returns|Yields):", docstring)
    if returns_or_yields:
        section_name = returns_or_yields.group(1)
        section_match = re.search(
            rf"{section_name}:\s*\n(.*?)(?=\n\s*(?:Examples|!!!|\?\?\?))",
            docstring,
            re.DOTALL,
        )
        if section_match:
            section_content = section_match.group(1)
            # Check format: optional_name (type):
            return_lines = [
                line for line in section_content.split("\n") if line.strip()
            ]
            for line in return_lines:
                if not line.startswith(" "):  # Return value line
                    if not re.match(r"(\w+\s*)?\([^)]+\):", line):
                        raise ValueError(
                            f"Invalid {section_name} format: '{line}'. Expected: 'name (type):' or '(type):'"
                        )


def check_docstrings_cli() -> None:
    """Command line interface for docstring checking."""
    if len(sys.argv) < 2:
        print("Usage: python scripts.py <python_file>")
        sys.exit(1)

    try:
        check_docstrings(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
