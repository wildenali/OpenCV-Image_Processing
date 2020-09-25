import cv2
import numpy as np

img = cv2.imread("opencv_logo.png")

# 1. Erosion
kernel = np.ones((5, 5), np.uint8)
erison = cv2.erode(img, kernel, iterations=1)

# 2. Dilataion
dilation = cv2.dilate(img, kernel, iterations=1)

# 3. Opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 4. Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 5. Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 6. Top Hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 7. Black Hat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", img)
cv2.imshow("Erison", erison)
cv2.imshow("Dilataion", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradient", gradient)
cv2.imshow("Top Hat", tophat)
cv2.imshow("Black Hat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
