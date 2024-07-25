import tkinter
from tkinter import *


root=Tk()
root.title("TO DO LIST")
root.geometry("400x600+450+100")
root.resizable(False, False)

task_list =  []

Image_icon = PhotoImage(file = "Image/task.png")
root.iconphoto(False, Image_icon)
Label(root, image=Image_icon).pack()


root.mainloop()

