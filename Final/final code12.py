# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 15:51:40 2016

@author: Administrator
"""

import numpy as np
import random
import math
import pylab as pl

class two_random_walk:
    def __init__(self, step_numbers = 3):
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
        pl.plot(self.x, self.y,'ok')
        pl.plot(self.x, self.y,'c')
    
    def plot1(self):
#        pl.plot(self.x, self.y,'r')
#        pl.plot(self.x[0],self.y[0],'ok')
#        pl.plot(self.x[-1],self.y[-1],'ok')
        pl.plot(self.x, self.y,'or')
        pl.plot(self.x, self.y,'r')
        
    def plot2(self):
#        pl.plot(self.x, self.y,'k')
#        pl.plot(self.x[0],self.y[0],'ok')
#        pl.plot(self.x[-1],self.y[-1],'ok')
        pl.plot(self.x, self.y,'ok')
        pl.plot(self.x, self.y,'k')
    
    def plotgrid(self):
        self.x_var = np.linspace(-10,10,21)
        self.y_var = np.linspace(-10,10,21)
        for i in range(21):
            self.xi = np.linspace(i-10,i-10,21)
            self.yi = np.linspace(i-10,i-10,21)
            pl.plot(self.xi,self.y_var,':k')
            pl.plot(self.x_var,self.yi,':k')            
#            print(self.xi,self.yi)

        
        
    

        
        
fig = pl.figure(figsize=(8,8))
#t1 = two_random_walk()
#t1.simulation()
#t1.plot1()
#t1.plotgrid()
t2 = two_random_walk()
t2.simulation()
t2.plot2()
t2.plotgrid()
pl.xlim(-3,3)
pl.ylim(-3,3)
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.title('Random walk in two dimensions')
pl.grid()
#t = two_random_walk()
#t.plotgrid()
