# Computational Physics Homework 6
***

#### Student class: 14级弘毅班
#### Student name: 余康
#### Student number: 2014301020117
***

## **1.Abstract（摘要）**

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

**It is a piece of cake to add the effect of the wind. The only thing to take care of is the algorithm of vector calculation, i.e., velocity stack. I think the orthogonal decomposition is the easiest method.**

**Net problem we will meet is that the target can be higher and lower than the "baseball-cannon".**

* **If the target is lower**

**This is an easier case because the trajectory will only intersect the horizontal line of the altitude of the target once.**

**So the judgement condition to stop to find the intersection can be easily written as 





             
             
             
             
