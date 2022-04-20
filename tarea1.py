#Desarrolle un programa que usando la imagen de lena.jpg a color, cambié la resolución de la imagen disminuyendo el tamaño de la matriz de representación 
#de la imagen de 50% en 50% hasta llegar a 1/4 del tamaño original, mostrar la imágenes generadas.


import cv2
#cargar la imagen
image = cv2.imread("lena.jpg")
#guardar en las variables el alto y ancho
alto,ancho=image.shape[0:2]
print('tamaño original: ',alto,ancho)
#mostrar imagen original
cv2.imshow('Imagen original',image)
alto2=alto//2
ancho2=ancho//2
print('tamaño mitad: ',alto2,ancho2)
#disminuir imagen a 50%
imagenmitad = cv2.resize(image, (512, 128))
cv2.imshow('Imagen a la mitad', imagenmitad)
alto3=alto2//2
ancho3=ancho2//2
print('tamaño cuarto: ',alto3,ancho3)
#disminuir imagen de 50%, es decir a 1/4 de la imagen original
imagencuarto = cv2.resize(image, (alto3, ancho3))
cv2.imshow('imagen a cuarto', imagencuarto)


cv2.waitKey(0)