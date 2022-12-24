



import cv2
import numpy
import serial
import time
import utils
cap = cv2.VideoCapture(1)

while 1:
    _, img = cap.read()