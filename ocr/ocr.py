import pytesseract
import cv2
import pyscreenshot as ImageGrab
import numpy as np
cap = cv2.VideoCapture(-1)     
cap.set(3, 640)
cap.set(4, 480)


def CaptureScreen(bbox=(300, 300, 1500, 1000)):      #<--- Use PIL for Windows
    capscr = np.array(ImageGrab.grab(bbox))
    capscr = cv2.cvtColor(capscr , cv2.COLOR_RGB2BGR)
    return capscr


while True:
    timer = cv2.getTickCount()
    _, img = cap.read()
    himg, wimg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    for b in boxes.splitlines():
        b = b.split(' ')
        #print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, himg - y), (w, himg - h), (50, 50, 255), 1)

    cv2.imshow('Result', img)
    cv2.waitKey(1)

cv2.imshow('Image', img)
cv2.waitkey(0)




