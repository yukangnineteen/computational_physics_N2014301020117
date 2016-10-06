# Computational Physics Homework 3
***
#### Student class: 14级弘毅班
#### Student name: 余康
#### Student Number: 2014301020117
***
## 1.Abstract(摘要)
1. 在课程主页上复习这两次课程的内容，初步掌握python和matplotlib的语法规则，为接下来的课程做好准备
2. 需要提交的作业内容

- 作业L1 在屏幕上让你的英文名字水平移动起来 

> 提示：可以使用如下语句把屏幕清理干净
```python
import os
i = os.system('cls')
```
字符移动可以用在每行前面增加空格的方法实现
```python
print("      ###")
print("     #   ")
print("     #   ")
print("     #   ")
print("      ###")
```
 
- 作业L2 在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）
 
> 提示：字符串变成列表
```python
a = "test"
l = list(a)
```
列表变成字符串
```python
a = "".join(l)
```
当然有更多的方法解决这个问题，除了画的东西，方法上也希望各位能脑洞大开！

## 2.Background（背景介绍）


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

a = ("#      #   #       #")
b = (" #    #    #     #  ")
c = ("  #  #     #   #    ")
d = ("   #       # #      ")
e = ("   #       #   #    ")
f = ("   #       #     #  ")
g = ("   #       #       #")
h = ("\n")
j = (" ")
i = 1
os.system("cls")
while i < 20:
    print(a+h+b+h+c+h+d+h+e+h+f+h+g+h)
    time.sleep(0.5)
    i = i+1
    a = j+a
    b = j+b
    c = j+c
    d = j+d
    e = j+e
    f = j+f
    g = j+g
    os.system("cls")
    
    
input("please Enter:")
```

* [output](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L1.gif)

![GIF-L1](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L1.gif)

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
a = ("◆◆◆◆\n")
b = ("◆◆◆◆◆◆◆◆◆◆◆◆\n")
c = ("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆\n")
d = ("◆◆\n")
e = ("                ◆◆◆◆\n")
f = ("                              ◆◆\n")
li = [15*a+2*b,4*c+8*d,2*b+15*e,8*f+4*c]
i = 0
while i < 20:
    print(li[i%4])
    time.sleep(1)
    i = i+1
    os.system('cls')
    
input("please Enter:")
```
* [output](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L2.gif)

![GIF-L2](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-3/computational_physics%20homework%203-L2.gif)

## 4.Conclusion
* Finally I made it alone and in the process of it I learned a lot more than what I had learned in the class

## 5.Acknowledgement
* our devoted professor
