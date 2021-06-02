from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File open")

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="D:\Projects\Tkinter", title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_img).pack()

my_btn = Button(root, text="Open File", command=open).pack()

# btn = Button(root, text="Click to Close", command=root.exit).pack()

root.mainloop()