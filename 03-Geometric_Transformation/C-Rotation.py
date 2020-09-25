import cv2
import numpy as np

# Untuk persamaan Rotation cek di https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

img = cv2.imread("messi5.jpg", 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

print(M)

cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()