# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 17:27:39 2016

@author: Mobingbizhen
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:33:03 2016

@author: Mobingbizhen
"""
import pylab as pl
import math
import numpy as np

#From the 7th homework
class routes_to_chaos:
    def __init__(self, time_step = 0.01, time_duration = 100, initial_theta = 0.2, length = 9.8, strength_of_damping = 0.5, amplitude = 1.2, anguluar_frequency = 0.66666666):
        self.l = length
        self.dt = time_step
        self.T = time_duration
        self.n_steps = int(self.T / self.dt + 1)
        self.theta = [initial_theta]
        self.omega = [0]
        self.t = [0]
        self.g = 9.8
        self.q = strength_of_damping
        self.F_D = amplitude   #The unit of F_D is /s虏
        self.Omega_D = anguluar_frequency
        
    def calculate(self):
        for i in range(self.n_steps):
            self.omega.append(self.omega[i] - self.g / self.l * math.sin(self.theta[i]) * self.dt - self.q * self.omega[i] * self.dt + self.F_D * math.sin(self.Omega_D * self.t[i]) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            while(self.theta[i + 1] > math.pi):
                self.theta[i + 1] -= 2 * math.pi
            while self.theta[i + 1] < -math.pi:
                self.theta[i + 1] += 2 * math.pi
            self.t.append(self.t[i] + self.dt)
            
    def show(self):
        pl.plot(self.t, self.theta, label = '$F_D =$' + str(self.F_D))
        pl.xlim(0, 100)
        pl.ylim(-4, 4)
        pl.xlabel('time ($s$)')
        pl.ylabel('$\\theta$ (radians)')
        pl.legend()
#        pl.text(32, 2, '$\\theta$ versus time $F_D =$' + str(self.F_D))

#pl.subplot(311)
#r1 = routes_to_chaos(amplitude = 1.35)
#r1.calculate()
#r1.show()
#pl.subplot(312)
#r2 = routes_to_chaos(amplitude = 1.44)
#r2.calculate()
#r2.show()
#pl.subplot(313)
#r3 = routes_to_chaos(amplitude = 1.465)
#r3.calculate()
#r3.show()
#pl.show()

#r= routes_to_chaos(amplitude = 1.465)
#r.calculate()
#r.show()

r1 = routes_to_chaos(amplitude = 1.35)
r1.calculate()
r1.show()
r2 = routes_to_chaos(amplitude = 1.44)
r2.calculate()
r2.show()
r3 = routes_to_chaos(amplitude = 1.465)
r3.calculate()
r3.show()
pl.show()