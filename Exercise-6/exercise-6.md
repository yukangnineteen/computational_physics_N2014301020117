# Computational Physics Homework 6
***

#### Student class: 14 Hong Yi
#### Student name: Kang Yu
#### Student number: 2014301020117
***

## **1.Abstract**

> 作业分两个层次来做，大家自己选择

> * 作业L1 2.10题强化版（引入迎面风阻）

> * 作业L2 2.10题进一步升级，发展“超级辅助精确打击系统”（考虑炮弹初始发射的时候发射角度误差度，速度有5%的误差，迎面风阻误差10%，以炮弹落点与打击目标距离差平方均值最小为优胜）

>以上所有计算需要考虑海拔高度的影响，使用绝热模型进行计算，误差描述使用最简单的均匀分布描述（也就是在误差范围内每个取值概率是一样的）。完成L2作业的同学，下次上课可以比赛，对100km的目标看谁打得最精确！

#### *2.10. Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher and lower thatn the cannon. Also investgate how the minimum firing velocity required to hit the target varies as the altitude of the target is varied.

#### For simplicity, I will only introduce a methodological solution especially for the initial conditions I set. I won't give the general solution fit for all kinds of initial conditions which you can set by yourselves, but the method is proved to be valid in all situations.

***

## **2.Background**

#### Based on what we have discussed in the last homework, what we need to introduce this time is **variation of the drag coefficient** and **the effects of atomospheric drag**

* **variation of the drag coefficient**

#### In my homework, in order to add this facor, I choose a normal baseballl as my "shell" of my designed precise guidance system. From our textbook, we can know that the drag factor for a normal baseball is described reasonally well by the function (now using SI units)

![formula 1](http://latex.codecogs.com/gif.latex?B_2%20%3D%200.0039%20&plus;%20%5Cfrac%7B0.0058%7D%7B1%20&plus;%20exp%5B%28v%20-%20v_d%29%20/%20%5CDelta%5D%29%7D%20%2C)

#### with vd = 35 m/s and Δ = 5 m/s.
             
* **the effects of wind drag**

#### It is easy to see that wind has an enormous effect. Let us next add the effect of the wind. Not like the textbook, I am not goinf to assume that it is blowing in a horizontal (x) direction but I assume that it can blow in all directions. So, by symmetry, the formulas will change a little. Of course the wind has a constant magnitude and direction during the flight of the ball for reducing calculation. In this case the componesnts of the drag force become
     
![formula 2](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%20%3D%20-%20B_2%20%7C%5Coverrightarrow%7Bv%7D%20-%20%5Coverrightarrow%7Bv%7D_%7Bwind%7D%7C%28v_x%20-%20v_%7Bwind%2Cx%7D%29)             

![formula 3](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%20%3D%20-%20B_2%20%7C%5Coverrightarrow%7Bv%7D%20-%20%5Coverrightarrow%7Bv%7D_%7Bwind%7D%7C%28v_y%20-%20v_%7Bwind%2Cy%7D%29%2C)
             
#### where vwind is the velocity of the wind**(vector)**. α is the angle of wind. And α in the range [0,) corresponds to a tailwind; α in the range (90,180] means a headwind. The derivation is understood most easily if you consider the drag force in the reference frame at rest with respect to the wind.

* **adiabatic model**

#### Having been discussed in detail last time. So I will only review the formulas.

![formula 3](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%20%5Crho_0%20%281%20-%20%5Cfrac%7Bay%7D%7BT_0%7D%29%20%5E%20%5Calpha%2C)

![formula 4](http://latex.codecogs.com/gif.latex?F%5E%7B*%7D_%7Bdrag%7D%20%3D%20%5Cfrac%7B%5Crho%7D%7B%5Crho_0%7D%20F_%7Bdrag%7D%28y%20%3D%200%29.)

#### What is different is this time I realize my ignorance to set T0 = 300 K in my last homework, so I decide to set T0 = 273 K.

### *Illustration：*

#### *SI units are used all the time in this homework!*

***

## **3.Main**

## ★ Level 1

### Way of Thinking

#### ▶ **Add the wind drag**

**It is a piece of cake to add the effect of the wind. The only thing to take care of is the algorithm of vector calculation, i.e., velocity stack. I think the orthogonal decomposition is the easiest method.**

#### ▶ **Deal with different altitudes**

**Net problem we will meet is that the target can be higher and lower than the "baseball-cannon".**

* **If the target is lower**

**This is an easier case because the trajectory can only intersect the horizontal line of the altitude of the target once.**

**So the judgement condition to stop to find the intersection can be easily written: 'y[i] < y0', where y0 < 0 and is the vertical coordinate of the target.**

* **If the target is higher**

**This is more complex because the trajectory can intersect the horizontal line of the altitude of the target twice.**

**But we can reduce complexity by physical analysis to a certain extent: it is easy to conclude that the initial velocity of the "baseball shell" which hit the target when it crosses the horizontal line of the taget the first time is larger than that when it crosses the horizontal line of the target the second time. So for convenience of further requirement of the problem, I will only expalin how to find the second intersection. (Furthermore, the way to find the first intersection is the same as that in last case.)**

**So after analysis the judgement conditions to find the intersection can be written: 'y[i - 1] > y0 and y[i] < y0', wehere y0 > 0.**

**Imagine the trajectory in your mind, and you will easily understand it. We make use of the monotonicity of the parabola-like curve. It is not right all the time becasuse in fact the real function of the projectory is not analytic, let alone definite monotonicity but combined with our experience it is right most of the time.**

* **Intersection**

**Finally, I need to find the intersection(In fact, what is needed to be calculated is the horizontal coordinate.) of the trajectory and the horizontal line and set it as the last point of the trajectory.**

#### ▶ **Investigate minimum "firing" velocity**

**We can scan both velocities and firing angles to minimize the velocity. By physical qualitative analysis I conclude that it is better to scan from smaller to bigger values of both velocities and firing angles. What we need to determine is the minimum of velocity, so we need to scan all the angles for a set velocity, and then if there is no angle satisfying the requirement to reach the target point, we should increase the velocity a little bit. In the same word, what we need to do is to scan velocities, and for every determined velocity, scan angles. It is very easy to think up nested loop structure to realize the algorithm. And break all the loop structures when the requirement is satisfied: 'x[-1] > x0', where x0 is the horizontal coordinate of the target.**

***A small trick: Actually this algorithm demands a large amount of computation takes a large amount of computating time. To decrease the amount of computation and computating time(positively correlated) and improve the accuracy(negatively correlated ), I decrease the scanning scales and the scaaning intervals gradually.***

### *Summary:*

* #### *The Euler Methos*

* #### *The Double-Scan Algorithm*

### Design of Program and Result

**Declaration: In the following programs, for simplicity we will fix some initial conditions**

* ***For all cases, the vertical coordinate of the target is fixed at -100 m, and the horizontal coordinate is 220 m.***

* **When adding the effect of wind: initial velocity is 110 m/s, firing angle is 45°, velocity of the wind is 10 m/s, time step is 0.01 s.**

* **When investigating the minimum firing velocity: time step is 0.01 s, velocity of wind is 10 m/s, angle of wind is 135°.**

#### ▶ **Add the wind drag (y0 = -100 m)**

**I change the angle of wind from 85° to 95° to show the effect of the wind: 85° - 89° represents tailwind; 91° - 95° represents headwind**

* **This is its source codes**

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

* **This is its figure results**

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure1.png)

#### **Figure:**

![figure1](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure1.png)

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure2.png)

