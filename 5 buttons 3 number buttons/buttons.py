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

#TODO:  Get the 0 button to span 2 columns, make sure that exisiting buttons dont break
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


