from pathlib import Path
import os

# Sphinx configuration build
# -- General configuration ------------------------------------------------
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_thebe",
    "sphinxcontrib.youtube",
    "notfound.extension",
    "sphinxext.rediraffe",
]

# Translations config
locale_dirs = ["locales"]
gettext_uuid = True
gettext_compact = False
language = os.environ.get("READTHEDOCS_LANGUAGE", "en")

# configure notfound extension to not add any prefix to the urls
notfound_urls_prefix = f"/{language}/latest/"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# MyST related params
nb_execution_mode = "auto"
nb_execution_excludepatterns = ["*.ipynb"]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "substitution",
    "html_image",
    "linkify",
]
myst_substitutions = {
  "meenal": "Meenal Jhajharia",
  "du_email": "[info@dataumbrella.org](mailto:info@dataumbrella.org)",
}

# redirections
rediraffe_redirects = {
    "webinars/contributing_to_documentation/index.md": "about/contributing_to_documentation/index.md",
    "webinars/contributing_to_pymc/index.md": "about/contributing_to_pymc/index.md",
    "webinars/intro_to_array_operations/index.md": "about/intro_to_array_operations/index.md",
    "webinars/probabilistic_programming_with_pymc/index.md": "about/probabilistic_programming_with_pymc/index.md",
    "sprint/docstring_tutorial.md": "sprint/tutorials/docstring_tutorial.md",
    "index.md": "2022-07_sprint/schedule.md",
}

# use numbered figures
numfig = True

# The base toctree document.
master_doc = "index"

# General information about the project.
project = "PyMC-Data Umbrella Sprint"
copyright = "2021-2023, Sprint contributors"
author = "Sprint Contributors"
pymc_url = "https://www.pymc.io/projects/docs/en/latest/"

version = "0.1"
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints", "README.md", "CONTRIBUTING.md", "jupyter_execute", "**.part.md", "write_tx_config.py"
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "external_links": [
    {
        "name": "PyMC", "url": pymc_url
    },
    {
        "name": "Data Umbrella", "url": "https://www.dataumbrella.org"
    },
    ],
    "header_links_before_dropdown": 6,
    "show_toc_level": 2,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pymc-devs/pymc-data-umbrella",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.pymc.io",
            "icon": "fa-brands fa-discourse",
        }
    ],
    "use_edit_page_button": True,
    "secondary_sidebar_items": ["page-toc", "searchbox", "edit-this-page", "sourcelink", "cheatsheet"],
    "navbar_start": ["navbar-logo", "version-switcher"],
    "navbar_end": ["navbar-icon-links"],
    "search_bar_text": "Search...",
    "footer_items": ["coc_notice", "copyright", "sphinx-version"],
    "google_analytics_id": "G-8YL5S5CGYD",
    "switcher": {
        "json_url": "https://pymc-data-umbrella.xyz/en/latest/_static/switcher.json",
        "version_match": language
    },
}

html_context = {
    "github_user": "pymc-devs",
    "github_repo": "pymc-data-umbrella",
    "github_version": "main",
    "doc_path": ".",
    "default_mode": "light",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]
html_css_files = ['custom.css']

# -- Options for HTMLHelp output ------------------------------------------

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/images/du-pymc-logo.png"


# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/images/favicon.ico"

# Example configuration for intersphinx
intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pymc": (pymc_url, None),
    "nb": ("https://www.pymc.io/projects/examples/en/latest/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "myst": ("https://myst-parser.readthedocs.io/en/latest", None),
    "myst-nb": ("https://myst-nb.readthedocs.io/en/latest", None),
}

thebe_config = {
    "always_load": True,
    "repository_url": "https://github.com/pymc-devs/pymc-sandbox",
    "repository_branch": "sprint",
    "selector": "div.highlight"
}

def remove_index(app):
    """
    This removes the index pages so rediraffe generates the redirect placeholder
    It needs to be present initially for the toctree as it defines the navbar.
    """

    index_file = Path(app.outdir) / "index.html"
    index_file.unlink()

    app.env.project.docnames -= {"index"}
    yield "", {}, "layout.html"


def setup(app):
    """
    Add extra steps to sphinx build
    """

    app.connect("html-collect-pages", remove_index, 100)
