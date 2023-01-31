#!/usr/bin/env python
"""
Example on using the latexlides module, i.e., writing (LaTeX)
slides in Python.

Usage:

unix> python exampletalk.py
unix> # run last output line from the above command:
unix> latex exampletalk.tex; dvips exampletalk.dvi; ps2pdf exampletalk.ps; acroread exampletalk.pdf

Read the PDF file and this source code file in parallel. It takes 10 minutes,
and afterwards you are probably ready to write your own talk.
"""

from latexslides import *

# We recommend to use raw strings (r'some string') because a backslash
# is then a backslash and that's convenient when writing LaTeX.

# Now for the official title page of the talk; we can define
# Python variables and use these in text strings to make things
# more compact and easier to change.

# First set a few module variables:
package = BeamerSlides # Can also be 'ProsperSlides' and 'HTMLSlides'
beamer_theme = 'hpl1' #'shadow', 'Darmstadt' are other themes
prosper_style = 'hplplainsmall' # 'default', 'hplplain' are other themes
header_footer = True # Decorations are turned on

# Add newcommands:
newcommands = r"""\newcommand{\OBS}[1]{\marginpar{\scriptsize##1}}"""

# Set institutions:
gsup = "School of Geographical Sciences and Urban Planning,"
asu="Arizona State University"
geoda = "GeoDa Center for Gecomputation and Spatial Analysis"

# Set authors:
sjr = 'Sergio J. Rey'

slides = package(title='GPH 483/598 Geographic Information Analysis',
                 author_and_inst=[(sjr,geoda,gsup,asu)],
                 date='Spring 2010',
                 beamer_theme=beamer_theme,
                 prosper_style=prosper_style,
                 header_footer=header_footer,
                 titlepage_figure='wave-dueto-slide.ps',
                 titlepage_figure_pos='s', # Figure to the south
                 titlepage_figure_fraction_width=0.5,
                 #titlepage_left_column_width=1., # If figure to the east 
                 toc_heading='List of Topics',
                 toc_figure='python1.ps',
                 toc_figure_fraction_width=1,
                 toc_left_column_width=0.5,
                 newcommands=newcommands)

# Exemplify raw LaTeX, please note that the code is for Beamer,
# so if you want to use Prosper, you should comment out this slide
# when writing to file:
first_intro = RawSlide(r"""

\begin{frame} %% plain: no header and footer

\frametitle{Do you use \LaTeX{} for writing slides?}
Continue studying these slides if your answer to at least one of
the following questions is 'yes':
\begin{enumerate}
\item Are you using prosper for writing slides?
\item Have you not yet discovered latex-beamer?
\item Would you like your slide collection to be independent of what
is the currently most popular \LaTeX~slide package?
\item Would you like to write less \LaTeX~source code when you
create presentations?
\item Would like to get more flexibility than what plain ASCII
files with \LaTeX~source provide?
\end{enumerate}
\end{frame}
""",
hidden=False)

# The talk can be divided into sections, subsections, etc., and
# then a toc is automatically generated, navigation utilities
# are included in the header etc.

s_intro = Section(r'Intro to Latexslides', short_title='Intro')
ss_objectives=SubSection('Objectives','Objectives')
ss_components=SubSection('Components','Components')
ss_schedule=SubSection('Schedule')


s_logistics=Section('Logistics')
ss_grading=SubSection('Grading')
ss_reading=SubSection('Reading')
ss_software=SubSection('Software')

s_intro_GIA=Section('Introduction to Geographic Information Analysis')
ss_big_picture=SubSection('GIS and Spatial Analysis')
ss_eda_esda=SubSection('EDA and ESDA')

objectives =\
BulletSlide('Course Objectives',
            ['Introduce fundamentals of ESDA',
             'Conceptual and theoretical background',
             'Hands-on experience'
             ],
            dim='single_then_all')


components =\
Slide('Components',
      [BulletBlock(heading='Four Sections:',
                  bullets=
            ['Introduction to Spatial Data',
             'Point Patterns',
             'Lattice Data',
             'Geostatistics'
             ],)],
            dim='single_then_all')

book=\
Slide('Textbook',
      figure='gia.ps',
      figure_fraction_width=0.5)

lbook=\
Slide('Textbook',
      [BulletBlock(['Readings assigned by topic',
                    'Support lecture',
                    'To be read prior to lecture'])],
      figure='gia.ps',
      figure_pos='e',
      left_column_width=0.6,
      figure_fraction_width=0.5)


book=\
Slide('GIS Then',
      figure='snowmap1.pdf',
      figure_fraction_width=0.5)



# Collect slide objects:
collection = [
s_intro,
ss_objectives,
objectives,
ss_components,
components,
s_logistics,
ss_grading,
components,
ss_reading,
book,
lbook,
ss_software,
components,
s_intro_GIA,
ss_big_picture,
ss_eda_esda,
]

for c in collection:
    slides.add_slide(c)
# Write slides to file:
filename = 'gph483s10_01.tex'
slides.write(filename)


