
extensions = []
templates_path = ['_templates']

# source_suffix = '.rst'

master_doc = 'index'

project = u'Digital security and privacy workshop'
copyright = u'2018, People'
author = u'People'

version = u''
release = u''

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'default'
# html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'Digitalsecurityandprivacyworkshopdoc'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'Digitalsecurityandprivacyworkshop.tex', u'Digital security and privacy workshop',
     u'People', 'manual'),
]

man_pages = [
    (master_doc, 'digitalsecurityandprivacyworkshop', u'Digital security and privacy workshop',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Digitalsecurityandprivacyworkshop', u'Digital security and privacy workshop',
     author, 'Digitalsecurityandprivacyworkshop', 'One line description of project.',
     'Miscellaneous'),
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