#### **Figure:**

![figure2](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure2.png)

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure3.png)

#### **Figure:**

![figure3](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure3.png)

**These pictures show the effects of wind drag. Evidently tailwind helps the baseball-shell fly furthur, and headwind prevents the baseball-shell flying furthur. It consists in our practice.**

***Small tips: The tool 'Zoom to rectangular' allow us to choose part of figure to display with appropriate plotting scales to show more details.***

#### ▶ **Investigate minimum "firing" velocity (x0 = 220 m, y0 = -100 m)**

**I run my program to explore the minimum velocity under the fixed initial conditions. Next, I will show my approaching method in the following figures with different plotting scales.

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure4.png)

#### **Figure:**

![figure4](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure4.png)
             
**There seems to be only one curve in the figure, but I will gradually revel the truth.**

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure5.png)

#### **Figure:**

![figure5](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure5.png)

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure6.png)

#### **Figure:**

![figure6](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure6.png)  

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure7.png)

#### **Figure:**

![figure7](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure7.png)

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure8.png)

#### **Figure:**

![figure8](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure8.png)

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20code.py)

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure9.png)

#### **Figure:**

![figure9](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-6/6%20figure9.png)

**These figures show the same scanning process in different plotting scales. From left to right, the falling point of my baseball-shell appoaches x0(220 m). The velocity changes one time; the angle changes 10 times correspondingly if x0 is not reached. Once x0 is reached, the program prints the corresponding velocity and angle. As we see, only the last curve reaches(exceeds) x0, so the program stops here(no more calculation and plotting).**

***In fact, the final scan intervals are extremely small: v += 0.00001, θ += 0.0001.*** 


             
