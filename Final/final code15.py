# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 19:38:01 2016

@author: Administrator
"""

#import numpy as np
import random
import math
import pylab as pl

class two_random_walk:
    def __init__(self, step_numbers = 1000000):
        self.N = step_numbers
        self.x = [0]
        self.y = [0]
        
    def simulation(self):
        for i in range(self.N):
#            rnd = random.random()
#            if 0<rnd<1/4:
                rnd_theta = random.uniform(0,2*math.pi)
                self.x.append(self.x[i]+ math.cos(rnd_theta))
                self.y.append(self.y[i]+ math.sin(rnd_theta))
#            elif 1/4<rnd<1/2:
#                self.x.append(self.x[i]-1)
#                self.y.append(self.y[i])
#            elif 1/2<rnd<3/4:
#                self.y.append(self.y[i]+1)
#                self.x.append(self.x[i])
#            else:
#                self.y.append(self.y[i]-1)
#                self.x.append(self.x[i])
    
    def plot1(self):
        pl.plot(self.x, self.y,'r')
        pl.plot(self.x[0],self.y[0],'ok')
        pl.plot(self.x[-1],self.y[-1],'ok')
#        pl.plot(self.x, self.y,'ok')
#        pl.plot(self.x, self.y,'c')
    def plot2(self):
        pl.plot(self.x, self.y,'k')
        pl.plot(self.x[0],self.y[0],'ok')
        pl.plot(self.x[-1],self.y[-1],'ok')
        
    
fig = pl.figure(figsize=(8,8))
t1 = two_random_walk()
t1.simulation()
t1.plot1()
t2 = two_random_walk()
t2.simulation()
t2.plot2()
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.title('Random walk in two dimensions')
pl.grid()
#pl.text(10,80,'$\\leftangle \\rho^2 \\rightangle$ versus time')