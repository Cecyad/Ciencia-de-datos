import cv2
import numpy as np

gris = cv2.imread("lena.jpeg")
image=cv2.cvtColor(gris,cv2.COLOR_BGR2GRAY)

kernel1 = np.matrix([[0, -1,0], [-1, 5, -1], [0, -1, 0]])

filtro1 = cv2.filter2D(image,-1,kernel1)

cv2.imshow('Original', image)
cv2.imshow('Filtro_uno', filtro1)


cv2.waitKey(0)
cv2.destroyAllWindows()
