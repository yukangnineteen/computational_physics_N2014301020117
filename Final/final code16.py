# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:50:19 2016

@author: Administrator
"""

import numpy as np
import random
import math
import pylab as pl

class one_random_walk:
    def __init__(self, maximum_numbers = 100,walkers = 5000):
#        self.N = step_muber
        self.N = maximum_numbers
        self.M = walkers
#        self.m = [0]
        self.n = [0]
#        self.r = 0
        self.x = 0
        self.y = 0
#        self.z = 0
        self.r2 = 0
        self.r2ave = [0]

#    def nsteps(self, n):
#        for i in range(n):
#            rnd = random.random()
#            if rnd > 0.5:
#                self.x += 1
#            else:
#                self.x -= 1
#            self.x2ave = math.pow(self.x,2)/n
##            return math.pow(self.x,2)/n
            
        
    def simulation(self):
        for i in range(self.N):
#            self.x = 0
            self.r2 = 0
            for j in range(self.M):
#                self.r = 0
                self.x = 0
                self.y = 0
#                self.z = 0
                for k in range(i):
                    rnd_theta = random.uniform(0,2*math.pi)
#                    rnd_fi = random.uniform(0,2*math.pi)
                    self.x += math.cos(rnd_theta)
                    self.y += math.sin(rnd_theta)
#                    self.z += math.cos(rnd_theta)
                self.r2 += math.pow(self.x,2) + math.pow(self.y,2)
            self.r2ave.append(self.r2/self.M)
            self.n.append(i+1)

    def fit(self):
        z = np.polyfit(self.n, self.r2ave, 1)
        p = np.poly1d(z)
        print(z)
        print(p)
        self.r2ave_fit = [z[1]]
        for i in range(self.N):
            self.r2ave_fit.append((i+1)*z[0] + z[1])
            
    def plot(self):
        pl.plot(self.n,self.r2ave,'.c')
        pl.plot(self.n,self.r2ave_fit,'k')
        pl.ylim(0,100)
#        for i in range(self.M):
#            self.x = 0
#            for j in range(self.N):
#                for k in range(j):
#                    rnd = random.random()        
            
#                rnd = random.random()
#                if rnd > 0.5:
#                    self.x +=1
#                else:
#                    self.x -=1
##            print(self.x)
#            self.x2 += math.pow(self.x,2)
##            print(self.x2)
#        self.x2ave = self.x2/self.M
#        print(self.x2ave)
##        return self.x2ave
   

      
fig = pl.figure(figsize=(8,8))
o = one_random_walk()
o.simulation()
o.fit()
o.plot()    
pl.xlabel('step number (= time)')
pl.ylabel('$\\leftangle \\rho^2 \\rightangle$')
pl.title('Random walk in two dimensions')
pl.text(10,80,'$\\leftangle \\rho^2 \\rightangle$ versus time')