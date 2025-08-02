# ============================================================================ #
#                                                                              #
#     Title: Shortcodes and Hooks for MkDocs Material Documentation            #
#     Purpose: Provide custom shortcodes and hooks for enhancing the docs.     #
#     Notes: Created with reference to MkDocs Material hooks and shortcodes.   #
#            https://github.com/squidfunk/mkdocs-material/blob/master/src/overrides/hooks/shortcodes.py
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


# ## Future Python Library Imports ----
from __future__ import annotations

# ## Python StdLib Imports ----
import posixpath
import re
from re import Match

# ## Python Third Party Imports ----
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page

# ## Local First Party Imports ----
from toolbox_python.collection_types import str_list


## --------------------------------------------------------------------------- #
##  Exports                                                                 ####
## --------------------------------------------------------------------------- #


__all__: str_list = ["on_page_markdown", "flag", "option", "setting"]


## --------------------------------------------------------------------------- #
##  Main Hook                                                               ####
## --------------------------------------------------------------------------- #


# @todo
def on_page_markdown(markdown: str, *, page: Page, config: MkDocsConfig, files: Files):

    # There are some pages which are short-referenced, meaning that they
    # are referenced in the main page, but their content is not included in the
    # main page. This is done using the Snippets Notation: https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
    # In this case, we will read the content of the source file and return it.
    short_referenced_pages: list[str] = ["overview", "changelog", "contributing"]
    if page.file.name in short_referenced_pages:
        pattern = r'-*8<-*\s*"([^"]+)"'
        match = re.search(pattern, markdown)
        if match:
            filename = match.group(1)
            with open(filename, encoding="utf-8") as f:
                markdown = f.read()

    # Replace callback
    def replace(match: Match):
        type, args = match.groups()
        args = args.strip()
        if type == "folder":
            return _badge_for_folder(args, page, files)
        elif type == "file":
            return _badge_for_file(args, page, files)
        elif type == "tag":
            return _badge_for_tag(args, page, files)
        elif type == "date":
            return _badge_for_date(args, page, files)
        elif type == "link":
            return _badge_for_link(args, page, files)
        elif type == "version":
            if args.startswith("insiders-"):
                return _badge_for_version_insiders(args, page, files)
            else:
                return _badge_for_version(args, page, files)
        elif type == "sponsors":
            return _badge_for_sponsors(page, files)
        elif type == "flag":
            return flag(args, page, files)
        elif type == "option":
            return option(args)
        elif type == "setting":
            return setting(args)
        elif type == "feature":
            return _badge_for_feature(args, page, files)
        elif type == "plugin":
            return _badge_for_plugin(args, page, files)
        elif type == "extension":
            return _badge_for_extension(args, page, files)
        elif type == "utility":
            return _badge_for_utility(args, page, files)
        elif type == "example":
            return _badge_for_example(args, page, files)
        elif type == "demo":
            return _badge_for_demo(args, page, files)
        elif type == "default":
            if args == "none":
                return _badge_for_default_none(page, files)
            elif args == "computed":
                return _badge_for_default_computed(page, files)
            else:
                return _badge_for_default(args, page, files)

        # Otherwise, raise an error
        raise RuntimeError(f"Unknown shortcode: {type}")

    # Find and replace all external asset URLs in current page
    return re.sub(r"<!-- md:(\w+)(.*?) -->", replace, markdown, flags=re.I | re.M)


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Helper Functions                                                      ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Config functions                                                        ####
## --------------------------------------------------------------------------- #


# Create a flag of a specific type
def flag(args: str, page: Page, files: Files):
    type, *_ = args.split(" ", 1)
    if type == "experimental":
        return _badge_for_experimental(page, files)
    elif type == "required":
        return _badge_for_required(page, files)
    elif type == "customization":
        return _badge_for_customization(page, files)
    elif type == "metadata":
        return _badge_for_metadata(page, files)
    elif type == "multiple":
        return _badge_for_multiple(page, files)
    raise RuntimeError(f"Unknown type: {type}")


# Create a linkable option
def option(type: str):
    _, *_, name = re.split(r"[.:]", type)
    return f"[`{name}`](#+{type}){{ #+{type} }}\n\n"


# Create a linkable setting - @todo append them to the bottom of the page
def setting(type: str):
    _, *_, name = re.split(r"[.*]", type)
    return f"`{name}` {{ #{type} }}\n\n[{type}]: #{type}\n\n"


## --------------------------------------------------------------------------- #
##  Resolver functions                                                      ####
## --------------------------------------------------------------------------- #


# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve_path(path: str, page: Page, files: Files):
    path, anchor, *_ = f"{path}#".split("#")
    path = _resolve(files.get_file_from_path(path), page)
    return "#".join([path, anchor]) if anchor else path


# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve(file: File, page: Page):
    path = posixpath.relpath(file.src_uri, page.file.src_uri)
    return posixpath.sep.join(path.split(posixpath.sep)[1:])


# Create badge
def _badge(icon: str, text: str = "", type: str = ""):
    classes = f"mdx-badge mdx-badge--{type}" if type else "mdx-badge"
    return "".join(
        [
            f'<span class="{classes}">',
            *([f'<span class="mdx-badge__icon">{icon}</span>'] if icon else []),
            *([f'<span class="mdx-badge__text">{text}</span>'] if text else []),
            f"</span>",
        ]
    )


## --------------------------------------------------------------------------- #
##  Customs                                                                 ####
## --------------------------------------------------------------------------- #


# Create badge for folder
def _badge_for_folder(text: str, page: Page, files: Files) -> str:
    icon = "material-folder-multiple"
    return _badge(icon=f"[:{icon}:]({text})", text=f"[`{text}`][{text}]")


