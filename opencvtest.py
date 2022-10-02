# importing packages
import os
import numpy as np
import cv2
from skimage import io 

with open('input.txt') as f:
    url = f.readline()

#load junocam image into numpy array for cv2 processing
img = io.imread(url)

#split and save the r, g, b images
b, g, r = cv2.split(img)

splitr = "red.png"
splitg = "green.png"
splitb = "blue.png"

cv2.imwrite("red.png", r)
cv2.imwrite("green.png", g)
cv2.imwrite("blue.png", b)

#merge images and save to disk
mergedfile = "converted.png"
merged = cv2.merge([r, g, b])
cv2.imwrite("converted.png", merged) 