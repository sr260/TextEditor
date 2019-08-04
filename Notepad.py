from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os


def newfile():
	global file
	root.title("Untitled-Writepad")
	file=None
	TextArea.delete(1.0,END)

def openfile():
	global file
	file= askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
	if file=="":
		file=None
	else:
		root.title(os.path.basename(file)+" -Writepad")
		TextArea.delete(1.0,END)
		f=open(file,"r")
		TextArea.insert(1.0,f.read())
		f.close()

def savefile():
	global file
	if file ==None:
		file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if file=="":
			file=None
		else:
			f=open(file,"w")
			f.write(TextArea.get(1.0,END))
			f.close()

			root.title(os.path.basename(file)+" -Writepad")
			print("Saved")

	else:
		f=open(file,"w")
		f.write(TextArea.get(1.0,END))
		f.close()

def quit():
	root.destroy()

def cut():
	TextArea.event_generate("<<Cut>>")

def copy():
	TextArea.event_generate("<<Copy>>")

def paste():
	TextArea.event_generate("<<Paste>>")

def about():
	showinfo("Notepad","A Text Editor")

if __name__=='__main__':
	root=Tk()
	root.title("Untitled-Writepad")
	root.geometry("644x780")
	TextArea= Text(root,font="lucida 13")
	TextArea.pack(expand=True,fill=BOTH)

	file=None

	Menubar= Menu(root)
	
	FileMenu= Menu(Menubar,tearoff=0)
	FileMenu.add_command(label="New",command=newfile)
	FileMenu.add_command(label="Open",command=openfile)
	FileMenu.add_command(label="Save",command=savefile)
	FileMenu.add_separator()
	FileMenu.add_command(label="Exit",command=quit)
	Menubar.add_cascade(label="File",menu=FileMenu)

	EditMenu= Menu(Menubar,tearoff=0)

	EditMenu.add_command(label="Cut",command=cut)
	EditMenu.add_command(label="Copy",command=copy)
	EditMenu.add_command(label="Paste",command=paste)
	Menubar.add_cascade(label="Edit",menu=EditMenu)
	
	HelpMenu= Menu(Menubar,tearoff=0)
	HelpMenu.add_command(label="About",command=about)
	Menubar.add_cascade(label="Help",menu=HelpMenu)

	root.config(menu=Menubar)
	Scrollbar= Scrollbar(TextArea)
	Scrollbar.pack(side=RIGHT,fill=Y)
	Scrollbar.config(command=TextArea.yview)
	TextArea.config(yscrollcommand=Scrollbar.set)
	
	root.mainloop()

	