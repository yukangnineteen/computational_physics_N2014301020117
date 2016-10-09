# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 10:39:10 2016

@author: Administrator
"""

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
    def __init__(self, number_of_nuclei_A = 75, number_of_nuclei_B = 25, time_constantA = 2, time_constantB = 1, time_of_duration = 5, time_step = 0.05 ):
        self.n_A = [number_of_nuclei_A]
        self.n_B = [number_of_nuclei_B]
        self.t = [0]
        self.tauA = time_constantA
        self.tauB = time_constantB
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei A ->", number_of_nuclei_A)
        print("Initial number of nuclei B ->", number_of_nuclei_B)
        print("Time constant of nuclei A ->", time_constantA)
        print("Time constant of nuclei B ->", time_constantB)        
        print("Time step ->", time_step)
        print("Total time ->", time_of_duration)

    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.n_A[i] + (self.n_B[i] / self.tauB - self.n_A[i] / self.tauA) * self.dt
            tmp_B = self.n_B[i] + (self.n_A[i] / self.tauA - self.n_B[i] / self.tauB) * self.dt
            self.n_A.append(tmp_A)
            self.n_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
           
    def show_results(self):
        pl.plot(self.t, self.n_A, 'b--', label='Number of Nuclei A: Time Constant = 2')
        pl.plot(self.t, self.n_B, 'g', label='Number of Nuclei B: Time Constant = 1')
        pl.title('Double Decay Probelm - Nuclei with Different Time Constans')
        pl.xlim(0.0, 5.0)
        pl.ylim(0.0, 100.0)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc='best', shadow=True)
        
    def store_results(self):
        myfile = open('4(improved-12) data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_A[i], self.n_B[i], file = myfile)
        myfile.close()

#matplotlib inline
a = nuclei_decay()
a.calculate()
a.show_results()
a.store_results()