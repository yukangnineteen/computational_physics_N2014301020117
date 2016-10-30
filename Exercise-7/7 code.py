# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:58:53 2016

@author: Administrator
"""

#Chapter 3 Oscillatory Motions and Chaos
#Section 3.1 & 3.2
#in SI
import pylab as pl
import math
import numpy as np
#import fractions as fr
class simple_harmonic_motion(object):
    
#    def __init__(self, time_step = float(input('time step: ')), time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), length = float(input('length: ')), strength_of_damping = float(input('stength of damping: ')), amplitude = float(input('amplitude of driving force: ')), anguluar_frequency = float(input('angular frequency of driving force: '))):
    def __init__(self, time_step = 0.04, time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), length = 9.8, strength_of_damping = float(input('damping factor: ')), amplitude = float(input('amplitude of driving force: ')), anguluar_frequency = 0.66666666):
        self.l = length
        self.dt = time_step
        self.T = time_duration
        self.n_steps = int(self.T / self.dt + 1)
        self.theta = [initial_theta]
        self.omega = [0]
        self.t = [0]
        self.g = 9.8
        self.q = strength_of_damping
        self.F_D = amplitude   #The unit of F_D is /s²
        self.Omega_D = anguluar_frequency
    
    def calculate(self):
        for i in range(self.n_steps):
            self.omega.append(self.omega[i] - self.g / self.l * math.sin(self.theta[i]) * self.dt - self.q * self.omega[i] * self.dt + self.F_D * math.sin(self.Omega_D * self.t[i]) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
##            print("12")90
#            while(self.theta[i + 1] > math.pi):
#                self.theta[i + 1] -= 2 * math.pi
##                print("123")
##                if self.theta[i + 1] <= math.pi:
##                    break
##                break
#            while self.theta[i + 1] < -math.pi:
#                self.theta[i + 1] += 2 * math.pi
##                print("124")
##                if self.theta[i + 1] >= -math.pi:
##                    break
##                break
            self.t.append(self.t[i] + self.dt)
        global omega
        omega = self.omega
        global time_array
        time_array = np.array(self.t)
        global a
        a = np.array(self.theta)
#        print(a)
        
    
    def calculate_delta(self):
#        b= simple_harmonic_motion(time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), amplitude = float(input('amplitude of driving force: ')))
        b= simple_harmonic_motion()
        b.calculate()
#        self.theta_1 = b.calculate(self).self.theta
        self.theta_1 = a
#        print(self.theta_1)
        b= simple_harmonic_motion(time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), strength_of_damping = float(input('damping factor: ')), amplitude = float(input('amplitude of driving force: ')))
#        b= simple_harmonic_motion()
        b.calculate()
#        self.theta_2 = b.calculate().self.theta
        self.theta_2 = a
#        print(self.theta_2)
        self.delta = [abs(self.theta_1[0] - self.theta_2[0])]
#        self.log_delta = [math.log10(abs(self.theta_1[0] - self.theta_2[0]))]
#        self.delta = self.theta_1 - self.theta_2
        self.time_array = time_array
        for i in range(self.n_steps):
            self.delta.append(abs(self.theta_1[i + 1] - self.theta_2[i + 1]))
#            self.log_delta.append(math.log10(abs(self.theta_1[i + 1] - self.theta_2[i + 1])))
#        print(self.delta)
#        print(self.time_array)

    def phase(self):
        self.n = int(self.T / (3 * math.pi))
        self.time_phase = [0]
        self.theta_phase = [0.2]
        self.omega_phase = [0]
#        print(self.t)
#        print(self.omega)
#        print(self.theta)
        for i in range(self.n):
            index = int(3 * (i + 1) * math.pi / self.dt)
            if abs(self.t[index] - 3 * (i + 1)) < self.dt / 2:
                self.time_phase.append(self.t[index])
                self.omega_phase.append(self.omega[index])
                self.theta_phase.append(self.theta[index])
            else:
                self.time_phase.append(self.t[index + 1])
                self.omega_phase.append(self.omega[index + 1])
                self.theta_phase.append(self.theta[index + 1])
        
    
    def show(self):
#        pl.semilogy(self.theta, self.omega)
#                , label = '$L =%.1f m, $'%self.l + '$dt = %.2f s, $'%self.dt + '$\\theta_0 = %.2f radians, $'%self.theta[0] + '$q = %i, $'%self.q + '$F_D = %.2f, $'%self.F_D + '$\\Omega_D = %.1f$'%self.Omega_D)
        pl.plot(self.time_array,self.delta)
        
#        pl.show()
#        pl.semilogy(self.time_array, self.delta)
#        pl.legend(loc = 'upper center', fontsize = 'small')
#        pl.xlabel('$time (s)$')
#        pl.ylabel('$\\Delta\\theta (radians)$')
#        pl.xlim(0, self.T)
#        pl.ylim(float(input('ylim-: ')),float(input('ylim+: ')))
#        pl.ylim(1E-11, 0.01)
#        pl.text(4, -0.15, 'nonlinear pendulum - Euler-Cromer method')
#        pl.text(10, 1E-3, '$\\Delta\\theta versus time F_D = 0.5$')
#        pl.title('Simple Harmonic Motion')
#        pl.title('Chaotic Regime')
    
    def show_log(self):
#        pl.subplot(121)
        pl.semilogy(self.time_array, self.delta, 'c')
        pl.xlabel('$time (s)$')
        pl.ylabel('$\\Delta\\theta$ (radians)')
        pl.xlim(0, self.T)
#        pl.ylim(1E-11, 0.01)
        pl.text(42, 1E-7, '$\\Delta\\theta$ versus time $F_D = 1.2$', fontsize = 'x-large')
        pl.title('Chaotic Regime')
        pl.show()
        
#    def show_log_sub122(self):
#        pl.subplot(122)
#        pl.semilogy(self.time_array, self.delta, 'g')
#        pl.xlabel('$time (s)$')
#        pl.ylabel('$\\Delta\\theta$ (radians)')
#        pl.xlim(0, self.T)
#        pl.ylim(1E-6, 100)
#        pl.text(20, 1E-5, '$\\Delta\\theta$ versus time $F_D = 1.2$', fontsize = 'x-large')
#        pl.title('Chaotic Regime')
#        pl.show()

    def multi_show(self):
        for i in range(2):
            a = simple_harmonic_motion(time_step = float(input('time step: ')), time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), length = float(input('length: ')), strength_of_damping = float(input('stength of damping: ')), amplitude = float(input('amplitude of driving force: ')), anguluar_frequency = float(input('angular frequency of driving force: ')))
            a.calculate()
            a.show()
        pl.show()
            
            
            
 
#class please_input():
#        string_input = input('xlocation ,ylocation: ')
#        numbers = [float(n) for n in string_input.split()]        
#        x = numbers[0]
#        y = numbers[1]
        
        

#b = simple_harmonic_motion()
#b.calculate_delta()
#b.show()

s = simple_harmonic_motion()
s.calculate_delta()
#s.show()
s.show_log()

#s = simple_harmonic_motion()
#s.calculate_delta()
#s.show_log()
#c = simple_harmonic_motion()
#c.calculate_delta()
#c.show_log()

#s = simple_harmonic_motion(time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), strength_of_damping = float(input('damping factor: ')), amplitude = float(input('amplitude of driving force: ')))
##s = simple_harmonic_motion()
#s.calculate_delta()
#s.show_log_sub122()