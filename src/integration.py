import numpy as np
import cv2
import time
from keras.models import load_model
from Tkinter import Tk
from tkFileDialog import askopenfilename

model_path = './my_model.h5'

model = load_model(model_path)

img_width, img_height = 65, 65

shift = 10
startingSize = 65
finalSize = 65
increment = 1


def getNextPosition(img, currentX, currentY, size):
    currentX = currentX + shift
    if (currentX + size) > img.shape[1]:
        currentX = 0
        currentY = currentY + shift
    if (currentY + size) > img.shape[0]:
        currentX, currentY = 0, 0
        size = size + increment
    if size > finalSize:
        currentX = -1
    return currentX, currentY, size


def slide(img, currentX, currentY, size):
    imgX = img.shape[1]
    imgY = img.shape[0]
    currentX, currentY = 0, 0

    for_drawing = img.copy();

    while True:
        clone = img.copy()

        crop_img = clone[currentY:currentY + size, currentX:currentX + size]
        x = np.array(crop_img)
        x = x.reshape(1, 3, 65, 65)

        output = model.predict(x, batch_size=32, verbose=0)
        if output > 0.5:
            #print output
            cv2.rectangle(for_drawing, (currentX, currentY), (currentX + size, currentY + size), (0, 255, 0), 2)
            cv2.imshow('Window', for_drawing)
            cv2.waitKey(1)

        currentX, currentY, size = getNextPosition(img, currentX, currentY, size)
        if currentX < 0:
            break

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

imgPath = filename

img = cv2.imread(imgPath, 1)
currentX = 0
currentY = 0
size = startingSize

slide(img, currentX, currentY, size)

