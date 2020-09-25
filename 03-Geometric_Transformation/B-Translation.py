import cv2
import numpy as np

# Untuk persamaan Translation cek di https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

img = cv2.imread("messi5.jpg", 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])  # 100 adalah sumbu x, 50 adalah sumbu y
dst = cv2.warpAffine(img, M, (cols, rows))

print(M)

cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()