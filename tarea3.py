#Utilizando la imagen de lena.jpg a escalas a grises, Implemente el cifrado por
#desplazamiento, es una técnicas de codificación de textos más simples y usados. Es un
#tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada por
#otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.

import cv2
image = cv2.imread("lenaa.jpeg")
alto,ancho=image.shape[0:2]
num = int(input("Ingrese el desplazamiento: "))
rest=num//255
if(rest>0):
    rest=num%255
else:
    rest=num

for i in range(alto):
    for j in range(ancho):
        b=image[i,j][0:1]
        c1=int(b)+ int(rest)
        if(c1>255):
            c1=c1-255
        image.itemset((i,j,0),c1)
        image.itemset((i,j,1),c1)
        image.itemset((i,j,2),c1)

cv2.imshow('gris', image)
cv2.imwrite('imagen_codificada.jpg', image)
cv2.waitKey(8000)



