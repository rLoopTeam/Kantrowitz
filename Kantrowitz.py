import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.plotly as py
import plotly.graph_objs as go
vel = np.arange(0, 341, 1) #Creating a velocity matrix from 0 to 340 m/s
temp = np.arange(273, 324, 1) #Creating a Temperature matrix from 273 to 324 K
P = 100 # Pressure inside the tube in Pascals
w, h = 50, 340 #simple variables for width and height of Mach number matrix
M = [[0 for x in range(w)] for y in range(h)] #Matrix containing Mach number data points for local v, T

#calculate the MACH number for a certain v, T
def speedSound(v,T):
     R = 287.058
     gamma = 1.4
     d = (P/(R*T))
     a = np.sqrt((gamma*P)/d)
     Mach = v/a
     return Mach


#creating all data points in the matrix.
for i in range(340):
    for j in range(50):
        M[i][j] = speedSound(vel[i], temp[j])

f = np.array(M)

#Commented out code is for 3D plot of data

'''data = [go.Surface(z=f)]
layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='elevations-3d-surface')'''

'''
p = range(50)
q = range(340)
hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')
X, Y = np.meshgrid(p,q)
ha.plot_surface(X, Y, f, rstride=1, cstride=1, cmap='hot', antialiased=False)
ha.set_xlabel("Temperature in C")
ha.set_ylabel("Speed in m/s")
ha.set_zlabel("Mach Number")
plt.show()'''

#Choosing a Mach number for Calculating Dia of tube. 
Ma = f[339][30]

A = 0.4*(Ma**2)
B = 2.8*(Ma**2)

RHS = (0.6)*((1+(2/A)**0.5))*((1-(0.4/B))**2.5)

LHS = (-1)*(1-RHS)
print LHS
Dpod = 4

Dtube = Dpod/(LHS**0.5)

print Dtube
