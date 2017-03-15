from tkinter import *
from tkinter import ttk
import random

class GUI:
	def __init__(self, master):
		self.master = master
		master.title("JJAY Veterans Association HID Scanner")
		master.update_idletasks()
		width = 400
		height = 400
		x = (master.winfo_screenwidth() // 2) - (width // 2)
		y = (master.winfo_screenheight() // 2) - (height // 2)
		master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

		self.randLabel = Label(master, text="Number read: ")
		self.randLabel.pack()
		#self.randDisplay = StringVar()

		self.display_button = Button(master, text="Random", command=self.randGen)
		#self.display_button.grid(row=1, column=0, sticky = W)
		self.display_button.pack()

		'''
		self.label = Label(master, text="Enter a message: ")
		#self.label.grid(row=0, sticky = W)
		self.label.pack()

		self.display = StringVar()
		self.display_entry = ttk.Entry(master, width=40, textvariable=self.display)
		#self.display_entry.grid(row=0, column=1)
		self.display_entry.pack()

		self.display_button = Button(master, text="Enter", command=self.displayMessage)
		#self.display_button.grid(row=1, column=0, sticky = W)
		self.display_button.pack()
		'''
		self.close_button = Button(master, text="Close", command=master.quit)
		#self.close_button.grid(row=1, column=1, sticky = E)
		self.close_button.pack()


	def displayMessage(self):
		self.displayText = self.display.get()
		self.displayLabel = Label(self.master, text=self.displayText).pack()
		#self.displayLabel.grid(row=3, stick= W)

	def randGen(self):
		self.a = random.randint(1,10)
		if self.a%2 == 0:
			#self.displayRand = Label(self.master, text=self.a).pack()
			self.EnterMessage()
		#print(self.a)
		
	def EnterMessage(self):
		self.label = Label(self.master, text="Enter a message: ")
		#self.label.grid(row=0, sticky = W)
		self.label.pack()

		self.display = StringVar()
		self.display_entry = ttk.Entry(self.master, width=40, textvariable=self.display)
		#self.display_entry.grid(row=0, column=1)
		self.display_entry.pack()

		self.display_button = Button(self.master, text="Enter", command=self.displayMessage)
		#self.display_button.grid(row=1, column=0, sticky = W)
		self.display_button.pack()

if __name__ == "__main__":
	root = Tk()
	my_gui = GUI(root)
	root.mainloop()