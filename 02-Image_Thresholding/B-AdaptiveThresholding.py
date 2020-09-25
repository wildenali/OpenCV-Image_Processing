import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Goal
- Bisa adaptif dengan lingkungan yg misalnya low light dan high light
- Example functions: 
    - cv2.ADAPTIVE_THRESH_MEAN_C : nilai threshold adalah nilai rata-rata dari lingkungan sekitar
    - cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
"""

img = cv2.imread("b_adaptive.jpg", 0)
img = cv2.medianBlur(img, 5)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
thresh3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

titles = [
    "Original Image",
    "Global Threshold (v=127)",
    "Adaptive Mean Thresholding",
    "Adaptive Gaussian Thresholding",
]
images = [img, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()