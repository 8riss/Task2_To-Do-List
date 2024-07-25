import tkinter
from tkinter import *


root=Tk()
root.title("TO DO LIST")
root.geometry("400x600+450+100")
root.resizable(False, False)

task_list =  []
def addTask():
    task=task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("taskist.txt", 'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete(ANCHOR)
        
        
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt', 'w')
        file.close()





TopImage = PhotoImage(file = "Downloads/Tab.png")
Label(root, image=TopImage).pack()

DockImage = PhotoImage(file = "Downloads/dock.png")
Label(root, image=DockImage).place(x=30, y=40)

heading = Label(root, text=" ALL TASK☑", font="zain 40", fg="white", bg="#32405b")
heading.place(x=115, y=25)




#Main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)
task = StringVar()
task_entry =  Entry(frame, width = 19, font="zain 28", border=0)
task_entry.place(x=5, y=5)
task_entry.focus()


button = Button(frame, text="ADD", font="zain 26", width=3, bg="dark blue", fg="#fff", bd=0, command=addTask)
button.place(x=308, y=6)



#List
frame1 = Frame(root, bd=2, width=600, height=200, bg="white")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font="zain 15", width=45, height=5, bg="sky blue", fg="white", cursor="hand2")
listbox.pack(side=LEFT, fill=BOTH, padx=3)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#Delete
del_icon = PhotoImage(file = "Downloads/delete.png")
Button(root, image=del_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=12)



root.mainloop()
