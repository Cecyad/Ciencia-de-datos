#Utilizando el ejercicio anterior, desarrolle un programa que decodifique la
#imagen_codificada.jpg a la imagen original.


import cv2
image = cv2.imread("imagen_codificada.jpg")
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
        c1=int(b)- int(rest)
        if(c1<0):
            c1=c1*-1
            c1=255-c1
        image.itemset((i,j,0),c1)
        image.itemset((i,j,1),c1)
        image.itemset((i,j,2),c1)

cv2.imshow('gris', image)
cv2.imwrite('imagen_codificada.jpg', image)
cv2.waitKey(8000)
