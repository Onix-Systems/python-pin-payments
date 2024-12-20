import os
import sys
print(sys.path)
sys.path.insert(0, os.path.abspath('../..'))
# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]
project = 'Python-Pin-Payments Library'
copyright = '2024, Onix-Systems'
author = 'Onix-Systems'
release = '1.0'

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    "collapse_navigation": False,  # Keeps the menu expanded
    "navigation_depth": 4,  # Adjust the depth of navigation in the sidebar
    "titles_only": False  # Ensures subheadings are part of the ToC
}

# Napoleon settings for Google style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

numpydoc_show_class_members = False
