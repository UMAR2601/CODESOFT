from tkinter import*
import random
def click1(event):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password=""
    length=int(e2.get())
    for i in range(0,length):
        password=password+random.choice(digits)
    pwd.set(password)   
def click2(event):
    e3.config(bg="green",fg="white")
    
def click3(event):
    name.set("")
    numvalue.set("")
    pwd.set("")
    e3.config(bg="white",fg="black")

    
root=Tk()
root.geometry("600x600")
root.title("password Generator")
root.configure(bg="black")

l=Label(root,text="PASSWORD GENERATOR",font="lucida 35 bold",fg="orange",bg="black")
l.pack(pady=20)

f1=Frame(root,bg="black")
name=StringVar()
l1=Label(f1,text="Enter your name:",font="Times" "30" "bold") 
e1=Entry(f1,textvar=name,font="30")
l1.pack(side=LEFT)
e1.pack(ipady=4,padx=20,pady=20)
f1.pack()

f2=Frame(root,bg="black")
numvalue=StringVar()
l2=Label(f2,text="Length Of password:",font="Times" "30" "bold") 
e2=Entry(f2,font="30",textvar=numvalue)
l2.pack(side=LEFT)
e2.pack(ipady=4,padx=20,pady=20)
f2.pack()

f3=Frame(root,bg="black")
pwd=StringVar()
l3=Label(f3,text="Generated Password:",font="Times" "30" "bold") 
e3=Entry(f3,textvar=pwd,font="30")
l3.pack(side=LEFT)
e3.pack(ipady=4,padx=20,pady=20)
f3.pack()

f4=Frame(root,bg="orange")
l4=Button(f4,text="GENERATE PASSWORD",font="Times" "30" "bold",height=3,width=20,fg="black",bg="orange") 
l4.bind("<Button>",click1)
l4.pack(fill=Y,ipadx=10)
f4.pack(pady=6)

f5=Frame(root,bg="orange")
l5=Button(f5,text="Confirm",font="Times" "30" "bold",height=1,width=15,fg="black",bg="orange") 
l5.bind("<Button>",click2)
l5.pack(ipadx=10)
f5.pack(pady=6)

f6=Frame(root,bg="orange")
l6=Button(f6,text="Reset",font="Times" "30" "bold",height=1,width=15,fg="black",bg="orange") 
l6.pack(ipadx=10)
l6.bind("<Button>",click3)
f6.pack()

root.mainloop()