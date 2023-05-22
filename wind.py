import math
from tkinter import *
from tkinter import ttk
from PIL import ImageGrab, Image, ImageOps
from load import recognize
clicks = 0


def click_button():
    # изменяем текст на кнопке
    # print(root.winfo_x(), root.winfo_y())
    x,y=root.winfo_x(), root.winfo_y()
    im2 = ImageGrab.grab(bbox =(x, y+80, x+280, y+305))
    # im2.show()

    rec=recognize(im2)
    # im2.show()
    label.config(text="Распознана цифра "+str(rec))
    canvas.delete("all")

def reset_button():
    canvas.delete("all")
def update():
    x, y = root.winfo_x(), root.winfo_y()
    im2 = ImageGrab.grab(bbox=(x, y + 80, x + 280, y + 305))

    rec = recognize(im2)
    # im2.show()
    label.config(text="Распознана цифра "+rec)
    label.after(1000,update)


def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy

    # if (math.sqrt((lasx-event.x)**2+(lasy-event.y)**2))>2:
    canvas.create_line((lasx, lasy, event.x, event.y),
                      fill='black',
                      width=8)
    if (math.sqrt((lasx - event.x) ** 2 + (lasy - event.y) ** 2)) <= 6:
        canvas.create_arc((lasx, lasy, event.x, event.y),
                          fill='black',
                          width=8)
    lasx, lasy = event.x, event.y


root = Tk()
root.title("Tsybrov LR3")
root.geometry("280x280")

label = Label(root,
                 text = "")
label.pack(side=TOP)

button_frame= Frame(root)
button_frame.pack(side=TOP)

btn = ttk.Button(button_frame,text="Распознать", command=click_button)
res= ttk.Button(button_frame,text="Очистить", command=reset_button)

btn.pack(side=LEFT)
res.pack(side=LEFT)

canvas = Canvas(root, bg='white')
canvas.pack(anchor='nw', fill='both', expand=1)
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

root.mainloop()