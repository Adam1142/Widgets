from tkinter import *
from datetime import date
root = Tk()
root.title("Getting Started With Widgets")
root.geometry("400x300")
lvl = Label(text="Hey There",fg="white",bg="#072F5F",height=1,width=300)
name_lvl = Label(text="Full Name",bg="#3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    message = "Welcom To The Application \nToday's Date is: "
    Greet = "Hello "+name+"\n"
    text_box.insert(END,Greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
    text_box = Text(height = 3)
    btn = Button(text = "begin",command = display,height = 1,bg = "#1261A0",fg = "white")
    lvl.pack()
    name_lvl.pack()
    name_entry.pack()
    text_box.pack()