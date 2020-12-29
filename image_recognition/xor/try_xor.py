import numpy as np
import cv2

# Load an color image in grayscale
img1 = cv2.imread('d.png')
img2 = cv2.imread('e.png')
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.imshow('image',img2)
cv2.waitKey(0)

result = cv2.bitwise_xor(img2,img1)

cv2.imshow('image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()