# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:26:51 2016

@author: Administrator
"""
import time
import os
a = ("◆◆◆◆\n")
b = ("◆◆◆◆◆◆◆◆◆◆◆◆\n")
c = ("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆\n")
d = ("◆◆\n")
e = ("                ◆◆◆◆\n")
f = ("                              ◆◆\n")
li = [15*a+2*b, 4*c+8*d, 2*b+15*e, 8*f+4*c]
i = 0
while i < 20:
    print(li[i%4])
    time.sleep(1)
    i = i+1
    os.system('cls')
    
input("please Enter:")
    
