import os
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("notes.png", cv2.IMREAD_GRAYSCALE)
height, width = image.shape[0], image.shape[1]
grey = list()
for i in range(140, 255):
  grey.append(i)
for x in range (width):
  for y in range (height):
    if image [y][x] in grey:
      image [y][x] = 255
    
plt.hist(image.ravel(),256,[0,256])
plt.show()

new_image = cv2.imwrite("new_notes.png", image)
