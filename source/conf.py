# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Nathaniel Na's Blog"
copyright = '2024, Nathaniel Na'
author = 'Nathaniel Na'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'ablog',
    'sphinx_design',
]

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "deflist",
    "colon_fence",
    "linkify",
    "strikethrough",
]
suppress_warnings = ["myst.strikethrough"]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = project
html_copy_source = False
html_logo = "_static/icon.png"
html_favicon = "_static/icon.png"
html_sidebars = {
    "**": [
        "navbar-logo.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
    ]
}
html_css_files = [
    "index.css",
]
# Github
html_theme_options = {
    "repository_url": "https://github.com/nathanielisna/nathanielisna.github.io",
    "use_repository_button": True,
    "logo": {
        "text": project,
    }
    #    "footer_icons": [
    #        {
    #            "name": "GitHub",
    #            "url": "https://github.com/nathanielisna",
    #            "html": "",
    #            "class": "fa-brands fa-solid fa-github fa-2x",
    #        },
    #    ],
}
templates_path = ['_templates']

# ABlog
blog_title = project
blog_path = "posts"
blog_post_pattern = "posts/*.md"
blog_baseurl = "https://nathanielisna.github.io"

# Myst configuration
myst_heading_anchors = 3
myst_linkify_fuzzy_links = False