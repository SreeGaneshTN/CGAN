import numpy as np
import random
import matplotlib.pyplot as plt
sample_size=100
import os

path1='/home/sreegs/Documents/CGAN/data/vertical/'
path2='/home/sreegs/Documents/CGAN/data/horizontal/'

for k in range(sample_size):
    arr=np.zeros((8,8),dtype=float)
    for i in range(8):
        for j in range(8):
            if j < 4:
                arr[i,j]=random.randrange(0,128)
            else:
                arr[i,j]=256
    plt.imshow(arr)
    plt.imsave(path1+'vertical_'+str(k)+'.jpg',arr)

for k in range(sample_size):
    arr=np.zeros((8,8),dtype=float)
    for i in range(8):
        for j in range(8):
            if i < 4:
                arr[i,j]=random.randrange(0,128)
            else:
                arr[i,j]=256
    plt.imshow(arr)
    plt.imsave(path2+'horizontal_'+str(k)+'.jpg',arr)
            
