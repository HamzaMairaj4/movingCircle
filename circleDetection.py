#import libraries
import cv2 as cv
import numpy as np

#define function with image as only parameter
def circleDetection(img):
   #convert image to grayscale
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

   #blur grayscale image
    gauss = cv.GaussianBlur(grey,(11,11),0)

   #Blur twice for good luck

   #Use HoughCircles transform to detect circular objects
    circles = cv.HoughCircles(gauss,cv.HOUGH_GRADIENT,1,41,param1=100,param2=65,minRadius=130,maxRadius=0)


   #Convert circles to integers
    try:
        circles = np.uint16(np.around(circles))

       #Draw detected circles
        for i in circles[0,:]:
            #Draw outer circle
            cv.circle(img,(i[0],i[1]),i[2],(34,255,0),7)

            #Draw midpoint
            cv.circle(img, (i[0], i[1]), 2, (0, 255, 0), 3)
    except:
        return img

   #show frame and wait for break
    return img
