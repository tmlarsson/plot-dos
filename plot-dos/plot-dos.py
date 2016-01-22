import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print 'No filename specified...'
    exit()

filename = sys.argv[1]

val = np.loadtxt(filename+'.DOS')

f = open(filename+'.EIG','r')
eig= float(f.readline())

val[:,0] = val[:,0]-eig
xmax = np.ceil(np.ndarray.max(val[:,0]))
xmin = np.floor(np.ndarray.min(val[:,0]))
ymax = np.ceil(np.ndarray.max(val[:,1]))
ymin = np.floor(np.ndarray.min(val[:,1]))

plt.cla()
plt.plot(val[:,0],val[:,1])
plt.xlabel('Energy')
plt.ylabel('Density of states')
plt.title('Density of states for different energies')
plt.axis([xmin, xmax, ymin, ymax])
plt.savefig(filename+'.eps')
