# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 17:34:41 2016

@author: Mobingbizhen
"""
import pylab as pl
import math 

#From the 7th homework
class routes_to_chaos:
    def __init__(self, time_step = 0.01, time_duration = 10000, initial_theta = 0.2, length = 9.8, strength_of_damping = 0.5, amplitude = 1.35, anguluar_frequency = 0.66666666):
        self.p = 2 * math.pi / anguluar_frequency
        self.l = length
        self.dt = self.p / 1000
        self.T = time_duration
        self.n_steps = int(self.T / self.dt + 1)
        self.theta = [initial_theta]
        self.omega = [0]
        self.t = [0]
        self.g = 9.8
        self.q = strength_of_damping
        self.F_D = amplitude   #The unit of F_D is /s
        self.Omega_D = anguluar_frequency
        self.p = 2 * math.pi / anguluar_frequency
        
    def calculate(self):
        for i in range(self.n_steps):
            self.omega.append(self.omega[i] - self.g / self.l * math.sin(self.theta[i]) * self.dt - self.q * self.omega[i] * self.dt + self.F_D * math.sin(self.Omega_D * self.t[i]) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            while(self.theta[i + 1] > math.pi):
                self.theta[i + 1] -= 2 * math.pi
            while self.theta[i + 1] < -math.pi:
                self.theta[i + 1] += 2 * math.pi
            self.t.append(self.t[i] + self.dt)
    
    def phase(self, varphi):
        self.varphi = varphi
        self.n = int(self.T / self.p)
        self.time_phase = [0]
        self.theta_phase = [0.2]
        self.omega_phase = [0]
        for i in range(self.n):
            self.time_phase.append(self.t[int(self.varphi / (self.dt * self.Omega_D)) + 1000 * i])
            self.theta_phase.append(self.theta[int(self.varphi / (self.dt * self.Omega_D)) + 1000 * i])
            self.omega_phase.append(self.omega[int(self.varphi / (self.dt * self.Omega_D)) + 1000 * i])
        for i in range(100):
            del self.time_phase[0]
            del self.theta_phase[0]
            del self.omega_phase[0]
            
#    def phase(self):
#        self.n = int(self.T / (3 * math.pi))
#        self.time_phase = [0]
#        self.theta_phase = [0.2]
#        self.omega_phase = [0]
#        for i in range(self.n):
#            index = int((3 * (i + 1) * math.pi) / self.dt)
#            if abs(self.t[index] - (3 * (i + 1) * math.pi - 3 * math.pi / 8)) < self.dt / 2:
#                self.time_phase.append(self.t[index])
#                self.omega_phase.append(self.omega[index])
#                self.theta_phase.append(self.theta[index])
#            else:
#                self.time_phase.append(self.t[index + 1])
#                self.omega_phase.append(self.omega[index + 1])
#                self.theta_phase.append(self.theta[index + 1])
        
    def show_phase(self):
        pl.plot(self.theta_phase, self.omega_phase, 'r.')
        pl.xlim(-4, 4)
        pl.ylim(-4, 4)
        pl.text(-2.7, 2, '$\\omega$ versus $\\theta$ $F_D =$' + str(self.F_D), fontsize = 'large')

#r1 = routes_to_chaos(amplitude = 1.465)
#r1.calculate()
#r1.phase(0)
#r1.show_phase()
#pl.xlabel('$\\theta$ (radians)')
#pl.ylabel('$\\omega$ (radians/s)')
#pl.show()
pl.subplot(221)
r1 = routes_to_chaos(amplitude = 1.2)
r1.calculate()
r1.phase(0)
r1.show_phase()
pl.ylabel('$\\omega$ (radians/s)')
pl.subplot(222)
r2 = routes_to_chaos(amplitude = 1.35)
r2.calculate()
r2.phase(0)
r2.show_phase()
pl.subplot(223)
r3 = routes_to_chaos(amplitude = 1.44)
r3.calculate()
r3.phase(0)
r3.show_phase()
pl.xlabel('$\\theta$ (radians)')
pl.ylabel('$\\omega$ (radians/s)')
pl.subplot(224)
r4 = routes_to_chaos(amplitude = 1.465)
r4.calculate()
r4.phase(0)
r4.show_phase()
pl.xlabel('$\\theta$ (radians)')
pl.show()