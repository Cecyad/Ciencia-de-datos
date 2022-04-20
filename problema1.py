import cv2
import numpy as np
import math

gris = cv2.imread("imagen1.png")
image=cv2.cvtColor(gris,cv2.COLOR_BGR2GRAY)
cv2.imshow('original', image)

# matriz Prewitt
#fila
kernel = np.matrix([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
Prewitt = cv2.filter2D(image,-1,kernel)
#columna
kernel2 = np.matrix([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
Prewitt2=cv2.filter2D(image,-1,kernel2)

Prewitt3=cv2.filter2D(Prewitt,-1,kernel2)


#cv2.imshow('Prewitt_fila', Prewitt)
#cv2.imshow('Prewitt_columna', Prewitt2)
#cv2.imshow('Prewitt_ambas', Prewitt3)


#matriz Sobel 
#fila
kernels = np.matrix([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Sobel = cv2.filter2D(image,-1,kernels)
#columna
kernels2 = np.matrix([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
Sobel2=cv2.filter2D(image,-1,kernels2)

Sobel3=cv2.filter2D(Sobel,-1,kernels2)

#cv2.imshow('Sobel_fila', Sobel)
#cv2.imshow('Sobel2_columna', Sobel2)
#cv2.imshow('Sobel3_ambas', Sobel3)



#matriz Frei-Chen
#fila
kernelf = np.matrix([[-1, 0,1], [-math.sqrt(2), 0, math.sqrt(2)], [-1, 0, 1]])
Frei = cv2.filter2D(image,-1,kernelf)
#columna
kernelf2 = np.matrix([[-1, -math.sqrt(2),-1], [0, 0, 0], [1, math.sqrt(2), 1]])
Frei2=cv2.filter2D(image,-1,kernelf2)

Frei3=cv2.filter2D(Frei,-1,kernelf2)

cv2.imshow('Frei_fila', Frei)
cv2.imshow('Frei2_columna', Frei2)
cv2.imshow('Frei3_ambas', Frei3)


cv2.waitKey(0)
cv2.destroyAllWindows()
