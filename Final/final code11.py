# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 19:50:42 2016

@author: Administrator
"""

import numpy as np
import random
import math
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D 

class two_random_walk:
    def __init__(self, step_numbers = 100):
        self.N = step_numbers
        self.x = [0]
        self.y = [0]
        
    def simulation(self):
        for i in range(self.N):
            rnd = random.random()
            if 0<rnd<1/4:
                self.x.append(self.x[i]+1)
                self.y.append(self.y[i])
            elif 1/4<rnd<1/2:
                self.x.append(self.x[i]-1)
                self.y.append(self.y[i])
            elif 1/2<rnd<3/4:
                self.y.append(self.y[i]+1)
                self.x.append(self.x[i])
            else:
                self.y.append(self.y[i]-1)
                self.x.append(self.x[i])
    
    def plot(self):
        fig = pl.figure() 
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.x,self.y)
        ax.plot(self.x,self.y)
#        pl.plot(self.x, self.y,'ok')
#        pl.plot(self.x, self.y,'c')

    
        
t = two_random_walk()
t.simulation()
t.plot()