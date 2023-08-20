from tkinter import*
def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if(scvalue.get().isdigit()):
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                scvalue.set("Error") 
                screen.update()     
    elif text=="C":
        scvalue.set("")
        screen.update()
    elif text=="<--":
        scvalue.set(scvalue.get()[0:len(scvalue.get())-1])
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    scvalue.set(value)  
    screen.update() 
root=Tk()
root.geometry("644x900")
root.configure(bg="orange")
l=Label(root,text="CALCULATOR", font="lucida 35 bold")
l.pack(pady=20)
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,padx=10,pady=10,ipadx=8)
f=Frame(root,bg="grey")
b=Button(f,text="C",font="lucida 35 bold",)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="<--",font="lucida 35 bold",)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="lucida 35 bold",)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 35 bold",)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="9",font="lucida 35 bold")
b.pack(side=LEFT,padx=25,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 35 bold")
b.pack(side=LEFT,padx=24,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 35 bold")
b.pack(side=LEFT,padx=24,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 35 bold")
b.pack(side=LEFT,padx=25,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",font="lucida 35 bold",)
b.pack(side=LEFT,padx=25,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 35 bold",)
b.pack(side=LEFT,padx=24,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 35 bold",)
b.pack(side=LEFT,padx=25,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 35 bold")
b.pack(side=LEFT,padx=24,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",font="lucida 35 bold",)
b.pack(side=LEFT,padx=23,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 35 bold",)
b.pack(side=LEFT,padx=23,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 35 bold",)
b.pack(side=LEFT,padx=23,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="lucida 35 bold",)
b.pack(side=LEFT,padx=23,pady=5,)
b.bind("<Button-1>",click)
f.pack()





f=Frame(root,bg="grey")
b=Button(f,text="00",font="lucida 35 bold",)
b.pack(side=LEFT,padx=22,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="0",font="lucida 35 bold",)
b.pack(side=LEFT,padx=21,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 35 bold",)
b.pack(side=LEFT,padx=22,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 35 bold",)
b.pack(side=LEFT,padx=21,pady=5)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()