from tkinter import *
from PIL  import ImageTk, Image

root = Tk()
root.title('Radio Button')

# r = IntVar()

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

my_button = Button(root, text="Click Me!", command=lambda: clicked(pizza.get())).pack()

root.mainloop()