import cv2
import numpy as np

"""
Goal
- Convert images from one color-space to another, like BGR<->Gray, BGR<->HSV etc.
- Example functions: cv2.cvtColor(), cv2/inRange() etc
"""

# Contoh yg akan di buat yaitu Object Tracking
"""
Langkah-langkah Pembuatannya:
1. Ambil setiap frame dari video
2. Convert dari BGR ke HSV
3. Atur rentang threshold HSV untuk warna BIRU misalnya
4. Ekstrak Objek biru 
"""

cap = cv2.VideoCapture(0)

while True:
    # 1. Ambil setiap frame dari video
    _, frame = cap.read()

    # 2. Convert dari BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 3. Atur rentang threshold HSV untuk warna BIRU misalnya
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 4. Ekstrak Objek biru
    # Bitwise AND mask and origina image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('1. Ambil setiap frame dari video', frame)
    cv2.imshow('3. Atur rentang threshold HSV untuk warna BIRU misalnya', mask)
    cv2.imshow('4. Ekstrak Objek biru', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

"""
Langkah-langkah Uji Coba:
1. Run program
2. Ambil benda yg berwarna biru
3. Dekatkan dengan kamera webcam, sehingga dapat terlihat dalam webcam
4. Lihat Hasilnya
"""
