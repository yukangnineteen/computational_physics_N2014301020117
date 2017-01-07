# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:23:24 2016

@author: Administrator
"""

import random
import math
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

class three_random_walk:
    def __init__(self, step_numbers = 1000000):
        self.N = step_numbers
        self.x = [0]
        self.y = [0]
        self.z = [0]
        
    def simulation(self):
        for i in range(self.N):
            self.x.append(self.x[i]+random.uniform(-math.sqrt(1/3),math.sqrt(1/3)))
            self.y.append(self.y[i]+random.uniform(-math.sqrt(1/3),math.sqrt(1/3))) 
            self.z.append(self.z[i]+random.uniform(-math.sqrt(1/3),math.sqrt(1/3))) 
#            rnd = random.random()
#            if 0<rnd<1/4:
#                rnd_theta = random.uniform(0,2*math.pi)
#                self.x.append(self.x[i]+ math.cos(rnd_theta))
#                self.y.append(self.y[i]+ math.sin(rnd_theta))
#            elif 1/4<rnd<1/2:
#                self.x.append(self.x[i]-1)
#                self.y.append(self.y[i])
#            elif 1/2<rnd<3/4:
#                self.y.append(self.y[i]+1)
#                self.x.append(self.x[i])
#            else:
#                self.y.append(self.y[i]-1)
#                self.x.append(self.x[i])
    
    def plot(self):
        fig = pl.figure(figsize=(8,8))
        ax1 = fig.add_subplot(111, projection='3d')
        ax1.scatter(self.x,self.y,self.z,c='k',s=10,marker='.')
#        pl.plot(self.x, self.y,'ok')
#        pl.plot(self.x, self.y,'c')
#        坐标轴
        ax1.set_zlabel('$z$') 
        ax1.set_ylabel('$y$')
        ax1.set_xlabel('$x$')
        ax1.set_title('Random walk in three dimensions')
#        pl.plot(self.x, self.y,'ok')
#        pl.plot(self.x, self.y,'c')
    
        
t = three_random_walk()
t.simulation()
t.plot()