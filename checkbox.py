from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkbox")
root.geometry("400x400")

def show():
    result = var.get()
    my_label = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="Pizza", offvalue="Hamburger")
c.deselect() # The checkbox would have been checked by default and it will show blank results
c.pack()

my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()