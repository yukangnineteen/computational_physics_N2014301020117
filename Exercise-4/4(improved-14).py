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
    def __init__(self, number_of_nuclei_A1 = 100, number_of_nuclei_B1 = 0,number_of_nuclei_A2 = 75, number_of_nuclei_B2 = 25,number_of_nuclei_A3 = 50, number_of_nuclei_B3 = 50, time_constantA = 1, time_constantB = 2, time_of_duration = 5, time_step = 0.05 ):
        self.n_A1 = [number_of_nuclei_A1]
        self.n_B1 = [number_of_nuclei_B1]
        self.n_A2 = [number_of_nuclei_A2]
        self.n_B2 = [number_of_nuclei_B2]
        self.n_A3 = [number_of_nuclei_A3]
        self.n_B3 = [number_of_nuclei_B3]
        self.t = [0]
        self.tauA = time_constantA
        self.tauB = time_constantB
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei A 1->", number_of_nuclei_A1)
        print("Initial number of nuclei B 1->", number_of_nuclei_B1)
        print("Initial number of nuclei A 2->", number_of_nuclei_A2)
        print("Initial number of nuclei B 2->", number_of_nuclei_B2)
        print("Initial number of nuclei A 3->", number_of_nuclei_A3)
        print("Initial number of nuclei B 3->", number_of_nuclei_B3)
        print("Time constant of nuclei A ->", time_constantA)
        print("Time constant of nuclei B ->", time_constantB)        
        print("Time step ->", time_step)
        print("Total time ->", time_of_duration)

    def calculate(self):
        for i in range(self.nsteps):
            tmp_A1 = self.n_A1[i] + (self.n_B1[i] / self.tauB - self.n_A1[i] / self.tauA) * self.dt
            tmp_B1 = self.n_B1[i] + (self.n_A1[i] / self.tauA - self.n_B1[i] / self.tauB) * self.dt
            self.n_A1.append(tmp_A1)
            self.n_B1.append(tmp_B1)
            tmp_A2 = self.n_A2[i] + (self.n_B2[i] / self.tauB - self.n_A2[i] / self.tauA) * self.dt
            tmp_B2 = self.n_B2[i] + (self.n_A2[i] / self.tauA - self.n_B2[i] / self.tauB) * self.dt
            self.n_A2.append(tmp_A2)
            self.n_B2.append(tmp_B2)
            tmp_A3 = self.n_A3[i] + (self.n_B3[i] / self.tauB - self.n_A3[i] / self.tauA) * self.dt
            tmp_B3 = self.n_B3[i] + (self.n_A3[i] / self.tauA - self.n_B3[i] / self.tauB) * self.dt
            self.n_A3.append(tmp_A3)
            self.n_B3.append(tmp_B3)
            self.t.append(self.t[i] + self.dt)
           
    def show_results(self):
        pl.plot(self.t, self.n_A1, 'b--', label='A1: Time Constant = 1')
        pl.plot(self.t, self.n_B1, 'g', label='B1: Time Constant = 2')
        pl.plot(self.t, self.n_A2, 'k--', label='A2: Time Constant = 1')
        pl.plot(self.t, self.n_B2, 'c', label='B2: Time Constant = 2')
        pl.plot(self.t, self.n_A3, 'm--', label='A3: Time Constant = 1')
        pl.plot(self.t, self.n_B3, 'y', label='B3: Time Constant = 2')
        pl.title('Double Decay Probelm - Nuclei with Different Time Constans')
        pl.xlim(0.0, 5.0)
        pl.ylim(0.0, 100.0)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc='upper right', shadow=True, fontsize='small')
        
    def store_results(self):
        myfile = open('4(improved-14) data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_A1[i], self.n_B1[i], self.n_A2[i], self.n_B2[i],self.n_A3[i], self.n_B3[i], file = myfile)
        myfile.close()

#matplotlib inline
a = nuclei_decay()
a.calculate()
a.show_results()
a.store_results()