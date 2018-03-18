import ip
from sys import*
from tkinter import *
from tkinter import ttk 
window = Tk()
window.title("WELCOME TO THE EAGLES EYE")
window.geometry('1900x3700')
btn1 = ttk.Button(window , text = "enter ")
btn1.pack()
label2 = Label(window, text = "USERNAME", font = ("BOLD",15))
label3 = Label(window, text = "PASSWORD", font = ("BOLD",15))
entry2 = Entry(window)
entry3 = Entry(window)
label2.grid(row=0)
label3.grid(row= 1)
a = entry2.grid(row = 0, column = 1)
b = entry3.grid(row = 1 , column = 1)
btn1.config(command = if entry2.grid == "palsom4u" and entry3.grid == "ronaldo":
            ip.ips()



else:
    sys.exit()

window.mainloop()
