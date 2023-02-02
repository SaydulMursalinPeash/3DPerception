import matplotlib.pyplot as plt
import matplotlib.image as img
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from time import time


img1_loc='1.png'
img2_loc='6.png'
depth_map=img.imread(img2_loc)
image=img.imread(img1_loc)
start_time=time()
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
rows,cols=depth_map[:,:,1].shape
max_vel=depth_map[:,:,1].max()
print(rows,cols)
pixel_cut=3
count=0
for x in range(cols):
    for y in range(rows):
        if(x%pixel_cut==0 and y% pixel_cut==0):
            count+=1
            
            depth=depth_map[y,x,1]
            if depth==0:
                depth=max_vel
            ax.scatter(y,depth,x,marker='.')

elevation=30
azimuth=0
ax.view_init(elevation,azimuth)

plt.show()