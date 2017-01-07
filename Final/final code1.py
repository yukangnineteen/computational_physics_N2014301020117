# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:42:15 2016

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
        self.x = 0
        self.x_store = 0
        self.x2 = 0        
        self.x2ave = [0]
        self.xave = [0]

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
            self.x_store = 0
            self.x2 = 0
            for j in range(self.M):
                self.x = 0
                for k in range(i):
                    rnd = random.random()
                    if rnd > 0.5:
                        self.x += 1
                    else:
                        self.x -= 1
                self.x2 += math.pow(self.x, 2)
                self.x_store += self.x
            self.xave.append(self.x_store/self.M)    
            self.x2ave.append(self.x2/self.M)
            self.n.append(i+1)

    def fit(self):
        z = np.polyfit(self.n, self.xave, 1)
        p = np.poly1d(z)
        print(z)
        print(p)
        self.xave_fit = [z[1]]
        for i in range(self.N):
            self.xave_fit.append(i*z[0] + z[1])
            
    def plot(self):
        fig = pl.figure(figsize=(8,8))
        pl.plot(self.n,self.xave,'.c')
        pl.plot(self.n,self.xave_fit,'k')
        pl.ylim(-1,1)
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
   

      
    
o = one_random_walk()
o.simulation()
o.fit()
o.plot()    
pl.xlabel('step number (= time)')
pl.ylabel('$\\leftangle x \\rightangle$')
pl.title('Random walk in one dimension')
pl.text(10,0.5,'$\\leftangle x \\rightangle$ versus time')