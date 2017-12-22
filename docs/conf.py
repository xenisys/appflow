# -*- coding: utf-8 -*-
#
# documentation build configuration file, created by
# sphinx-quickstart on Sat Sep 10 18:18:25 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import sys, os
sys.path.append(os.path.join(os.path.dirname(__name__), '..'))
print(os.path.join(os.path.dirname(__name__), '..'), "*******************8")
# sys.path.insert(0, os.path.abspath('../'))
# sys.path.insert(0, os.path.abspath('.'))

# from AppFlow import __version__ as sw_version

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'AppFlow - Deduplicating Archiver'
# copyright = '2010-2014 Jonas AppFlowström, 2015-2017 The AppFlow Collective (see AUTHORS file)'
copyright = u'2017, Ivo Marino, Luca Di Maio'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# split_char = '+' if '+' in sw_version else '-'
# version = sw_version.split(split_char)[0]
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = version

suppress_warnings = ['image.nonlocal_uri']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# The AppFlow docs contain no or very little Python docs.
# Thus, the primary domain is rst.
primary_domain = 'rst'

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'


def set_rst_settings(app):
    app.env.settings.update({
        'field_name_limit': 0,
        'option_limit': 0,
    })


def setup(app):
    app.add_stylesheet('css/AppFlow.css')
    app.connect('builder-inited', set_rst_settings)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'project_nav_name': 'AppFlow %s' % version,
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['appflow_theme']

# html_extra_path = ['../src/AppFlow/paperkey.html']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['logo-text.html', 'searchbox.html', 'globaltoc.html'],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'AppFlowdoc'


# # -- Options for LaTeX output --------------------------------------------------

# # Grouping the document tree into LaTeX files. List of tuples
# # (source start file, target name, title, author, documentclass [howto/manual]).
# latex_documents = [
#   ('book', 'AppFlow.tex', 'AppFlow Documentation',
#    'The AppFlow Collective', 'manual'),
# ]

# # The name of an image file (relative to this directory) to place at the top of
# # the title page.
# latex_logo = '_static/logo.pdf'

# latex_elements = {
#     'papersize': 'a4paper',
#     'pointsize': '10pt',
#     'figure_align': 'H',
# }

# # For "manual" documents, if this is true, then toplevel headings are parts,
# # not chapters.
# #latex_use_parts = False

# # If true, show page references after internal links.
# #latex_show_pagerefs = False

# # If true, show URL addresses after external links.
# latex_show_urls = 'footnote'

# # Additional stuff for the LaTeX preamble.
# #latex_preamble = ''

# # Documents to append as an appendix to all manuals.
# latex_appendices = [
#     'support',
#     'resources',
#     'changes',
#     'authors',
# ]

# # If false, no module index is generated.
# #latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
        ('usage', 'AppFlow',
         'AppFlowBackup is a deduplicating backup program with optional compression and authenticated encryption.',
         ['The AppFlow Collective (see AUTHORS file)'],
         1),
]

extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

extlinks = {
    'issue': ('https://github.com/AppFlowbackup/AppFlow/issues/%s', '#'),
    'targz_url': ('https://pypi.python.org/packages/source/b/AppFlowbackup/%%s-%s.tar.gz' % version, None),
}
