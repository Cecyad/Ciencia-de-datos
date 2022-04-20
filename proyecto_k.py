import numpy as np 
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import csv
import matplotlib.pyplot as plt

banda=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

mean_dis=[]
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sum7=0
sum8=0
sum9=0
sum10=0
sum11=0
sum12=0
sum13=0

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

for i in range(30):
    print("corrida = " + str(i+1))
    Kmedia5= KMeans(n_clusters=5).fit(bandas)
    Kmedia7= KMeans(n_clusters=7).fit(bandas)
    Kmedia9= KMeans(n_clusters=9).fit(bandas)
    Kmedia11= KMeans(n_clusters=11).fit(bandas)
    Kmedia13= KMeans(n_clusters=13).fit(bandas)

    k={0:Kmedia5,1:Kmedia7,2:Kmedia9,3:Kmedia11,4:Kmedia13}


    print("Distancia")
    print("k=5")
    print(k[0].inertia_)
    print("k=7")
    print(k[1].inertia_)
    print("k=9")
    print(k[2].inertia_)
    print("k=11")
    print(k[3].inertia_)
    print("k=13")
    print(k[4].inertia_)
    des=np.std([k[0].inertia_,k[1].inertia_,k[2].inertia_,k[3].inertia_,k[4].inertia_])
    print("Desviación estándar = "+ str(des))
    print("")

    #sum1=sum1+k[0].inertia_
    #sum2=sum2+k[1].inertia_
    #sum3=sum3+k[2].inertia_
    #sum4=sum4+k[3].inertia_
    #sum5=sum5+k[4].inertia_
    if i==1:
        for p in range(5):
            for i, l in enumerate(k[p].labels_):
                if l == 0:
                    sum1=sum1+1
                if l==1:
                    sum2=sum2+1
                if l==2:
                    sum3=sum3+1
                if l==3:
                    sum4=sum4+1
                if l==4:
                    sum5=sum5+1
                if l==5:
                    sum6=sum6+1
                if l == 6:
                    sum7=sum7+1
                if l==7:
                    sum8=sum8+1
                if l==8:
                    sum9=sum9+1
                if l==9:
                    sum10=sum10+1
                if l==10:
                    sum11=sum11+1
                if l==11:
                    sum12=sum12+1
                if l==12:
                    sum13=sum13+1
                
            if p==0:
                print("k=5 ")
                print("cluster 1: " + str(sum1))
                print("cluster 2: " + str(sum2))
                print("cluster 3: " + str(sum3))
                print("cluster 4: " + str(sum4))
                print("cluster 5: " + str(sum5))
            if p==1:
                print("k=7 ")
                print("cluster 1: " + str(sum1))
                print("cluster 2: " + str(sum2))
                print("cluster 3: " + str(sum3))
                print("cluster 4: " + str(sum4))
                print("cluster 5: " + str(sum5))
                print("cluster 6: " + str(sum6))
                print("cluster 7: " + str(sum7))
            if p==2:
                print("k=9 ")
                print("cluster 1: " + str(sum1))
                print("cluster 2: " + str(sum2))
                print("cluster 3: " + str(sum3))
                print("cluster 4: " + str(sum4))
                print("cluster 5: " + str(sum5))
                print("cluster 6: " + str(sum6))
                print("cluster 7: " + str(sum7))
                print("cluster 8: " + str(sum8))
                print("cluster 9: " + str(sum9))
            if p==3:
                print("k=11 ")
                print("cluster 1: " + str(sum1))
                print("cluster 2: " + str(sum2))
                print("cluster 3: " + str(sum3))
                print("cluster 4: " + str(sum4))
                print("cluster 5: " + str(sum5))
                print("cluster 6: " + str(sum6))
                print("cluster 7: " + str(sum7))
                print("cluster 8: " + str(sum8))
                print("cluster 9: " + str(sum9))
                print("cluster 10: " + str(sum10))
                print("cluster 11: " + str(sum11))
            if p==4:
                print("k=13 ")
                print("cluster 1: " + str(sum1))
                print("cluster 2: " + str(sum2))
                print("cluster 3: " + str(sum3))
                print("cluster 4: " + str(sum4))
                print("cluster 5: " + str(sum5))
                print("cluster 6: " + str(sum6))
                print("cluster 7: " + str(sum7))
                print("cluster 8: " + str(sum8))
                print("cluster 9: " + str(sum9))
                print("cluster 10: " + str(sum10))
                print("cluster 11: " + str(sum11))
                print("cluster 12: " + str(sum12))
                print("cluster 13: " + str(sum13))
            sum1=0
            sum2=0
            sum3=0
            sum4=0
            sum5=0
            sum6=0
            sum7=0
            sum8=0
            sum9=0
            sum10=0
            sum11=0
            sum12=0
            sum13=0

            





#mean_dis.append(int(sum1))
#mean_dis.append(int(sum2))
#mean_dis.append(int(sum3))
#mean_dis.append(int(sum4))
#mean_dis.append(int(sum5))

#plt.plot(mean_dis)
#plt.show()






