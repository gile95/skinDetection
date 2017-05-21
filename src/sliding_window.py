import numpy as np
import cv2
import time

imgPath = 'set path'

shift = 10
startingSize = 50
finalSize = 70
increment = 10

def getNextPosition( img, currentX, currentY, size ):
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

def slide( img, currentX, currentY, size ):
    imgX = img.shape[1]
    imgY = img.shape[0]
    currentX, currentY = 0, 0

    while True:
        
        clone = img.copy()
        cv2.rectangle(clone, (currentX, currentY), (currentX + size, currentY + size), (0, 255, 0), 2)
        cv2.imshow('Window', clone)
        cv2.waitKey(1)
        time.sleep(0.025)
        #cv2.destroyAllWindows()
        
        currentX, currentY, size = getNextPosition(img, currentX, currentY, size)
        if currentX < 0:
            break
        

img = cv2.imread(imgPath, 1)
currentX = 0
currentY = 0
size = startingSize

slide(img, currentX, currentY, size)

