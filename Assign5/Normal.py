# platform: python2 MacOS
import math
import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

datax = np.random.random(10000)
datay = np.random.random(10000)
meanx = np.mean(datax)
meany = np.mean(datay)
strdx = np.std(datax)
strdy = np.std(datay)
newdx = (datax - meanx) / strdx
newdy = (datay - meany) / strdy
graph = np.sqrt(-2 * np.log(datax)) * np.cos(2 * datay * math.pi)

plt.hist(graph, bins = 50, edgecolor = 'k')
plt.title('Standard Normal Distribution')
plt.xlabel('Variable X')
plt.ylabel('Count')
plt.show()
