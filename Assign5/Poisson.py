# platform: python2 MacOS
import math
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

time = numb = 0
landa = 20.0 / 3600 * -1

while 1:
	data = random.random()
	time += math.log(data, 2) / landa
	numb += 1
	if time > 3600:
		break
	test = str(int(time / 3600)).zfill(2) + ':' + str(int((time - int(time / 3600) * 3600) / 60)).zfill(2) + ':' + str(int((time % 60))).zfill(2)
	print numb, '->', test
