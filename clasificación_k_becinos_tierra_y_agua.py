import numpy as np # matriz
import pandas as pd
from statistics import mode
from scipy.spatial import distance
import scipy as sc   # expande lo de numpy, tratamiento de imagenes
import matplotlib.pyplot as plt  # visualizacion grafica
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
dato=np.loadtxt('rsTrain.dat')
import cv2
from scipy import stats as s



with open('rsTrain.dat','r') as f:
    next(f)
    df=pd.DataFrame(l.rstrip().split() for l in f)

x=np.array(df)
xil=np.array(x[:,:4])
yil=np.array(x[:,4])

otro=np.array(dato[1:,4])




X_train, X_test, y_train, y_test = train_test_split(xil,otro, test_size=0.25)




sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


algoritmo = KNeighborsClassifier(n_neighbors = 150, metric = 'minkowski', p = 2)

algoritmo.fit(X_train,y_train)

y_pred = algoritmo.predict(X_test)


matriz = confusion_matrix(y_test, y_pred)
print('Matriz de Confusión:')
print(matriz)


precision = precision_score(y_test, y_pred)
print('Precisión del modelo:')
print(precision)



#abrir las band

banda=[[],[],[],[]]

tup={0:"band1.irs",1:"band2.irs",2:"band3.irs",3:"band4.irs"}


for i in range(4):
    file=open(tup[i],"rb")
    while True:
        caracter=file.read(1)
        if not caracter:
            break
        temporal=np.uint8(int.from_bytes(caracter,byteorder='big'))
        banda[i].append(temporal)
    file.close()
bandas=np.array(banda).T



vector=[]

x = xil[0].astype(np.float)


img1 = np.zeros((512,512),np.uint8)
c=0
f=0
#262144

resultado={0:"imagen1",1:"imagen2",2:"imagen3",3:"imagen4"}
guardar={0:"imagen1.jpg",1:"imagen2.jpg",2:"imagen3.jpg",3:"imagen4.jpg"}
knn=3

for p in range(4):
    for i in range(262144):
        for j in range(200):
            distancia=distance.euclidean(bandas[i],xil[j].astype(np.float))
            vector.append((distancia, otro[j]))
        k=np.array(sorted(vector))
        kn=np.array(k[:knn,1])
        res=int(s.mode(kn)[0])
        if res > 0:
            img1[c][f] = 255
            f=f+1
        else:
            img1[c][f] =0
            f=f+1
        if f==512:
            c=c+1
            f=0
        for j in range(200):
            vector.pop(0)

    cv2.imshow(resultado[p], img1)
    cv2.imwrite(guardar[p], img1)
    cv2.waitKey(8000)
    img1 = np.zeros((512,512),np.uint8)
    if knn==100:
        knn=150
    if knn==7:
        knn=100
    if knn==3:
        knn=7
    c=0
    f=0













