import numpy as np 
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import csv
import matplotlib.pyplot as plt
from pylab import bone,pcolor,colorbar,plot,show
from  minisom  import  MiniSom    

banda=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]


#open('seismic-bumps.csv') as File:
with open('seismic-bumps.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        a=row[3:17]
        lista = list(map(int, a))
        banda.append(lista)



bandas = [x for x in banda if x != []]

scaler = MinMaxScaler()
bandas = scaler.fit_transform(bandas)

k=[5,7,9,11,13]

for re in range(30):
    print("corrida = " + str(re+1))

    desviacion=[]
    for d in range(5):
        print("k = "+ str(k[d]))
        som_shape = (1, k[d])
        som  =  MiniSom ( 1 , k[d] , 14 , sigma = 0.5 , learning_rate = 0.5)
        som.random_weights_init(bandas)
        som.train_batch(bandas,200)
        winner_coordinates = np.array([som.winner(x) for x in bandas]).T
        cluster_index = np.ravel_multi_index(winner_coordinates, som_shape)
    
        mapaaa=som.win_map(bandas)
    
        peso=som.get_weights()

        cero=[]
        uno=[]
        dos=[]
        tres=[]
        cuatro=[]
        cinco=[]
        seis=[]
        siete=[]
        ocho=[]
        nueve=[]
        diez=[]
        once=[]
        doce=[]
        trece=[]


        nomb={0:cero,1:uno,2:dos,3:tres,4:cuatro,5:cinco,6:seis,7:siete,8:ocho,9:nueve,10:diez,11:once,12:doce,13:trece}

        for y in range(k[d]):
            nomb[y]=np.array(mapaaa[(0,y)])


        distan=0
        eucledian=0
        

        for c in range(k[d]):
            if re==0:
                print("cluster = " + str(c) + "=" + str(nomb[c].shape[0]))
            for x in range(nomb[c].shape[0]):
                distan=np.sqrt(np.sum((nomb[c][x]-peso[0][c])**2))
                eucledian=eucledian+distan
    
        desviacion.append(eucledian)
        print("distancia")
        print(eucledian)


        for c in np.unique(cluster_index):
            plt.scatter(bandas[cluster_index == c, 0],
                    bandas[cluster_index == c, 1], label='cluster='+str(c+1), alpha=.7)

    


        for centroid in som.get_weights():
            plt.scatter(centroid[:, 0], centroid[:, 1], marker='x', 
                    s=100, linewidths=35, color='black', label='centroid')
                
        plt.legend()
        #show()
    if re==0:
        print("")
    
    des=np.std([desviacion[0],desviacion[1],desviacion[2],desviacion[3],desviacion[4]])
    print("Desviación estándar = "+ str(des))
    print("")