# Create badge for file
def _badge_for_file(text: str, page: Page, files: Files) -> str:
    icon = "material-file-multiple"
    return _badge(icon=f"[:{icon}:]({text})", text=f"[`{text}`]({text})")


def _badge_for_tag(text: str, page: Page, files: Files) -> str:
    # icon = "material-tag-multiple"
    icon = "label"
    return _badge(icon=f":{icon}:", text=f"`{text}`")


def _badge_for_date(text: str, page: Page, files: Files) -> str:
    # icon = "material-calendar-month"
    icon = "calendar"
    return _badge(icon=f":{icon}:", text=f"`{text}`")


def _badge_for_link(text: str, page: Page, files: Files) -> str:
    # icon = "material-link-variant"
    icon = "link"
    return _badge(icon=f":{icon}:", text=f"{text}")


## --------------------------------------------------------------------------- #
##  Creator functions                                                       ####
## --------------------------------------------------------------------------- #


# Create sponsors badge
def _badge_for_sponsors(page: Page, files: Files):
    icon = "material-heart"
    href = _resolve_path("insiders/index.md", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Sponsors only')", type="heart")


# Create badge for version
def _badge_for_version(text: str, page: Page, files: Files):
    spec = text
    path = f"changelog/index.md#{spec}"

    # Return badge
    icon = "material-tag-outline"
    href = _resolve_path("conventions.md#version", page, files)
    return _badge(
        icon=f"[:{icon}:]({href} 'Minimum version')",
        text=f"[{text}]({_resolve_path(path, page, files)})" if spec else "",
    )


# Create badge for version of Insiders
def _badge_for_version_insiders(text: str, page: Page, files: Files):
    spec = text.replace("insiders-", "")
    path = f"insiders/changelog/index.md#{spec}"

    # Return badge
    icon = "material-tag-heart-outline"
    href = _resolve_path("conventions.md#version-insiders", page, files)
    return _badge(
        icon=f"[:{icon}:]({href} 'Minimum version')",
        text=f"[{text}]({_resolve_path(path, page, files)})" if spec else "",
    )


# Create badge for feature
def _badge_for_feature(text: str, page: Page, files: Files):
    icon = "material-toggle-switch"
    href = _resolve_path("conventions.md#feature", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Optional feature')", text=text)


# Create badge for plugin
def _badge_for_plugin(text: str, page: Page, files: Files):
    icon = "material-floppy"
    href = _resolve_path("conventions.md#plugin", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Plugin')", text=text)


# Create badge for extension
def _badge_for_extension(text: str, page: Page, files: Files):
    icon = "material-language-markdown"
    href = _resolve_path("conventions.md#extension", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Markdown extension')", text=text)


# Create badge for utility
def _badge_for_utility(text: str, page: Page, files: Files):
    icon = "material-package-variant"
    href = _resolve_path("conventions.md#utility", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Third-party utility')", text=text)


# Create badge for example
def _badge_for_example(text: str, page: Page, files: Files):
    return "\n".join(
        [
            _badge_for_example_download(text, page, files),
            _badge_for_example_view(text, page, files),
        ]
    )


# Create badge for example view
def _badge_for_example_view(text: str, page: Page, files: Files):
    icon = "material-folder-eye"
    href = f"https://mkdocs-material.github.io/examples/{text}/"
    return _badge(icon=f"[:{icon}:]({href} 'View example')", type="right")


# Create badge for example download
def _badge_for_example_download(text: str, page: Page, files: Files):
    icon = "material-folder-download"
    href = f"https://mkdocs-material.github.io/examples/{text}.zip"
    return _badge(
        icon=f"[:{icon}:]({href} 'Download example files')",
        text=f"[`.zip`]({href})",
        type="right",
    )


# Create badge for demo repository
def _badge_for_demo(text: str, page: Page, files: Files):
    icon = "material-github"
    href = f"https://github.com/mkdocs-material/{text}"
    return _badge(icon=f"[:{icon}:]({href} 'Demo repository')", text=text, type="right")


# Create badge for default value
def _badge_for_default(text: str, page: Page, files: Files):
    icon = "material-water"
    href = _resolve_path("conventions.md#default", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Default value')", text=text)


# Create badge for empty default value
def _badge_for_default_none(page: Page, files: Files):
    icon = "material-water-outline"
    href = _resolve_path("conventions.md#default", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Default value is empty')")


# Create badge for computed default value
def _badge_for_default_computed(page: Page, files: Files):
    icon = "material-water-check"
    href = _resolve_path("conventions.md#default", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Default value is computed')")


# Create badge for metadata property flag
def _badge_for_metadata(page: Page, files: Files):
    icon = "material-list-box-outline"
    href = _resolve_path("conventions.md#metadata", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Metadata property')")


# Create badge for required value flag
def _badge_for_required(page: Page, files: Files):
    icon = "material-alert"
    href = _resolve_path("conventions.md#required", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Required value')")


# Create badge for customization flag
def _badge_for_customization(page: Page, files: Files):
    icon = "material-brush-variant"
    href = _resolve_path("conventions.md#customization", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Customization')")


# Create badge for multiple instance flag
def _badge_for_multiple(page: Page, files: Files):
    icon = "material-inbox-multiple"
    href = _resolve_path("conventions.md#multiple-instances", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Multiple instances')")


# Create badge for experimental flag
def _badge_for_experimental(page: Page, files: Files):
    icon = "material-flask-outline"
    href = _resolve_path("conventions.md#experimental", page, files)
    return _badge(icon=f"[:{icon}:]({href} 'Experimental')")
