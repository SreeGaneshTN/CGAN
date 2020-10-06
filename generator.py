import numpy as np
import random
from PIL import Image
sample_size=10

path='/.../CGAN/data/vertical'

for k in range(sample_size):
    arr=np.array((8,8),dtype=float)
    for i in range(8):
        for j in range(8):
            if i <=4:
                arr[i,j]=random.randrange(0,128)
            else:
                arr[i,j]=256
    im=Image.fromarray(arr)
    im.save(path+'Vertical_'+str(k),format='jpeg')


            
