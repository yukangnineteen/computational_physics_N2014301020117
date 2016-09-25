# Computational Physics Homework 3
***
## 1.Contents
* L1: Move your English name on the screen
* L2: Draw what you want to draw in the 80×80 lattice with characters, and make them rotate. Wish you a big brain hole!(Such as letters, Matchstick Men, rockets and so on)

## 2.Background
* This homework is very interesting to me

## 3.Exercise

### L1
* [source code](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L1.py)
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:37:38 2016

@author: Administrator
"""
import os
import time
input("please Enter:")

a=("#      #   #       #")
b=(" #    #    #     #  ")
c=("  #  #     #   #    ")
d=("   #       # #      ")
e=("   #       #   #    ")
f=("   #       #     #  ")
g=("   #       #       #")
h=("\n")
j=(" ")
i=1
os.system("cls")
while i<20:
    print(a+h+b+h+c+h+d+h+e+h+f+h+g+h)
    time.sleep(0.5)
    i=i+1
    a=j+a
    b=j+b
    c=j+c
    d=j+d
    e=j+e
    f=j+f
    g=j+g
    os.system("cls")
    
    
input("please Enter:")
```


![](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L1.gif)

### L2
* [source code](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L2.py)
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:26:51 2016

@author: Administrator
"""
import time
import os
input("Please Enter:")
os.system("cls")
a=("◆◆◆◆\n")
b=("◆◆◆◆◆◆◆◆◆◆◆◆\n")
c=("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆\n")
d=("◆◆\n")
e=("                ◆◆◆◆\n")
f=("                              ◆◆\n")
li=[15*a+2*b,4*c+8*d,2*b+15*e,8*f+4*c]
i=0
while i<20:
    print(li[i%4])
    time.sleep(1)
    i=i+1
    os.system('cls')
    
input("please Enter:")
```
![](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L2.gif)

## 4.Conclusion
* Finished
