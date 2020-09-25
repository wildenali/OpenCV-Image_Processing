import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Goal
- Belajar Simple Thresholding, Adaptive Thresholding dan Otsu's Thresholding
- Example functions: cv2.threshold(), cv2.adaptiveThreshold() etc
"""

# Contoh yg akan di buat yaitu Object Tracking
"""
OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. Different types are:
- cv2.THRESH_BINARY
- cv2.THRESH_BINARY_INV
- cv2.THRESH_TRUNC
- cv2.THRESH_TOZERO
- cv2.THRESH_TOZERO_INV
- etc
"""

img = cv2.imread("gradient.jpg", 0)
ret, thresh1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

h, w = img.shape
print(img)
print(img.shape)
print("height: ", h)
print("width: ", w)

"""
# Ini untuk menampilkan nilai array dari gambar tersebut
for i in range(h):
    for j in range(h):
        print(img[i][j], end=" ")
    print()
"""

titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


"""
# Coba gambar yg lain
img2 = cv2.imread("gradient2.jpg", 0)
ret, img2Thresh1 = cv2.threshold(img2, 50, 255, cv2.THRESH_BINARY)
ret, img2Thresh2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY_INV)
ret, img2Thresh3 = cv2.threshold(img2, 127, 255, cv2.THRESH_TRUNC)
ret, img2Thresh4 = cv2.threshold(img2, 127, 255, cv2.THRESH_TOZERO)
ret, img2Thresh5 = cv2.threshold(img2, 127, 255, cv2.THRESH_TOZERO_INV)


h2, w2 = img2.shape
print(img2)
print(img2.shape)
print("height: ", h2)
print("width: ", w2)


images2 = [img2, img2Thresh1, img2Thresh2, img2Thresh3, img2Thresh4, img2Thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images2[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
"""