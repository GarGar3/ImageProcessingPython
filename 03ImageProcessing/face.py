import glob
import cv2
import os
import ctypes
import sys

from PIL import Image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


print(os.getcwd())

dir1 = str(os.getcwd()) + '\Images\*.JPG'
xleft = 0
xtop = 0
xright = 4000
xbot = 4000
print(dir1)
for i in glob.glob(dir1):
    print(dir1)
    img = Image.open(i)
    w ,h = img.size
  
    left = (w/4)- (w/8)
    right = left + 4100
    area = (left,0,right,h)
    cropped_img = img.crop(area)
    cropped_img.save(i)
    cropped_img.close()
    img.close()

    
    
for i in glob.glob(dir1):

    img = cv2.imread(i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        left = 0
        right = 0
        top = 0
        bot = 0
        left = x - ((w/2.2))
        right = x + w + ((w/2.2))
        bot = y + h + ((w/2.2))
        top = y - ((w/2.2))
        print( i + ',' + str(w) + ',x:' + str(x) + ', y:' + str(y) )
        if top < 0:
            top = 0
        if  (right-left) > 750 and x < 2500 and y < 2000:
            print( i + ',' + str(w) + ',x:' + str(x) + ', y:' + str(y) )
            
            break
        if x > 2500 and y < 2000:
            continue
        if y < 2000:
            continue
        if x < 300:
            continue
        left = xleft
        right = xright
        bot = xbot
        top = xtop
        
 
    area = (left,top,right,bot)
    xleft = left
    xtop = top
    xright = right
    xbot = bot
    img = Image.open(i)
    cropped_img = img.crop(area)
    cropped_img.save(i)

ctypes.windll.user32.MessageBoxW(0, "Done", "Image Processing", 0)
sys.exit()

    
    
