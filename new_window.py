from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Base Window')

# If you write this line inside the function it will consider it as local and it wont display
# my_img = ImageTk.PhotoImage(Image.open('images\pic4.jpg'))

def open_window():
    global my_img
    top = Toplevel()
    top.title('New Window')
    my_img = ImageTk.PhotoImage(Image.open('images\pic4.jpg'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text='Open new window', command=lambda: open_window()).pack()

mainloop()
