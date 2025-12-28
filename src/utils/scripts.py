## --------------------------------------------------------------------------- #
##  Setup                                                                   ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
import subprocess
import sys
from pathlib import Path
from textwrap import dedent
from typing import Union


## --------------------------------------------------------------------------- #
##  Constants                                                               ####
## --------------------------------------------------------------------------- #


PACKAGE_NAME: str = "toolbox-python"
'''PACKAGE_NAME="toolbox-python"'''
DIRECTORY_NAME: str = PACKAGE_NAME.replace("-", "_")
'''DIRECTORY_NAME="toolbox_python"'''


## --------------------------------------------------------------------------- #
##  Generic                                                                 ####
## --------------------------------------------------------------------------- #


def expand_space(lst: Union[list[str], tuple[str, ...]]) -> list[str]:
    return [item for element in lst for item in element.split()]


def run_command(*command, expand: bool = True) -> None:
    _command: list[str] = expand_space(command) if expand else list(command)
    print("\n", " ".join(_command), sep="", flush=True)
    subprocess.run(_command, check=True, encoding="utf-8")


run = run_command


def uv_sync() -> None:
    run("uv sync --all-groups --native-tls --link-mode=copy")


def lint_check() -> None:
    lint()
    check()


def get_all_files(*suffixes) -> list[str]:
    return [
        str(p)
        for p in Path("./").glob("**/*")
        if ".venv" not in p.parts and not p.parts[0].startswith(".") and p.is_file() and p.suffix in {*suffixes}
    ]


## --------------------------------------------------------------------------- #
##  Linting                                                                 ####
## --------------------------------------------------------------------------- #


def run_black() -> None:
    run("black --config=pyproject.toml ./")


def run_blacken_docs() -> None:
    run("blacken-docs", *get_all_files(".md", ".py", ".ipynb"))


def run_isort() -> None:
    run("isort --settings-file=pyproject.toml ./")


def run_pycln() -> None:
    run("pycln --config=pyproject.toml src/")


def run_pyupgrade() -> None:
    run("pyupgrade --py3-plus", *get_all_files(".py"))


def lint() -> None:
    run_black()
    run_blacken_docs()
    run_isort()
    run_pycln()


## --------------------------------------------------------------------------- #
##  Checking                                                                ####
## --------------------------------------------------------------------------- #


def check_black() -> None:
    run("black --check --config=pyproject.toml ./")


def check_blacken_docs() -> None:
    run("blacken-docs --check", *get_all_files(".md", ".py", ".ipynb"))


def check_ty() -> None:
    run(
        "ty",
        "check",
        # "--config-file=pyproject.toml",
        f"./src/{DIRECTORY_NAME}",
    )


def check_isort() -> None:
    run("isort --check --settings-file=pyproject.toml ./")


def check_codespell() -> None:
    run("codespell --toml=pyproject.toml src/ *.py")


def check_pylint() -> None:
    run(f"pylint --rcfile=pyproject.toml src/{DIRECTORY_NAME}")


def check_pycln() -> None:
    run(f"pycln --check --config=pyproject.toml src/{DIRECTORY_NAME}")


def check_build() -> None:
    run("uv build --out-dir=dist")
    run("rm --recursive dist")


def check_mkdocs() -> None:
    run("mkdocs build --site-dir=temp")
    run("rm --recursive temp")


def check_pytest() -> None:
    run("pytest --config-file=pyproject.toml")


def check_docstrings() -> None:
    run(f"dfc --output=table ./src/{DIRECTORY_NAME}")


def check_complexity() -> None:
    notes: str = dedent(
        """
        Notes from: https://rohaquinlop.github.io/complexipy/#running-the-analysis
        - Complexity <= 5: Simple, easy to understand
        - Complexity 6-15: Moderate, acceptable for most cases
        - Complexity >= 15: Complex, consider refactoring into simpler functions
        """
    )
    print(notes)
    run(f"complexipy ./src/{DIRECTORY_NAME}")


def check() -> None:
    check_black()
    check_blacken_docs()
    check_ty()
    check_isort()
    check_codespell()
    check_pycln()
    check_pylint()
    check_complexity()
    check_docstrings()
    check_pytest()
    check_mkdocs()
    check_build()


## --------------------------------------------------------------------------- #
##  Git                                                                     ####
## --------------------------------------------------------------------------- #


def add_git_credentials() -> None:
    run("git config --global user.name github-actions[bot]")
    run("git config --global user.email github-actions[bot]@users.noreply.github.com")


