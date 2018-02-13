import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

vel = np.arange(1, 341, 1) #Creating a velocity matrix from 0 to 340 m/s
temp = np.arange(263, 324, 1) #Creating a Temperature matrix from 273 to 324 K
P = 100 #Pa
w, h = 60, 340 #simple variables for width and height of Mach number matrix
Dpod = np.arange(0.25, 10, 0.25) #Defining a range of pod diameters
Dtube = [] #Empty array for Calculating corresponding tube diameters
M = [[0 for x in range(w)] for y in range(h)] #Matrix containing Mach number data points for local v, T

#calculate the Mach number for a certain v, T
def speedSound(v,T):
     R = 287.058
     gamma = 1.4
     a = np.sqrt(gamma*R*T)
     Mach = v/a
     return Mach


#creating all data points in the matrix.
for i in range(340):
    for j in range(60):
        M[i][j] = speedSound(vel[i], temp[j])

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

def slope_calculator(array):
    v1 = 100
    v2 = 150
    m_slope = (array[v2] - array[v1]) / (v2 - v1)
    return m_slope


slope_10 = slope_calculator(x_10)
slope0 = slope_calculator(x0)
slope10 = slope_calculator(x10)
slope20 = slope_calculator(x20)
slope30 = slope_calculator(x30)
slope40 = slope_calculator(x40)
slope50 = slope_calculator(x50)



plt.figure()
plt.plot(vel, x_10)
plt.plot(vel, x0)
plt.plot(vel, x10)
plt.plot(vel, x20)
plt.plot(vel, x30)
plt.plot(vel, x40)
plt.plot(vel, x50)
plt.legend(['Temp = -10 C Y ='+str(slope_10)+'X',
            'Temp = 0 C Y ='+str(slope0)+'X',
            'Temp = 10 C Y ='+str(slope10)+'X',
            'Temp = 20 C Y ='+str(slope20)+'X',
            'Temp = 30 C Y ='+str(slope30)+'X',
            'Temp = 40 C Y ='+str(slope40)+'X',
            'Temp = 50 C Y ='+str(slope50)+'X'], loc='upper left')
plt.xlabel('Velocity of the vehicle in m/s')
plt.ylabel('Mach Number for corresponding speed')
plt.grid()
plt.show()
