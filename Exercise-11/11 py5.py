# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:57:30 2016

@author: Administrator
"""

#The eleventh homework of comptational physics
#The unit of distance is 'HU' ad=nd the time unit is 'Hyperion-year'
import math
import pylab as pl
class Hyperion:
    def __init__(self, initial_speed, duration, time_step, initial_theta):
        self.GM = 4 * math.pi ** 2
        self.xc = [1]
        self.yc = [0]
        self.vx = [0]
        self.vy = [initial_speed]
        self.T = duration
        self.dt = time_step
        self.N = int(self.T / self.dt)
        self.theta = [initial_theta]
        self.omega = [0]
        
    def compute(self):
        self.t = [0]
        self.rc = [1]
        for i in range(self.N):
            self.vx.append(self.vx[i] - self.GM * self.xc[i] / math.pow(self.rc[i], 3) * self.dt)
            self.vy.append(self.vy[i] - self.GM * self.yc[i] / math.pow(self.rc[i], 3) * self.dt)
            self.xc.append(self.xc[i] + self.vx[i + 1] * self.dt)
            self.yc.append(self.yc[i] + self.vy[i + 1] * self.dt)
            self.rc.append(math.sqrt(self.xc[i + 1] ** 2 + self.yc[i + 1] ** 2))
            self.omega.append(self.omega[i] - 3 * self.GM * (self.xc[i] * math.sin(self.theta[i]) - self.yc[i] * math.cos(self.theta[i])) * (self.xc[i] * math.cos(self.theta[i]) + self.yc[i] * math.sin(self.theta[i])) / math.pow(self.rc[i], 5) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            while self.theta[i + 1] > math.pi:
                self.theta[i + 1] = self.theta[i + 1] - 2 * math.pi
            while self.theta[i + 1] <= -math.pi:
                self.theta[i + 1] = self.theta[i + 1] + 2 * math.pi
            self.t.append(self.t[i] + self.dt)
    
    def compute_delta(self):
        self.tprime = [0]
        h1 = Hyperion(2 * math.pi, 10, 0.0001, 0)
        h2 = Hyperion(2 * math.pi, 10, 0.0001, 0.01)
        self.deltatheta = [0.01]
        h1.compute()
        h2.compute()
#        print(h1.theta)
#        print(h2.theta)
#        h1.compute()
#        self.t = h1.compute.self.t
        for i in range(self.N):
#            h1.compute()
#            h2.compute()
            self.deltatheta.append(abs(h1.theta[i + 1] - h2.theta[i + 1]))
            self.tprime.append(self.tprime[i] + self.dt)
    
    def plot(self):
        pl.plot(self.t, self.theta)
        
        
    def plot_delta(self):
        pl.figure(figsize = (8, 8))
        pl.semilogy(self.tprime, self.deltatheta, 'r.')
#        pl.ylim(0.0001, 0.1)
#        pl.ylim(0.0001, 0.1)
        pl.xlim(0, 10)
        pl.ylabel('$\\Delta\\theta$ (radians)')
        pl.xlabel('time (yr)')
        pl.title('Hyperion $\\theta$ versus time')
        pl.text(4.1, 3.3, 'Circular orbit')


H = Hyperion(2 * math.pi, 10, 0.0001, 0)
#H.compute()
H.compute_delta()
H.plot_delta()

