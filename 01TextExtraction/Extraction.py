import cv2
import numpy as np
import pytesseract
import glob
import os
import ctypes
import sys

dir1 = str(os.getcwd()) + '\Images\*.JPG'

q = 0
for i in glob.glob(dir1):
    q = q + 1
    img = cv2.imread(i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh, image_black = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) 
    cv2.imwrite(i,image_black)
    d = pytesseract.image_to_string(image_black)
    
    with open(i + '.txt', 'w') as f:
        f.write(d)


ctypes.windll.user32.MessageBoxW(0, "Done", "Extracting Text", 0)
sys.exit()
