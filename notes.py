import os
import cv2
import math
import numpy as np
from matplotlib import pylot as plt

image = cv2.imread("notes.png", cv2.IMREAD_GRAYSCALE)
height, width = image.shape[0], image.shape[1]
white = list()
for i in range(205, 255):
  white.append(i)
black = list()
for i in range(-1, 40):
  black.append(i)  
for x in range (width):
  for y in range (height):
    if image [y][x] not in white and image [y][x] not in black:
      image [y][x] = 255
    
plt.hist(image.ravel(),256,[0,256])
plt.show()

new_image = cv2.imwrite("new_notes.png", image)
