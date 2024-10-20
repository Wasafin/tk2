from tkinter import *

# creating tk
Window = Tk()
Window.title('Widgets')
Window.geometry('480x480')

# Label 1
l1 = Label(text="Hello!",bg="Black",fg="white")
l1.pack()

# label 2
l2 = Label(text="Enter your name")
l2.pack()

# enter name
name = Entry()
name.pack()

# def getting name, which name
def hello():
    namestore = name.get()
    
    # greet name
    greet = "Hello" + namestore
    
    # greet label
    greetlabel.config(text=greet)

# pack the greet label
greetlabel = Label(text="")
greetlabel.pack()

# creating the button
b1 = Button(text="Click here!",bg="black",fg="white",height=3,command=hello)
b1.pack()

# adding text box
x = Text()
x.pack()

# end
Window.mainloop()
