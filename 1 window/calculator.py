import customtkinter as ctk
import darkdetect
from settings import *
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass


class Calculator(ctk.CTk):
	def __init__(self, is_dark):
		super().__init__(fg_color = (WHITE,BLACK))

		#* SETUP
		#TODO: set appearance to dark or light depending on is_dark
		#TODO: fg_color = white or black depending on dark or light
		#TODO: get the start window size from settings and disable window Resizing
		#TODO: Hide the title and icon
		
		ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
		self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
		self.resizable(False, False)
		self.title('')
		self.iconbitmap('1 window/empty.ico')
		self.title_bar_color(is_dark)
		
		#* LAYOUT
		self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = 'a')
		self.columnconfigure(list(range(MAIN_COLUMNS)), weight = 1, uniform = 'a')
		



		
		#* RUN
		self.mainloop()



	#* METHODS

	def title_bar_color(self, is_dark):
		try:

			HWND = windll.user32.GetParent(self.winfo_id())
			DWMWA_ATTRIBUTE = 35
			COLOR = TITLE_BAR_HEX_COLORS['dark'] if is_dark else TITLE_BAR_HEX_COLORS['light']
			windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))

		except:
			pass





if __name__ == '__main__':
	Calculator(darkdetect.isDark()) #! returns true if user is using dark mode