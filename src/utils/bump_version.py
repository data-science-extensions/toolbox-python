# ============================================================================ #
#                                                                              #
#     Title:    Bump Version                                                   #
#     Purpose:  This script reads a pyproject.toml file and extracts the       #
#           "files" section under "tool.bump_version.replacements". It also    #
#           accepts a version number as an argument to this module. It will    #
#           then update the version in the files with the version number       #
#           provided.                                                          #
#     Args:                                                                    #
#           - version: The new version to set in the files.                    #
#                                                                              #
# ============================================================================ #


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
import argparse
import re
import tomllib
from pathlib import Path
from typing import Any

# ## Local First Party Imports ----
from toolbox_python.dictionaries import DotDict


## --------------------------------------------------------------------------- #
##  Args                                                                    ####
## --------------------------------------------------------------------------- #


### Set up argument parsing ----
parser = argparse.ArgumentParser(description="Bump version in files.")
parser.add_argument(
    "-v", "--verbose", default=False, type=bool, help="Enable verbose output."
)
parser.add_argument("version", type=str, help="The new version to set in the files.")

### Parse the arguments ----
args: argparse.Namespace = parser.parse_args()

### Check ----
if args.verbose:
    print("Arguments:")
    for arg in vars(args):
        print(f"{arg}: {getattr(args, arg)}")


## --------------------------------------------------------------------------- #
##  Config                                                                  ####
## --------------------------------------------------------------------------- #


def get_config() -> list[DotDict]:

    ### Read the pyproject.toml file ----
    with open("pyproject.toml", "rb") as f:
        data: dict[str, Any] = tomllib.load(f)

    ### Convert the dictionary to a DotDict for easier access ----
    data = DotDict(data)

    ### Extract the relevant sections ----
    files: list[DotDict] = data.tool.bump_version.replacements.files

    ### Return ----
    return files


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Main Section                                                          ####
#                                                                              #
# ---------------------------------------------------------------------------- #


def update_files(files: list[DotDict]) -> None:

    ### Check the files ----
    if args.verbose:
        print("Updating files:")

    ### Loop through the files ----
    for file in files:

        ### Extract variables ----
        filepath = Path(file.file)
        pattern: str = file.pattern
        search_pattern: str = "^" + pattern.replace("{VERSION}", ".*?")

        ### Check ----
        if args.verbose:
            print(f"- {file.file}")

        ### Check if the file exists ----
        if not filepath.exists():
            print(f"-- File does not exist: {file.file}")
            continue

        ### Read the file ----
        content: str = filepath.read_text()

        ### Check if the pattern exists in the file ----
        if not re.search(pattern=search_pattern, string=content, flags=re.MULTILINE):
            print(f"-- !! Pattern not found in file: {file.pattern}")
            continue

        new_content: list[str] = []
        for line in content.splitlines():
            if re.search(pattern=search_pattern, string=line, flags=re.MULTILINE):
                new_line: str = re.sub(
                    pattern=search_pattern,
                    repl=pattern.replace("{VERSION}", args.version),
                    string=line,
                )
                new_content.append(new_line)
                if args.verbose:
                    print(f"-- old--> {line}")
                    print(f"-- new--> {new_line}")
            else:
                new_content.append(line)

        ### Write the new content to the file ----
        filepath.write_text("\n".join(new_content) + "\n")


def main() -> None:
    update_files(get_config())
