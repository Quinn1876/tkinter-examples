"""
This is a general Example of the Tkinter modual
https://www.tutorialspoint.com/python/python_gui_programming.htm
"""

from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)

		self.master = master
		self.init_window()

	def init_window(self):

		self.master.title("GUI")
		self.pack(fill=BOTH, expand=1)

		# quitButton = Button(self, text="Quit", command=self.client_exit)
		# quitButton.place(x=0, y=0)

		# topMenu is the menu bar at the top of the window
		# file is one of the menu options in the menu bar
		# inside of the file menu is the "Exit" command which will execute a method
		topMenu = Menu(self.master)
		self.master.config(menu=topMenu)

		file = Menu(topMenu)
		file.add_command(label="Exit", command=self.client_exit)

		edit = Menu(topMenu)
		edit.add_command(label="Undo")
		edit.add_command(label="Show Image", command=self.showImg)
		edit.add_command(label="Show Text", command=self.showTxt)

		topMenu.add_cascade(label="File", menu=file)
		topMenu.add_cascade(label="Edit", menu=edit)

	def client_exit(self):
		exit()

	def showImg(self):
		load = Image.open('volleyball.png').resize((400, 300))

		render = ImageTk.PhotoImage(load)

		img = Label(self, image=render)
		img.image = render
		img.place(x=0, y=0)

	def showTxt(self):
		text = Label(self, text='Hey there good lookin!')
		text.pack()


root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
