import math
from pystdlib import stddraw as sd
DIM = 30

sd.setXscale(-DIM,DIM)
sd.setYscale(-DIM,DIM)

xx = [0]
yy = [0]

POINTS = 2000
dalpha = 6*math.pi / POINTS

for i in range(1, POINTS):
    xx.append(i*dalpha*math.cos(i*dalpha))
    yy.append(i*dalpha*math.sin(i*dalpha))
    sd.line(xx[i - 1], yy[i - 1], xx[i], yy[i])


sd.show()