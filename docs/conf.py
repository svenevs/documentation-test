# -*- coding: utf-8 -*-
#
# NanoGUI documentation build configuration file, created by
# sphinx-quickstart on Sat Jun 18 06:30:54 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'breathe'
]

#
# Breathe setup for linking sphinx and doxygen
#
breathe_projects = { 'NanoGUI' : './doxyoutput/xml' }
breathe_default_project = 'NanoGUI'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'NanoGUI'

build_datetime = datetime.datetime.now()
build_year     = build_datetime.year
build_month    = build_datetime.month
build_day      = build_datetime.day
build_hour     = build_datetime.hour
build_minute   = build_datetime.minute
build_second   = build_datetime.second

copyright = u'{}, Wenzel Jakob'.format(build_year)
author = u'Wenzel Jakob'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = 'rc'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'cpp'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

    html_context = {
        'css_files': [
            '_static/theme_overrides.css'
        ]
    }
else:
    html_context = {
        'css_files': [
            '//media.readthedocs.org/css/sphinx_rtd_theme.css',
            '//media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/theme_overrides.css'
        ]
    }

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#     'nav_pages' : [('About', 'about'), ('Usage', 'usage'), ('Library API', 'library_api')],
# }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ['.']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'NanoGUI: Minimalistic GUI library for OpenGL'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'NanoGUI'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'NanoGUIdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'NanoGUIdoc.tex', u'NanoGUI Documentation',
   u'Wenzel Jakob', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nanoguidoc', u'NanoGUI Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'NanoGUI', u'NanoGUI Documentation',
   author, 'NanoGUI', 'A Minimalistic GUI library for OpenGL.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

primary_domain = 'cpp'
highlight_language = 'cpp'


# Approach modified from Breathe's read the docs
def generate_doxygen_xml():
    '''
    (Re)build the doxygen xml required for 'breathe' _always_, not just
    on the RTD server.
    '''
    import subprocess
    try:
        ret = subprocess.call(["doxygen"])
        if ret != 0:
            sys.stderr.write("Non-zero return code from 'doxygen'...")
    except Exception as e:
        sys.stderr.write("Unable to execute 'doxygen': {}".format(e))


def generate_library_api():
    '''
    Runs breathe and manipulates its parsing to generate a more coherent
    file / namespace / class hierarchy.
    '''
    # declare the library specific filename, title, and description for the
    # top of the library api page
    import textwrap
    library_api_directory = "generated_api"# note: absolute, or relative to __CONF.PY__
    library_api_file  = "library_root.rst"
    library_api_title = "Library API"
    library_api_brief = textwrap.dedent('''
    .. warning::

       Please be advised that the reference documentation discussing NanoGUI
       is currently being developed.  Presented below is *only* the **C++**
       API.  If you are using the **Python** API, the contents below are still
       applicable for understanding what methods are available.  **Python** users
       are advised to refer to the more concise ``example2`` program for
       understanding how to wield the **C++** API using **Python** --- all of the
       relevant **C++** API is bound to **Python** using ``pybind11``.
    ''')
    library_api_summary = textwrap.dedent('''
    .. warning::

       Pthis iaasdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfaeatherae asdf :FLK DS ;yiSDF: yiwefe be advitherae asdf :FLK DS ;yiSDF: yiwefed that the reference documentation ditherae asdf :FLK DS ;yiSDF: yiwefcutherae asdf :FLK DS ;yiSDF: yiweftherae asdf :FLK DS ;yiSDF: yiwefing NanoGUI
       itherae asdf :FLK DS ;yiSDF: yiwef currentthitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfay being devethitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfaoped.  Pretherae asdf :FLK DS ;yiSDF: yiwefented bethitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfaow itherae asdf :FLK DS ;yiSDF: yiwef *onthitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfay* the **C++**
       API.  If you are utherae asdf :FLK DS ;yiSDF: yiwefing the **Python** API, the contenttherae asdf :FLK DS ;yiSDF: yiwef bethitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfaow are therae asdf :FLK DS ;yiSDF: yiweftithitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfathitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfa
       appthitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfaicabthitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfae for undertherae asdf :FLK DS ;yiSDF: yiweftanding what methodtherae asdf :FLK DS ;yiSDF: yiwef are avaithitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfaabthitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfae.  **Python** utherae asdf :FLK DS ;yiSDF: yiwefertherae asdf :FLK DS ;yiSDF: yiwef
       are advitherae asdf :FLK DS ;yiSDF: yiwefed to refer to the more concitherae asdf :FLK DS ;yiSDF: yiwefe ``exampthitherae asdf :FLK DS ;yiSDF: yiwef iaatherae asdf :FLK DS ;yiSDF: yiwefdf itherae asdf :FLK DS ;yiSDF: yiwef how you warnt the peopleatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfatherae asdf :FLK DS ;yiSDF: yiwefdfae2`` program for
       undertherae asdf :FLK DS ;yiSDF: yiweftanding how to wield the **C++** API utherae asdf :FLK DS ;yiSDF: yiwefing **Python** --- all of the
       relevant **C++** API itherae asdf :FLK DS ;yiSDF: yiwef bound to **Python** utherae asdf :FLK DS ;yiSDF: yiwefing ``pybind11``.
    ''')

    # import the exhale module from the current directory and generate the api
    sys.path.append(os.path.abspath('.'))
    from exhale import generate
    # change to pass a dict with defaults for locations etc
    generate(library_api_directory, library_api_file, library_api_title, library_api_brief, library_api_summary, "./doxyoutput/xml/index.xml")


def setup(app):
    # Approach borrowed from the Sphinx docs
    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value'
    )

    # Add hook for building doxygen xml when needed
    # app.connect("builder-inited", generate_doxygen_xml)
    generate_doxygen_xml()
    generate_library_api()
    # app.add_config_value('documentation_build', 'development', True)
