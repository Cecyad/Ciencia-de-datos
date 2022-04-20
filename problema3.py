import cv2
import numpy as np

gris = cv2.imread("imagen3.jpg")
image=cv2.cvtColor(gris,cv2.COLOR_BGR2GRAY)

#filtro laplacian  
lap=cv2.Laplacian(image,cv2.CV_8U)

#filtro sobel
sob=cv2.Sobel(image,cv2.CV_8U,0,1)


cv2.imshow('Original', image)
cv2.imshow('Sobel', sob)
cv2.imshow('Laplaciano', lap)


cv2.waitKey(0)
cv2.destroyAllWindows()




