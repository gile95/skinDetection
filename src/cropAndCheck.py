import numpy as np
import cv2
import os

subwindowSize = 65	#image size dim*dim
numberSource = 78   #num of input images
shift = 5               

filename = 0    #names of output files

realPath = 'set path'
groundTruthPath = 'set path'

dest = '/set path/'

realExtension = '.jpg'
gtExtension = '.png'

skinValue = 255         #value of pixel labeled that skin

def checkIfContainsSkin (imgGt) :
    middlePixelPosition = subwindowSize / 2
    middlePixel = imgGt[middlePixelPosition, middlePixelPosition, 2]
    if middlePixel != skinValue :
        return True
    return False

def getNextAllowedPosition( imgRows, imgColumns, xDimLo, yDimLo):
    xDimLo = xDimLo + shift;
    if xDimLo + subwindowSize < imgColumns :
        return xDimLo, yDimLo
    xDimLo = 0
    yDimLo = yDimLo + subwindowSize
    if yDimLo + subwindowSize < imgRows :
        return xDimLo, yDimLo
    else :
        return -1, -1

def clipAndSave( imgReal, imgGt, fileName, dest):
    xDimLo = yDimLo = 0
    shape = imgReal.shape
    imgRows = shape[0]
    imgColumns = shape[1]
    
    while True:
        xDimLo, yDimLo = getNextAllowedPosition( imgRows, imgColumns, xDimLo, yDimLo)
        if xDimLo >= 0 :
            clipReal = imgReal[yDimLo:yDimLo + subwindowSize, xDimLo:xDimLo + subwindowSize]
            clipGt = imgGt[yDimLo:yDimLo + subwindowSize, xDimLo:xDimLo + subwindowSize]
            if checkIfContainsSkin(clipGt):
                fileName = fileName + 1
                string = dest + str(fileName) + realExtension
                cv2.imwrite(string, clipReal)
                xDimLo = xDimLo + subwindowSize
            
            #fileName = fileName + 1
            #clip = img[yDimLo:yDimLo + subwindowSize, xDimLo:xDimLo + subwindowSize]
            #string = fileDest + str(fileName) + extension
            #cv2.imwrite(string, clip)
            
        else :
            break;
    return fileName

#PROGRAM "MAIN"

for i in range(0, numberSource) : #input number of pictures from the beginning

    realImg = cv2.imread(realPath + str(i) + '.jpg', 1)
    gtImg = cv2.imread(groundTruthPath + str(i) + '.png', 1)

    
    filename = clipAndSave( realImg, gtImg, filename, dest)
