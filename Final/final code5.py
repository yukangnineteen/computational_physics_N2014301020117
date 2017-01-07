# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 08:21:25 2016

@author: Administrator
"""
import numpy as np
import random
import math
import pylab as pl

class oneDimension_random_walk:
    def __init__(self, step_number = 100000):
        self.N = step_number
        self.n = [0]    
        self.x = [0]
        self.x2ave = [0]
        
    
    def simulation(self):
        for i in range(self.N):
            rnd = random.random()
            if rnd > 0.5:
                self.x.append(self.x[i] + 1)
            else:
                self.x.append(self.x[i] - 1)
            self.n.append(i+1)

    def plot1(self):
        y = np.linspace(0,0,100001)
        pl.plot(self.n, self.x, 'ok')
        pl.plot(self.n, y, ':k')
        
#        pl.ylim(-20,20)
    def plot2(self):
        y = np.linspace(0,0,100001)
        pl.plot(self.n, self.x, 'ow')
        pl.plot(self.n, y, ':k')

o = oneDimension_random_walk()
o.simulation()
fig = pl.figure(figsize=(8,8))
o.plot1()
#d = oneDimension_random_walk()
#d.simulation()
#d.plot2()
pl.xlabel('step number')
pl.ylabel('$x$')
pl.title('Random walk in one dimension')
#pl.text(10,80,'$\\leftangle x^2 \\rightangle$ versus time')
pl.show()            
            
        

    