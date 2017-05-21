import numpy as np
import cv2
import os

#imgRows i imgColumns - original image dimensions
#xDimLo i yDimLo su current pixel position
def getNextAllowedPosition( imgRows, imgColumns, xDimLo, yDimLo, shift, subwindowSize ):
    xDimLo = xDimLo + shift;
    if xDimLo + subwindowSize < imgColumns :
        return xDimLo, yDimLo
    xDimLo = 0
    yDimLo = yDimLo + shift
    if yDimLo + subwindowSize < imgRows :
        return xDimLo, yDimLo
    else :
        return -1, -1
    
def clipAndSave( img, subwindowSize, shift, fileName, fileDest, extension ):
    xDimLo = yDimLo = 0
    shape = img.shape
    imgRows = shape[0]
    imgColumns = shape[1]
    
    while True:
        xDimLo, yDimLo = getNextAllowedPosition( imgRows, imgColumns, xDimLo, yDimLo, shift, subwindowSize)
        if xDimLo >= 0 :
            fileName = fileName + 1
            clip = img[yDimLo:yDimLo + subwindowSize, xDimLo:xDimLo + subwindowSize]
            string = fileDest + str(fileName) + extension
            cv2.imwrite(string, clip)
        else :
            break;
    return fileName

#PROGRAM "MAIN"
filenameReal = 0    #output file names


realPath = 'set path to real images directory'
realDest = 'set path to cropped images directory'
for i in range(0, 144) : #write number of images

    realImg = cv2.imread(realPath + str(i) + '.jpg', 1)

    filenameReal = clipAndSave( realImg, 65, 200, filenameReal, realDest, '.jpg')

