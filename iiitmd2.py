# -*- coding: utf-8 -*-
"""iiitmd2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iljsRh8eiusGRNLmHyg9-JVtojf56_bc
"""

import cv2

cv2.__path__

!cd  /usr/local/lib/python3.6/dist-packages/cv2'

!cd /usr/local/lib/python3.6/dist-packages/cv2

!ls /usr/local/lib/python3.6/dist-packages/cv2/data

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests
import io

image=Image.open(io.BytesIO(requests.get("https://images.pexels.com/photos/1222271/pexels-photo-1222271.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",stream=True).content)).convert("RGB")

plt.imshow(image)

grayimage=cv2.cvtColor(np.asarray(image),cv2.COLOR_RGB2GRAY)

plt.imshow(grayimage,cmap="gray")

detector=cv2.CascadeClassifier("/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_frontalface_default.xml")

faces=detector.detectMultiScale(grayimage,1.3,5)

faces

image=np.asarray(image)

for face in faces:
  x,y,w,h=face
  cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),5)

plt.imshow(image)

