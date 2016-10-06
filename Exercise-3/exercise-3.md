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

***
## 2.Background（背景介绍）
 　　这次的作业是我第一次正式地写的python程序，虽然它们实现的功能看起来十分简单，但是我实现它们的过程去并不轻松，而且它们的原理也远比我一开始所认为的要深远得多。而且对比了其他同学的作业之后，我不得不承认我的做法有些投机取巧，因为我选择了十分规则图形作为旋转的对象。因此，我的代码虽短，但是它实现旋转的原理仍然是与其他同学别无二致的，并没有什么值得称道的地方。这次的作业L1为我们展示了计算机屏幕显像的原理，作业L2为我们展示了电影的原理。
***
## 3.Exercise（正文）

### L1
- 平移功能的实现思路：

1.将需要平移的字符串按行进行拆分
```python
a = ("#      #   #       #")
b = (" #    #    #     #  ")
c = ("  #  #     #   #    ")
d = ("   #       # #      ")
e = ("   #       #   #    ")
f = ("   #       #     #  ")
g = ("   #       #       #")
```
2.定义空格字符与换行字符
```python
h = ("\n")
j = (" ")
```
3.设计while循环结构，执行以下步骤：输出组合好字符串；在每一个行字符串前面加上空格字符并赋值到原来的行字符串中；清除桌面显示的字符串
```python
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
```

- 其中细节问题：

1.必须引入时间控制函数来控制程序运行的速度
```python
import time
...
time.sleep(0.5)
```
2.可以引入输入程序来使python程序在输入相应的指令之后才开始运行，并且执行完成之后不立即退出
```python
input("please Enter:")
```

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
<br />
### L2
- 旋转功能的实现思路：

1.找到原图形与旋转之后的图形的基本组成字符串
```python
a = ("◆◆◆◆\n")
b = ("◆◆◆◆◆◆◆◆◆◆◆◆\n")
c = ("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆\n")
d = ("◆◆\n")
e = ("                ◆◆◆◆\n")
f = ("                              ◆◆\n")
```
2.运用基本组成字符串通过字符串的运算得到原图形与旋转不同角度之后的图形并将它们定义为一个li格式的列表
```python
li = [15*a+2*b,4*c+8*d,2*b+15*e,8*f+4*c]
```
3.设计while循环结构依次循环输出列表中的各个字符串元素，并且每一次输出后都清除屏幕上的字符串
```python
i = 0
while i < 20:
    print(li[i%4])
    time.sleep(1)
    i = i+1
    os.system('cls')
```

- 其中细节之处（如果与之前有相同的地方则略过）：

通过对循环结构中计数变量取余数的方式来循环输出列表中的元素，这一点十分巧妙
```python
print(li[i%4])
```

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
***
## 4.Conclusion（结论）
　　最终，通过一天的努力，我独立完成了这次的作业，学到了很多东西，也感受的了编程的乐趣所在。并且，通过了一天的编程实践，可以从中总结出我所编程序的一些优点和缺点，也反映出我编程学习的优点和缺点
  
- 优点： 简洁
- 缺点： 关于python语法的基础知识掌握得不牢固，需要随用随查；而且不喜欢过于繁琐的编程实践活动，从而导致了熟练度上问题；还没有养成写备注的习惯（或许是由于目前所写的程序过于简单的缘故）
***
## 5.Acknowledgement（致谢：本课程既然全网络共享，允许诸位同学借鉴他人的程序，如有借鉴请致谢。作业其他内容严禁『借鉴』！！！）
* our devoted Prof. Cai
***
## 6.Reference（参考文献）
* 除了课件之外没有什么像样的参考文献可以列出来
