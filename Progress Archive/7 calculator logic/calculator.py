import customtkinter as ctk
import darkdetect
from settings import *
from PIL import Image, ImageTk
from buttons import Button, ImageButton, NumButton, MathButtons, MathImageButton
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass


class Calculator(ctk.CTk):
	def __init__(self, is_dark):
		super().__init__(fg_color = (WHITE,BLACK))

		#* SETUP
		ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
		self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
		self.resizable(False, False)
		self.title('')
		self.iconbitmap('1 window/empty.ico')
		self.title_bar_color(is_dark)
		
		#* GRID LAYOUT
		self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = 'a')
		self.columnconfigure(list(range(MAIN_COLUMNS)), weight = 1, uniform = 'a')
		
		#* DATA
		self.formula_string = ctk.StringVar()
		self.result_string = ctk.StringVar(value = '0')
		self.display_nums = []
		self.full_operation = []


		#* WIDGETS
		self.create_widgets()


		
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


	def create_widgets(self): #! contains all the widgets i.e output and buttons
		
		#* FONTS
		main_font = ctk.CTkFont(family = FONT, size = NORMAL_FONT_SIZE)
		result_font = ctk.CTkFont(family = OUTPUT_FONT_SIZE, size = OUTPUT_FONT_SIZE)

		#* OUTPUT LABELS
		OutputLable(self, 0, 'se', main_font, self.formula_string) #! formula
		OutputLable(self, 1, 'e', result_font, self.result_string) #! result

		#* CLEAR (AC) BUTTON
		Button(parent = self, 
		text = OPERATORS['clear']['text'], 
		func = self.clear,
		col = OPERATORS['clear']['col'], 
		row = OPERATORS['clear']['row'],
		font = main_font)
		
		#* PERCENTAGE BUTTON
		Button(parent = self, 
		text = OPERATORS['percent']['text'], 
		func = self.percent,
		col = OPERATORS['percent']['col'], 
		row = OPERATORS['percent']['row'],
		font = main_font)

		#* INVERT BUTTON
		invert_image = ctk.CTkImage(dark_image = Image.open(OPERATORS['invert']['image path']['light']), 
			      					light_image = Image.open(OPERATORS['invert']['image path']['dark']))
		

		ImageButton(parent  = self, 
	      image = invert_image, 
		  func = self.invert, 
		  row = OPERATORS['invert']['row'], 
		  col = OPERATORS['invert']['col'],
		  text  = OPERATORS['invert']['text'])
		

		#* NUMBER BUTTONS
		for num, data in NUM_POSITIONS.items(): #! num is the key, data is the value which in this case is another dictionary
			NumButton(parent = self,
			text = num,
			func = self.num_press, #! parameter passed via numbutton class in buttons.py
			row = data['row'],
			col = data['col'],
			font  = main_font,
			span = data['span'])


		#* MATH BUTTONS
		for operator, data in MATH_POSITIONS.items():

			if data['image path']:
				divide_image  = ctk.CTkImage(light_image = Image.open(data['image path']['dark']),
			  										dark_image = Image.open(data['image path']['light']))
				
				MathImageButton(parent = self,
				row = data['row'],
				col = data['col'],
				image  = divide_image,
				operator = operator,
				func = self.math_press)


			else:

				MathButtons(parent = self,
				row = data['row'],
				col = data['col'],
				text = data['character'],
				font = main_font,
				operator = operator,
				func = self.math_press)



	def clear(self):
		self.formula_string.set('')
		self.result_string.set(0)
		self.display_nums.clear()


	def percent(self):
		#TODO: divide current value by 100
		 if self.display_nums:
				
				current_number = float(''.join(self.display_nums))
				percent_number = current_number / 100
				self.display_nums = list(str(percent_number))
				self.result_string.set(percent_number)
				
	def invert(self):
		current_number = ''.join(self.display_nums)
		if current_number: #! check positive or negative
			
			if float(current_number) > 0:
				self.display_nums.insert(0, '-')
			else:
				
				del self.display_nums[0]
			
			self.result_string.set(''.join(self.display_nums))
		
	def num_press(self, value):	#! value here is the actual number
		self.display_nums.append(str(value)) #! appends input to a list
		full_number = ''.join(self.display_nums) #! joins the numbers in the list, putting stuff in the '' is what will be in between the numbers
		self.result_string.set(full_number)

	def math_press(self, value): #! value here is the operation such as * for multiplication
		current_number = ''.join(self.display_nums)
		if current_number:
			self.full_operation.append(current_number)
			if value != '=':
				
				#* UPDATE DATA
				self.full_operation.append(value)
				self.display_nums.clear()

				#* UPDATE OUTPUT
				self.result_string.set('')
				self.formula_string.set(' '.join(self.full_operation))
			
			else:
				formula = ' '.join(self.full_operation)
				result = eval(formula)

				#* RESULT FORMAT
				if isinstance(result, float):

					if result.is_integer():
						result = int(result)

					else:
						result = round(result,3)
				
				
				#TODO: update output, clear the full operation list, display nums should have the value of the result
				
				self.result_string.set(result)
				self.formula_string.set(formula)

				self.full_operation.clear()

				self.display_nums = [str(result)]

				# self.display_nums
			





class OutputLable(ctk.CTkLabel): #! Shows formula and also result output from formula
	def __init__(self, parent, row, anchor, font, string_var):
		super().__init__(parent, textvariable = string_var, font = font)
		self.grid(row = row, column = 0, columnspan = 4, sticky = anchor, padx = 10)


if __name__ == '__main__':
	Calculator(darkdetect.isDark()) #! reutrns true if user is using dark mode