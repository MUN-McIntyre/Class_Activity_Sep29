import os
import cv2
import math
import numpy as np

image = cv2.imread("notes.png", cv2.IMREAD_GRAYSCALE)
height, width = image.shape[0], image.shape[1]
for x in range (width):
  for y in range (height):
    if image [y][x] != 0 or image [y][x] != 255:
      image [y][x] = 255
    
