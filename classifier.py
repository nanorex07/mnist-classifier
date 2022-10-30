import os
from tkinter import *
import customtkinter
import PIL
from PIL import ImageGrab
import nn

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Main:
	def __init__(self,master):
		self.master = master
		self.res = ""
		self.pre = [None,None]
		self.bs = 5
		self.c = Canvas(self.master,width=282,height=282,bg='black')
		self.c.pack(pady=10)
		customtkinter.CTkButton(self.master,text="Clear Canvas", text_font=("monospace", 10),command=self.clear).pack(pady=10)
		customtkinter.CTkButton(self.master,text=" Predict ", text_font=("monospace", 10),command=self.getResult).pack(pady=10)
		self.lb = customtkinter.CTkLabel(self.master, text_font=("monospace", 14), text="Draw on canvas and click predict")
		self.lb.pack()
		self.c.bind("<Button-1>",self.putPoint)
		self.c.bind("<B1-Motion>", self.paint)

	def getResult(self):
		x = self.master.winfo_rootx() + self.c.winfo_x()
		y = self.master.winfo_rooty() + self.c.winfo_y()
		x1 = x + self.c.winfo_width()
		y1 = y + self.c.winfo_height()   
		img = PIL.ImageGrab.grab()
		img = img.crop((x+2, y+2, x1-2, y1-2))
		img = img.resize((28,28))
		img.save("dist.png")
		self.res = str(nn.predict("dist.png"))
		self.lb.config(text = "It's a "+ self.res)

	def clear(self):
		self.c.delete('all')

	def putPoint(self,e):
		self.c.create_oval(e.x-self.bs,e.y-self.bs,e.x+self.bs,e.y+self.bs,outline='white',fill='white')
		self.pre = [e.x,e.y]

	def paint(self,e):
		self.c.create_line(self.pre[0], self.pre[1], e.x, e.y,width=self.bs*2, fill='white',capstyle=ROUND, smooth=TRUE)

		self.pre = [e.x,e.y]


if __name__ == "__main__":
	root = customtkinter.CTk()
	Main(root)
	root.title('Digit Classifier')
	root.resizable(0,0)
	root.mainloop()
