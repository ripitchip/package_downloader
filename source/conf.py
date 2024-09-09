# Created Date: Thursday, January 11th 2024, 11:59:24 pm
# Created By: BriocheAF
# Copyright (c) 2024 BriocheAF
# -----
# Last Modified: Friday, January 12th 2024, 1:43:24 pm
# Modified By: BriocheAF
import os

PROJECT = "default project"
copyright = "default author"  # noqa: A001
AUTHOR = copyright
RELEASE = "0.0.1"
autosectionlabel_prefix_document = True
html_title = PROJECT
html_logo = "_static/images/logo_full.svg"
html_favicon = "_static/images/logo.svg"
locale_dirs = ["locale/"]
gettext_compact = False

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.youtube",
    "sphinx_design",
]


def setup(app) -> None:  # noqa: ANN001
    """
    Set up the application.

    Args:
    ----
            app: The application object.

    """
    app.add_css_file("css/custom.css")


html_theme_options = {
    "logo": {
        "text": os.getenv("TITLE"),
        "alt_text": "Home Page",
    },
    "pygment_light_style": "emacs",
    "pygment_dark_style": "dracula",
    "repository_url": os.getenv("REPO_URL"),
    "use_repository_button": bool(os.getenv("REPO_URL")),
    "repository_provider": os.getenv("REPO_PROVIDER"),
    "use_download_button": True,
    # "navbar_end": ["mybutton.html"]
}


# Set the autodoc options
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "reference-labels": True,
}
autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns = []
autodoc_mock_imports = ["../../noxfile.py"]


myst_enable_extensions = {
    "colon_fence": True,
    "substitution": True,
    "deflist": True,
    "dollarmath": True,
    "amsmath": True,
    "smartquotes": True,
    "replacements": True,
    "html_image": True,
    "html_admonition": True,
    "attrs_inline": True,
}

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
source_parsers = {".md": "recommonmark.parser.CommonMarkParser"}
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
