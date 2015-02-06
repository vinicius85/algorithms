import numpy as np
import numpy.random
import matplotlib.pyplot as plt

x = []
y = []
i = 0
f = open('posts-060215.csv' , 'r')
for line in f:
	splits = line.split('\t')
	weekday = int(splits[4])
	likes = int(splits[5])
	print weekday
	print likes
	x.append(weekday)
	y.append(likes)
	
heatmap, xedges, yedges = np.histogram2d(x, y, bins=[1000,10])
print xedges
print yedges
extent = [0, 6, 0, 1250]

plt.clf()
plt.imshow(heatmap, extent=extent)
plt.show()