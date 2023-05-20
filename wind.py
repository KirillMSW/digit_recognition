from tkinter import *
from tkinter import ttk
from PIL import ImageGrab, Image, ImageOps
from load import recognize
clicks = 0


def click_button():
    global clicks
    clicks += 1
    # изменяем текст на кнопке
    print(root.winfo_x(), root.winfo_y())
    x,y=root.winfo_x(), root.winfo_y()
    im2 = ImageGrab.grab(bbox =(x, y+80, x+280, y+305))

    rec=recognize(im2)
    # im2.show()
    label.config(text=rec)
    canvas.delete("all")


def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y),
                      fill='black',
                      width=8)
    lasx, lasy = event.x, event.y

root = Tk()
root.title("Tsybrov LR3")
root.geometry("280x280")
btn = ttk.Button(text="Распознать", command=click_button)
label = Label(root,
                 text = "")
label.pack()
btn.pack()

canvas = Canvas(root, bg='white')
canvas.pack(anchor='nw', fill='both', expand=1)
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

root.mainloop()