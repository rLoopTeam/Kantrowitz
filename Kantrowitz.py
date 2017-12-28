import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

vel = np.arange(1, 341, 1) #Creating a velocity matrix from 0 to 340 m/s
temp = np.arange(263, 324, 1) #Creating a Temperature matrix from 273 to 324 K
P = 100 # Pressure inside the tube in Pascals
w, h = 60, 340 #simple variables for width and height of Mach number matrix
Dpod = np.arange(0.25, 10, 0.25) #Defining a range of pod diameters
Dtube = [] #Empty array for Calculating corresponding tube diameters
M = [[0 for x in range(w)] for y in range(h)] #Matrix containing Mach number data points for local v, T

#calculate the Mach number for a certain v, T
def speedSound(v,T):
     R = 287.058
     gamma = 1.4
     d = (P/(R*T))
     a = np.sqrt((gamma*P)/d)
     Mach = v/a
     return Mach


#creating all data points in the matrix.
for i in range(340):
    for j in range(60):
        M[i][j] = speedSound(vel[i], temp[j])

#df = pd.DataFrame(M)
#df.to_csv("Mach_raw.csv")
#Choosing a Mach number for Calculating Dia of tube.
f = np.array(M)
Ma = f[339][59]
A = (1 + (5 / (Ma**2) ) )**0.5
B = (1 - (1 / 7 * (Ma**2) ) )**2.5
X = (0.6) * A * B
RHS = abs(1-(X**0.5))

for i in Dpod:
    Dtube.append(i/(RHS))

x_10 = f[: , 0]
x0 = f[: , 10]
x10 = f[: , 20]
x20 = f[: , 30]
x30 = f[: , 40]
x40 = f[: , 50]
x50 = f[: , 59]

plt.figure()
plt.plot(vel, x_10)
plt.plot(vel, x0)
plt.plot(vel, x10)
plt.plot(vel, x20)
plt.plot(vel, x30)
plt.plot(vel, x40)
plt.plot(vel, x50)
plt.legend(['Temp = -10 C', 'Temp = 0 C', 'Temp = 10 C', 'Temp = 20 C', 'Temp = 30 C', 'Temp = 40 C', 'Temp = 50 C'], loc='upper left')
plt.xlabel('Velocity of the vehicle in m/s')
plt.ylabel('Mach Number for corresponding speed')
plt.grid()
plt.show()


'''
p = range(60)
q = range(340)
hf = plt.figure()
ha = hf.add_subplot(211, projection='3d')
X, Y = np.meshgrid(p,q)
ha.plot_wireframe(X, Y, f, rstride=10, cstride=10) #, cmap='coolwarm', linewidth=0, antialiased=False)
ha.set_xlabel("Temperature in C")
ha.set_ylabel("Speed in m/s")
ha.set_zlabel("Mach Number")

hb = hf.add_subplot(212)
hb.plot(Dtube, Dpod)
hb.set_xlabel("Diamter of Tube")
hb.set_ylabel("Diameter of Pod")
plt.grid()
plt.show()
'''
