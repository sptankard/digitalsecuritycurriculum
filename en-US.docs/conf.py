
extensions = []
templates_path = ['_templates']

# source_suffix = '.rst'

master_doc = 'index'

project = u'Digital security and privacy workshop'
copyright = u'and copyleft 12018, People'
author = u'People'

version = u''
release = u''

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'sphinx_rtd_theme' # 'default'
#html_theme_options = { 'style_external_links': True }

html_static_path = ['_static']
htmlhelp_basename = 'Digitalsecurityandprivacyworkshopdoc'

latex_show_urls = 'footnote'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\usepackage{lastpage}
\usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhead{} % clear all header fields
    \cfoot{\thepage\ / \pageref*{LastPage}}

\usepackage{libertine}

''',
}

full_title = u'Digital security and privacy workshop'

latex_documents = [

    ('digsec-intro',
     'digsec-intro.tex',
     full_title + u'\\\\  --  Intro segment',
     u'', # u'People',
     'howto',
     False
    ),

    # (master_doc,
    #  'Digitalsecurityandprivacyworkshop-full.tex',
    #  full_title,
    #  u'', # u'People',
    #  'manual',
    #  True
    # ),

]

man_pages = [
    (master_doc,
     'digitalsecurityandprivacyworkshop',
     full_title,
     [author],
     1
    )
]

texinfo_documents = [
    (master_doc,
     'Digitalsecurityandprivacyworkshop',
     full_title,
     author,
     'Digitalsecurityandprivacyworkshop',
     'One line description of project.',
     'Miscellaneous'
    ),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']

# Markdown support

source_suffix = ['.rst', '.md']

from recommonmark.parser import CommonMarkParser
source_parsers = {
	'.md': CommonMarkParser,
}
