
from latexslides import *

slides = ProsperSlides(title="Exampletalk",
                       prosper_style='exampletalk',
                       titlepage=False,
                       toc_heading=None,)

slide1 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # First set a few@# Exemplify
''', fontsize='tiny')])

slide3 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # Exemplify raw@# The talk
''', fontsize='tiny')])

slide4 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # The talk can be@what_is
''', fontsize='tiny')])

slide5 = Slide(content=[Code(r'''
@@@CODE exampletalk.py what_is@subsec
''', fontsize='tiny')])

slide6 = Slide(content=[Code(r'''
@@@CODE exampletalk.py subsec_p@ex1
''', fontsize='tiny')])

slide7 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex1 =@structure
''', fontsize='tiny')])

slide8 = Slide(content=[Code(r'''
@@@CODE exampletalk.py structure =@blocks
''', fontsize='tiny')])

slide9 = Slide(content=[Code(r'''
@@@CODE exampletalk.py blocks =@classes
''', fontsize='tiny')])

slide10 = Slide(content=[Code(r'''
@@@CODE exampletalk.py classes =@dimming
''', fontsize='tiny')])

slide16 = Slide(content=[Code(r'''
@@@CODE exampletalk.py dimming =@why =
''', fontsize='tiny')])

slide22 = Slide(content=[Code(r'''
@@@CODE exampletalk.py why =@# Short form
''', fontsize='tiny')])

slide31 = Slide(content=[Code(r'''
@@@CODE exampletalk.py # Short form@figures =
''', fontsize='tiny')])

slide32 = Slide(content=[Code(r'''
@@@CODE exampletalk.py figures =@ex_fig = 
''', fontsize='tiny')])

slide33 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_fig =@ex_fig2 =
''', fontsize='tiny')])

slide34 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_fig2 =@ex_fig3
''', fontsize='tiny')])

slide35 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_fig3 =@multiple_figs =
''', fontsize='tiny')])

slide36 = Slide(content=[Code(r'''
@@@CODE exampletalk.py multiple_figs =@subsec_code = 
''', fontsize='tiny')])

slide37 = Slide(content=[Code(r'''
@@@CODE exampletalk.py subsec_code =@code_obj = 
''', fontsize='tiny')])

slide38 = Slide(content=[Code(r'''
@@@CODE exampletalk.py code_obj =@code_obj_result = 
''', fontsize='tiny')])

slide39 = Slide(content=[Code(r'''
@@@CODE exampletalk.py code_obj_result =@sec_specials =
''', fontsize='tiny')])

slide40 = Slide(content=[Code(r'''
@@@CODE exampletalk.py sec_specials =@sections =
''', fontsize='tiny')])

slide41 = Slide(content=[Code(r'''
@@@CODE exampletalk.py sections =@navigation = 
''', fontsize='tiny')])

slide42 = Slide(content=[Code(r'''
@@@CODE exampletalk.py navigation =@ex_header =
''', fontsize='tiny')])

slide43 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_header =@prosper =
''', fontsize='tiny')])

slide44 = Slide(content=[Code(r'''
@@@CODE exampletalk.py prosper =@ex_titlepage =
''', fontsize='tiny')])

slide45 = Slide(content=[Code(r'''
@@@CODE exampletalk.py ex_titlepage =@emacs =
''', fontsize='tiny')])

slide46 = Slide(content=[Code(r'''
@@@CODE exampletalk.py emacs =@# Note
''', fontsize='tiny')])

slide47 = Slide(content=[Code(r'''
@@@CODE exampletalk.py slide_obj1 =@slide_obj2 =
''', fontsize='tiny')])

slide48 = Slide(content=[Code(r'''
@@@CODE exampletalk.py slide_obj2 =@compiling =
''', fontsize='tiny')])

slide49 = Slide(content=[Code(r'''
@@@CODE exampletalk.py compiling =@maths =
''', fontsize='tiny')])

slide50 = Slide(content=[Code(r'''
@@@CODE exampletalk.py maths =@learning =
''', fontsize='tiny')])

slide51 = Slide(content=[Code(r'''
@@@CODE exampletalk.py learning =@# Make
''', fontsize='tiny')])

collection = [
    slide1,
    slide3,
    slide4,
    slide5,
    slide6,
    slide7,
    slide8,
    slide9,
    slide10,
    slide16,
    slide22,
    slide31,
    slide32,
    slide33,
    slide34,
    slide35,
    slide36,
    slide37,
    slide38,
    slide39,
    slide40,
    slide41,
    slide42,
    slide43,
    slide44,
    slide45,
    slide46,
    slide47,
    slide48,
    slide49,
    slide50,
    slide51,
]

slides.add_slides(collection)
slides.write('textexampletalk.p.tex')
