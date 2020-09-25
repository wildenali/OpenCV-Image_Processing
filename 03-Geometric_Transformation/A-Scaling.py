import cv2
import numpy as np

"""
Goal
- cv2.INTER_AREA for shrinking
- cv2.INTER_CUBIC (slow)
- cv2.INTER_LINEAR for zooming.
"""

img = cv2.imread("messi5.jpg")

# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# cv2.imshow("img", res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# or

height, width = img.shape[:2]
res = cv2.resize(img, (3 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("img", res)
cv2.waitKey(0)
cv2.destroyAllWindows()