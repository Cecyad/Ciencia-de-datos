import cv2
import numpy as np
image = cv2.imread("ojo.jpeg")

kernel = np.matrix([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel2 = np.matrix([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

blur = cv2.filter2D(image,-1,kernel)

b=cv2.filter2D(image,-1,kernel2)


blur2=cv2.filter2D(blur,-1,kernel2)
cv2.imshow('imagen', blur)
cv2.imshow('imagen', b)
cv2.imshow('imagen', blur2)
cv2.waitKey(0)
cv2.destroyAllWindows()
