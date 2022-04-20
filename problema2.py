import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

img = cv2.imread('imagen.jpeg')
hist=cv2.calcHist([img],[0],None,[256],[0,256])
hist[0]=0

data=img.ravel()
data=data[data != 0]
data=data[data != 1]

gmm=GaussianMixture(n_components = 6)
gmm=gmm.fit(X=np.expand_dims(data,1))

threshold = np.mean(gmm.means_)
binary_img = img > threshold

gmm_x=np.linspace(0,253,256)
gmm_y=np.exp(gmm.score_samples(gmm_x.reshape(-1,1)))

fig, ax = plt.subplots()
ax.hist(img.ravel(),255,[2,256], normed=True)
ax.plot(gmm_x, gmm_y, color="crimson", lw=4, label="GMM")

ax.set_ylabel("Frequency")
ax.set_xlabel("Pixel Intensity")

plt.legend()
plt.show()



