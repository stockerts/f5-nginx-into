# Configuration file for the Sphinx documentation builder.
import f5_sphinx_theme
# -- Project information

project = 'NGINX Plus Intro'
copyright = '2023'
author = 'F5'

#release = '0.1'
#version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html4_writer = True
html_theme = "f5_sphinx_theme"
html_theme_path = f5_sphinx_theme.get_html_theme_path()
#html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
#html_css_files = ['theme_overrides.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'