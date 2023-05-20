from keras.models import load_model
from tkinter import *
import tkinter as tk
from PIL import ImageGrab, Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.datasets import mnist

model = load_model('mnist.h5')

(x_train, y_train), (x_test, y_test) = mnist.load_data()


img = Image.open("3.png")
# изменение рзмера изобржений на 28x28
# img = img.resize((28, 28))
np_img = np.array(img)
# img.save("7res.png")
image_index = 555
plt.imshow(x_test[image_index].reshape(28, 28),cmap='Greys')
plt.show()
# pred = model.predict(x_test[image_index].reshape(1, 28, 28, 1))
pred = model.predict(np_img.reshape(1, 28, 28, 1))
print(type(x_test[image_index]))
print(pred.argmax())
# # конвертируем rgb в grayscale
img = img.convert('L')
img = np.array(img)
# изменение размерности для поддержки модели ввода и нормализации
img = img.reshape(1, 28, 28, 1)
img = img / 255.0
# img.save("7res.png")

# предстказание цифры
res = model.predict(img)
print(res.argmax(), max(res))