def git_refresh_current_branch() -> None:
    run("git remote update")
    run("git fetch --verbose")
    run("git fetch --verbose --tags")
    run("git pull --verbose")
    run("git status --verbose")
    run("git branch --list --verbose")
    run("git tag --list --sort=-creatordate")


def git_checkout_branch(branch_name: str) -> None:
    run(f"git checkout -B {branch_name} --track origin/{branch_name}")


def git_switch_to_branch() -> None:
    if len(sys.argv) < 3:
        print("Requires argument: <branch_name>")
        sys.exit(1)
    git_checkout_branch(sys.argv[2])


def git_switch_to_main_branch() -> None:
    git_checkout_branch("main")


def git_switch_to_docs_branch() -> None:
    git_checkout_branch("docs-site")


def git_add_coverage_report() -> None:
    run("mkdir -p ./docs/code/coverage/")
    run("cp -r ./cov-report/html/. ./docs/code/coverage/")
    run("git add ./docs/code/coverage/")
    run("git", "commit", "--no-verify", '--message="Update coverage report [skip ci]"', expand=False)
    run("git push")


def git_update_version(version: str) -> None:
    run(f'echo VERSION="{version}"')
    run("git add .")
    run("git", "commit", "--allow-empty", f'--message="Bump to version `{version}` [skip ci]"', expand=False)
    run("git push --force --no-verify")
    run("git status")


def git_update_version_cli() -> None:
    if len(sys.argv) < 3:
        print("Requires argument: <version>")
        sys.exit(1)
    git_update_version(sys.argv[2])


def git_fix_tag_reference(version: str) -> None:
    run(f"git tag --force {version}")
    run(f"git push --force origin {version}")


def git_fix_tag_reference_cli() -> None:
    if len(sys.argv) < 3:
        print("Requires argument: <version>")
        sys.exit(1)
    git_fix_tag_reference(sys.argv[2])


## --------------------------------------------------------------------------- #
##  Docs                                                                    ####
## --------------------------------------------------------------------------- #


def docs_serve_static() -> None:
    run("mkdocs serve")


def docs_serve_versioned() -> None:
    run("mike serve --branch=docs-site")


def docs_build_static() -> None:
    run("mkdocs build --clean")


def docs_build_versioned(version: str) -> None:
    run("git config --global --list")
    run("git config --local --list")
    run("git remote --verbose")
    run(f"mike --debug deploy --update-aliases --branch=docs-site --push {version} latest")


def docs_build_versioned_cli() -> None:
    if len(sys.argv) < 3:
        print("Requires argument: <version>")
        sys.exit(1)
    docs_build_versioned(sys.argv[2])


def update_git_docs(version: str) -> None:
    run("git add .")
    run(
        "git",
        "commit",
        f'--message="Build docs `{version}` [skip ci]"',
        expand=False,
    )
    run("git push --force --no-verify --push-option ci.skip")


def update_git_docs_cli() -> None:
    if len(sys.argv) < 3:
        print("Requires argument: <version>")
        sys.exit(1)
    update_git_docs(sys.argv[2])


def docs_check_versions() -> None:
    run("mike --debug list --branch=docs-site")


def docs_delete_version(version: str) -> None:
    run(f"mike --debug delete --branch=docs-site {version}")


def docs_delete_version_cli() -> None:
    if len(sys.argv) < 2:
        print("Requires argument: <version>")
        sys.exit(1)
    docs_delete_version(sys.argv[1])


def docs_set_default() -> None:
    run("mike --debug set-default --branch=docs-site --push latest")


def build_static_docs(version: str) -> None:
    docs_build_static()
    update_git_docs(version)


def build_static_docs_cli() -> None:
    if len(sys.argv) < 3:
        print("Requires argument: <version>")
        sys.exit(1)
    build_static_docs(sys.argv[2])


def build_versioned_docs(version: str) -> None:
    docs_build_versioned(version)
    docs_set_default()


def build_versioned_docs_cli() -> None:
    if len(sys.argv) < 3:
        print("Requires argument: <version>")
        sys.exit(1)
    build_versioned_docs(sys.argv[2])


## --------------------------------------------------------------------------- #
##  Execute                                                                 ####
## --------------------------------------------------------------------------- #


if __name__ == "__main__":

    function_name: str = sys.argv[1].lower().replace("-", "_")
    if function_name not in globals():
        print(f"Function not found: '{function_name}'.")
        sys.exit(1)

    globals()[function_name]()
