import os
import cv2
import math
import numpy as np

image = cv2.imread("notes.png", cv2.IMREAD_GRAYSCALE)
height, width = image.shape[0], image.shape[1]
white = list()
for i in range(180, 255):
  white.append(i)
black = list()
for i in range(-1, 100):
  black.append(i)  
for x in range (width):
  for y in range (height):
    if image [y][x] not in white and image [y][x] not in black:
      image [y][x] = 255
    
new_image = cv2.imwrite("new_notes.png", image)
