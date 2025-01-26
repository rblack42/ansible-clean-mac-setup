# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ansible: Clean Mac Setup'
copyright = '2025, Roie R. Black'
author = 'Roie R. Black'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'sphinxcontrib.tikz',
    'sphinx_ext.wordcount',
]
tikz_proc_suite = 'ImageMagick'
tikz_latex_preamble = '\\usepackage{gitdags}'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = { }

html_static_path = ['_static']
html_use_smartypants = True
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
html_last_updated_fmt = '%b %d, %Y'

