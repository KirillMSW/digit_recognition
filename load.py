from keras.models import load_model
from keras.datasets import mnist
from keras.models import load_model
from tkinter import *
import tkinter as tk
from PIL import ImageGrab, Image, ImageOps, ImageFilter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.datasets import mnist

def recognize(img):
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # img = Image.open("7.png")
    model = load_model('mnist2.h5')
    orig = img.copy()
    orig=orig.convert('L')
    orig = np.array(orig)
    # orig = orig.filter(ImageFilter.MedianFilter(3))
    yellowY, yellowX = np.where((orig == 0))
    frame = 20
    top, bottom = yellowY.min()-frame, yellowY.max()+frame
    left, right = yellowX.min()-frame, yellowX.max()+frame
    print(top, bottom, left, right)

    # Extract Region of Interest from unblurred original
    if abs(left-right)<abs(top-bottom):
        diff = round ((abs(top-bottom) - abs(left-right))/2)
        left-=diff
        right+=diff


    ROI = orig[top:bottom, left:right]
    img = Image.fromarray(ROI)
    img = img.resize((28,28))
    # img = x_test[image_index]
    # конвертируем rgb в grayscale
    img = img.convert('L')
    # img.save("7res.png")
    img=ImageOps.invert(img)



    img=img.point(lambda p: 255 if p > 90 else 0)
    # img = img.convert('1')
    # img=ImageOps.invert(img)


    img = np.array(img)




    # Image.fromarray(ROI).save('result.png')
    # plt.imshow(img.reshape(28, 28),cmap='Greys')
    # изменение размерности для поддержки модели ввода и нормализации
    img = img.reshape(1,28,28,1)
    # plt.imshow(img.reshape(28, 28),cmap='Greys')

    img = img/255.0

    # plt.imshow(img.reshape(28, 28),cmap='Greys')
    # plt.show()
    # предстказание цифры
    res = model.predict([img])[0]
    # print(res.argmax(), max(res))
    return res.argmax()