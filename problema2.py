import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("imagen2.jpg")
gris=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#convierte la imagen a un arreglo
x=np.array(gris)
#tam de la imagen
c,d=gris.shape


#pixel = numero pixel
#hist=histograma; las veces que se repite cada pixel
hist, pixel = np.histogram (image.flatten (), 256, [0,256])


#acomulativo de los valores del histograma
cdf = hist.cumsum ()

#es una suma acumulativa es decir hay 3 pixeles de 106
#print(cdf_m[106])


# valor minimo y maximo de la matriz cdf
maximo=cdf.max()
minimo=cdf[cdf>0].min()


#Ajustando contraste y brillo
r=(cdf[x]*255)-minimo
i= r / (maximo - minimo)
t = i.astype(np.uint8)




#ajustando contraste y brillo, utilizando cv2
nueva=cv2.equalizeHist(gris)
#nu=np.array(nueva)


#ajustando contraste y brillo con s=alfa * pixel + beta
alfa= 1.1
beta=2
s=(alfa*x) + beta 
ajuste = s.astype(np.uint8)




cv2.imshow('original', gris)
cv2.imshow('funcion', nueva)
cv2.imshow('ajuste', t)
cv2.imshow('Ajuste2', ajuste)

cv2.waitKey(0)
cv2.destroyAllWindows()