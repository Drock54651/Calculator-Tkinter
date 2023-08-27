from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span = 1, color = 'dark-gray' ):
        super().__init__(parent,
                        text = text, 
                        corner_radius = STYLING['corner-radius'],
                        font = font,
                        fg_color = COLORS[color]['fg'],
                        hover_color = COLORS[color]['hover'],
                        text_color = COLORS[color]['text'],
                        command = func,
                        )
        
        self.grid(row = row, column = col, sticky = 'news', padx  =STYLING['gap'], pady= STYLING['gap'], columnspan = span)


class NumButton(Button):
    def __init__(self, parent, text, func, col, row, font, span, color = 'light-gray'):
        super().__init__(parent = parent, 
                        text = text, 
                        func = lambda: func(text), #! makes it possible to pass arguments in functions
                        col = col, 
                        row = row, 
                        font = font, 
                        color = color,
                        span = span)
        
class MathButtons(Button): 
    def __init__(self, parent, text, operator, func, col, row, font, color = 'orange'): 
        super().__init__(parent = parent,
                         text = text,
                         row = row,
                         col = col,
                         func  = lambda: func(operator),
                         font = font,
                         color = color
                         )


class ImageButton(CTkButton):
    def __init__(self, parent, func, col, row, image, text = '', color = 'dark-gray'):
        super().__init__(parent,
                        text = text, 
                        corner_radius = STYLING['corner-radius'],
                        image = image,
                        fg_color = COLORS[color]['fg'],
                        hover_color = COLORS[color]['hover'],
                        text_color = COLORS[color]['text'],
                        command = func)
        
        self.grid(row = row, column = col, sticky = 'news', padx  =STYLING['gap'], pady= STYLING['gap'])


class MathImageButton(ImageButton):
    def __init__(self, parent, operator, func, col, row, image, color = 'orange'):#! Its own def init however can be its own thing
        super().__init__(parent = parent, #! when inheriting from a class, the super init should always have the def __init__ params from the inherited class except the self ofc
                         row = row,
                         col = col,
                         image = image,
                         func  = lambda: func(operator),
                         color = color
                         )
        