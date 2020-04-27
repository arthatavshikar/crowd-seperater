from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np
import serial
import time
import struct

arduino = serial.Serial('/dev/ttyACM0', 9600)


while True:
    response = requests.get('http://192.168.1.178:8080/shot.jpg')
    img = Image.open(BytesIO(response.content))
    img = np.asarray(img)
    # Load the cascade
    body_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = body_cascade.detectMultiScale(gray, 1.1, 10)
    # Draw rectangle around the body
    count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count = count+1#see if more than one person is in the picture
    #crop_img = img[y:y-h, x:x-w]
    # Display the output
    print(count)
    count1 = count;
    count = str(count)
    count = str.encode(count)
    arduino.write(count);
    if(count1<2):
        break
        
cv2.imshow('img', img)
#cv2.imshow('cropped', crop_img)
cv2.waitKey()
