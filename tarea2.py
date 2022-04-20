#Desarrolle un programa que usando la imagen de lena.jpg a color, generé una imagen
#en donde cada posición valor_imagen(x,y) es la medía de las posiciones adyacente al
#punto (norte, sur, este y oeste), mostrar la imagen generada.


import cv2
image = cv2.imread("lena.jpg")
alto,ancho=image.shape[0:2]
for i in range(alto):
    for j in range(ancho):
        if(i==0 or i==511):
            #elementos de la primera fila y ultima fila de la matriz, sin contar las ezquinas.
            if(j>0 and j<511):
                if(i==0):
                    b,g,r=image[i,j-1]
                else:
                    b,g,r=image[i,j-1]
                if(i==0):
                    bb,gg,rr=image[i+1,j]
                else:
                    bb,gg,rr=image[i-1,j]
                if(i==0):
                    bbb,ggg,rrr=image[i,j+1]
                else:
                    bbb,ggg,rrr=image[i,j+1]
                c1=(int(b)+int(bb)+int(bbb))//3
                c2=(int(g)+int(gg)+int(ggg))//3
                c3=(int(r)+int(rr)+int(rrr))//3
                image.itemset((i,j,0),c1)
                image.itemset((i,j,1),c2)
                image.itemset((i,j,2),c3)
                d,q,t=image[i, j]
        #Elementos que cuentan con 4 elementos adyacentes a el.
        if(i>0 and i<511):
            if(j>0 and j<511):
                b,g,r=image[i,j-1]
                bb,gg,rr=image[i-1,j]
                bbb,ggg,rrr=image[i,j+1]
                bbbb,gggg,rrrr=image[i+1,j]
                c1=(int(b)+int(bb)+int(bbb)+int(bbbb))//4
                c2=(int(g)+int(gg)+int(ggg)+int(gggg))//4
                c3=(int(r)+int(rr)+int(rrr)+int(rrrr))//4
                image.itemset((i,j,0),c1)
                image.itemset((i,j,1),c2)
                image.itemset((i,j,2),c3)
                d,q,t=image[i, j]
        #elementos de la primera columna y de la ultima columna de la matriz, contando ezquinas.
        if(j==0 or j==511):
            if(i==0):
                if(j==0):
                    b,g,r=image[i, j+1]
                else:
                    b,g,r=image[i, j-1]
                if(j==0):
                    bb,gg,rr=image[i+1, j]
                else:
                    bb,gg,rr=image[i+1, j]
                c1=(int(b)+int(bb))//2
                c2=(int(g)+int(gg))//2
                c3=(int(r)+int(rr))//2
                image.itemset((i,j,0),c1)
                image.itemset((i,j,1),c2)
                image.itemset((i,j,2),c3)
                d,q,t=image[i, j]
            if(i==511):
                if(j==0):
                    b,g,r=image[i, j+1]
                else:
                    b,g,r=image[i, j-1]
                if(j==0):
                    bb,gg,rr=image[i-1, j]
                else:
                    bb,gg,rr=image[i-1, j]
                c1=(int(b)+int(bb))//2
                c2=(int(g)+int(gg))//2
                c3=(int(r)+int(rr))//2
                image.itemset((i,j,0),c1)
                image.itemset((i,j,1),c2)
                image.itemset((i,j,2),c3)
                d,q,t=image[i, j]
            
            if(i!=0 and i!=511):
                if(j==0):
                    b,g,r=image[i-1, j]
                else:
                    b,g,r=image[i-1, j]
                if(j==0):
                    bb,gg,rr=image[i, j+1]
                else:
                    bb,gg,rr=image[i, j-1]
                if(j==0):
                    bbb,ggg,rrr=image[i+1, j]
                else:
                    bbb,ggg,rrr=image[i+1, j]
                c1=(int(b)+int(bb)+int(bbb))//3
                c2=(int(g)+int(gg)+int(ggg))//3
                c3=(int(r)+int(rr)+int(rrr))//3
                image.itemset((i,j,0),c1)
                image.itemset((i,j,1),c2)
                image.itemset((i,j,2),c3)
                d,q,t=image[i, j]
        
cv2.imshow('Modificada', image)
cv2.waitKey(0)

