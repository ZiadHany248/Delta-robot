





import cv2
import numpy as np

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)



# function finds and returns contours drawn
#still needs centralizing and bounding rectangles
def conts(image):
    image_ = image.copy()
    image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
    image_ = cv2.GaussianBlur(image_,(7,7),1)
    image_ = cv2.Canny(image_,160,160)
    image_ = cv2.dilate(image_,(5,5),iterations=2)
    contours, heirarchy = cv2.findContours(image_,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:

        area = cv2.contourArea(cnt,False)
        if area > 10:
            cv2.drawContours(image,cnt,-1,(255,255,0),3)
            
        #peri = 2
        #x,y,w,h = cv2.approxPolyDP(cnt,0.02*peri)
        
    return image

def empty(a):
    pass
def masking(image):
    
    image_ = image.copy()
    image_hsv = cv2.cvtColor(image_, cv2.COLOR_BGR2HSV)
    """
    cv2.namedWindow('tracking')
    cv2.createTrackbar('h_min','tracking',0,179,empty)
    cv2.createTrackbar('h_max','tracking',179,179,empty)
    cv2.createTrackbar('sat_min','tracking',0,255,empty)
    cv2.createTrackbar('sat_max','tracking',255,255,empty)
    cv2.createTrackbar('val_min','tracking',0,255,empty)
    cv2.createTrackbar('val_max','tracking',255,255,empty)
    h_min = cv2.getTrackbarPos('h_min','tracking')
    h_max = cv2.getTrackbarPos('h_max','tracking')
    sat_min = cv2.getTrackbarPos('sat_min','tracking')
    sat_max = cv2.getTrackbarPos('sat_max','tracking')
    val_min = cv2.getTrackbarPos('val_min','tracking')
    val_max = cv2.getTrackbarPos('val_max','tracking')
    """
    min_array = np.array([79,120,120])
    max_array = np.array([179,255,255])
    mask = cv2.inRange(image_hsv,min_array,max_array)
    image = cv2.bitwise_and(image,image, mask = mask)
    return image

while 1:
    success, img = cap.read()
    #cont_img = conts(img)
    masking_part = masking(img)
    #cv2.imshow('window',img)
    #cv2.imshow('win2',cont_img)
    cv2.imshow('win3',masking_part)

    cv2.waitKey(1)
