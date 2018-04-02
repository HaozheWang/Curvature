import numpy as np
import argparse
import matplotlib.pyplot as plt


'''
curve C(p) = (x(p), y(p));
curvature K = (x'y''-x''y')/(x'^2+y'^2)^(3/2)
'''

parser = argparse.ArgumentParser(description="calculate curvature at each point for contour C")
parser.add_argument('-f',type=str, dest="file", required=True, help="input matrix containing x- and y- coordinates")
args = parser.parse_args()

a = np.loadtxt(args.file)
x = a[:, 0]
y = a[:, 1]
dx = np.gradient(x)   #x'
dy = np.gradient(y)   #y'

d2x = np.gradient(dx)    #x''
d2y = np.gradient(dy)    #y''

curvature = (dx * d2y - d2x * dy) / (dx * dx + dy * dy)**1.5
print (curvature)
plt.scatter(a[:,0], a[:,1])
