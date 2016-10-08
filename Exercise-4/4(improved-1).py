# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:35:43 2016

@author: Administrator
"""

import pylab as pl
class nuclei_decay:
    """
    Simulation of a decay problem with two types of nuclei
    Program to solve Chapter 1 Exercise *1.5. of 'Computational Physics' by Prof. Cai
    """
    def __init__(self, number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05 ):
        self.n_A = [number_of_nuclei_A]
        self.n_B = [number_of_nuclei_B]
        self.N = number_of_nuclei_A + number_of_nuclei_B
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei A ->", number_of_nuclei_A)
        print("Initial number of nuclei B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("Time step ->", time_step)
        print("Total time ->", time_of_duration)

    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.n_A[i] + (self.N - 2 * self.n_A[i]) / self.tau * self.dt
            tmp_B = self.N - tmp_A
            self.n_A.append(tmp_A)
            self.n_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
           
    def show_results(self):
        pl.plot(self.t, self.n_A, 'b--', label='Number of Nuclei A')
        pl.plot(self.t, self.n_B, 'g', label='Number of Nuclei B')
        pl.title('Double Decay Probelm-Situation 1')
        pl.xlim(0.0, 5.0)
        pl.ylim(0.0, 100.0)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc='best', shadow=True)
        
    def store_results(self):
        myfile = open('computational_physics homework 4(improved-1) data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_A[i], self.n_B[i], file = myfile)
        myfile.close()

#matplotlib inline
a = nuclei_decay()
a.calculate()
a.show_results()
a.store_results()
        
        
        
        
        
        
        
        
        