from tkinter import*
root=Tk()
root.config(bg="pink")
root.geometry("1600x1000")



def click1(event):
    li1.insert(0,e1.get())
    entry1.set("")
     
def click2(event):
    li1.delete(0,END)


f1=Frame(root,bg="pink")
l1=Label(f1,text="---To Do List---",font="lucida 35 bold")
l1.pack()
f1.pack(pady=20)

f2=Frame(root,bg="pink")
l21=Label(f2,text="Add Task",font="lucida 35 bold")
l21.pack(side=LEFT, padx=100)
l22=Label(f2,text="Tasks",font="lucida 35 bold")
l22.pack(side=RIGHT ,padx=250)
f2.pack()


f3=Frame(root,bg="pink")
entry1=StringVar()
e1=Entry(f3,textvariable=entry1,font=50)
e1.pack(side=LEFT )
b1=Button(f3,text="CLick here to Add",font="lucida 12  bold")
b1.pack(side=LEFT,padx=30,pady=10)
b1.bind("<Button>",click1)
b2=Button(f3,text="Reset",font="lucida 12  bold")
b2.bind("<Button>",click2)
b2.pack(side=LEFT)

li1=Listbox(f3,height =20,width=50,font="lucida 12  bold")
li1.pack(side=RIGHT,padx=70,pady=20,ipadx=40,ipady=20)
f3.pack()

f4=Frame(root,bg="pink")
b3=Button(f3,text="Remove",font="lucida 12  bold")
b3.pack(side=LEFT)
f4.pack(side=LEFT)



root.mainloop()