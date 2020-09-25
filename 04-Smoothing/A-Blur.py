import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("opencv_logo.png")

plt.subplot(121)
plt.imshow(img)
plt.title("Original")
plt.xticks([])
plt.yticks([])

# 1. Blur Averaging
# blur = cv2.blur(img, (5, 5))
# plt.subplot(122)
# plt.imshow(blur)
# plt.title("Blurred")
# plt.xticks([])
# plt.yticks([])
# plt.show()

# 2. Blur Gaussian
# blurGaussian = cv2.GaussianBlur(img, (5, 5), 0)
# plt.subplot(122)
# plt.imshow(blurGaussian)
# plt.title("Blur Gaussian")
# plt.xticks([])
# plt.yticks([])
# plt.show()

# 3. Blur Bilateral
blurBilateral = cv2.bilateralFilter(img, 9, 75, 75)
plt.subplot(122)
plt.imshow(blurBilateral)
plt.title("Blur Bilateral")
plt.xticks([])
plt.yticks([])
plt.show()