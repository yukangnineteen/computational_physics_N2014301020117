# Computational Physics Homework 5
***

#### Student class: 14 Hong Yi
#### Student name: Kang Yu
#### Student number: 2014301020117
***

## **1.Abstract**
> 抱歉作业更新晚了！2.2章作业任选一题。

#### Exercises
#### 2.8. In our model of the cannon shell trajectory we have assumed that the acceleration due to gravity, ***g***, is a constant. It will, of course, depend on altitude. Add this to the model and calculate how much it affects the range.

#### 2.9. Calculate the trajectory of of our cannon shell including both air drag and the reduced air density at high altitudes so that you can reproduce the results in Figure 2.5. Perform your calculation for different firing angles and determine the value of the angle that gives the maximum range.

#### All in all, what I would like to do is to explore the effects of ***g***'s independence on altitude, air drag and the reduced air density on the cannon shell trajectory.


----------


## **2.Background**
* **Projectile Motion**

#### On this topic, we have learned too much about it from our junior high schools to senior high schools, so I have nothing special to say.

* **gravitational acceleration**

#### In our problems, we will need to use the relation between ***g*** and altitude:

![formula 1](http://latex.codecogs.com/gif.latex?g%28y%29%20%3D%20GM_E%5Cfrac%7B1%7D%7B%28R_E%20&plus;%20y%29%20%5E%202%7D)

#### where ***ME*** is the mass of the Earth, ***RE*** is the average radius of the Earth, and ***y*** is the distance between the cannon shell and the surface of the Earth.

* **air drag**

#### According to our textbook, it is not difficult to find by energy relation that:

![formula 2](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%20%5Capprox%20-%20%5Cfrac%7B1%7D%7B2%7DC%5Crho%20Av%20%5E%202)

#### where ***C*** is known as the drag coefficient, and can be simply assumed to be ***1***. To be more simplified, we have:

![formula 3](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%20%3D%20-%20B_2%20v%20%5E%202)

#### What really matters is that ***B2*** is proportional to ***ρ***. So:

![formula 4](http://latex.codecogs.com/gif.latex?F%5E*_%7Bdrag%7D%20%3D%20%5Cfrac%7B%5Crho%7D%7B%5Crho_0%7DF_%7Bdrag%7D%28y%3D0%29)


* **air density**

**1.Isothermal model**

#### From our Thermaldynamics and Statistical Physics course, we have a conclusion :

![formula 5](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%20%5Crho_0%20exp%28-%20y%20/%20y_0%29)

#### where ***y0 = k_BT/mg ≈ 1.0E+4 m***, and ***ρ*** is density at sea level (***y = 0***).

#### From this and what I have emphasized before, we have:

![formula 6](http://latex.codecogs.com/gif.latex?F%5E*_%7Bdrag%7D%20%3D%20exp%28-%20y%20/%20y_0%29F_%7Bdrag%7D)
***



**2.Adiabatic model**

#### In the same way, we have a conclusion:

![formula 7](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%20%5Crho_0%20%281%20-%20%5Cfrac%7Bay%7D%7BT_0%7D%29%20%5E%20%5Calpha)

#### where ***a ≈ 6.5 K/km***, ***T0*** is the sea level temperature (in ***K***), and the exponent ***α ≈ 2.5*** for air.

#### From this and what I have emphasized before, we have:

![formula 8](http://latex.codecogs.com/gif.latex?F%5E*_%7Bdrag%7D%20%3D%20%281%20-%20%5Cfrac%7Bay%7D%7BT_0%7D%29%20%5E%20%5Calpha%20F_%7Bdrag%7D)



----------
## **3.Main**

### Way of Thinking

**I still choose to use the dirty and quick method - The Euler Mehtod (So no more illumination is to be made)**
* **Other Than:**

**There is a *small tip* when we need to deal with second-order ODE by the Euler Method. Fourtunately, it has very clear physical meanings.**

**That is:**

![formula plus 1](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%20%5E%202%20x%7D%7Bdt%20%5E%202%7D%20%3D%200)

![formula plus 2](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%20%5E%202%20y%7D%7Bdt%20%5E%202%7D%20%3D%20-%20g%2C)

**Each of the 2nd-order ODE can be transferred into two first-order ODEs, so the two 2nd-order ODEs can be transferred into the following four 1st-order ODEs:**

![formula plus 3](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%7D%7Bdt%7D%20%3D%20v_x)

![formula plus 4](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv_x%7D%7Bdt%7D%20%3D%200)

![formula plus 5](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdy%7D%7Bdt%7D%20%3D%20v_y)

![formula plus 6](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv_y%7D%7Bdt%7D%20%3D%20-%20g%2C)

**The situation is our familiar Euler Method for 1st-order OED.**
<br: />


### Design of Program and Result 

**(Declaration: The unit of distance is *km*, and other units are in SI)**

**(Another Declaration: All the constants and initial values are taken from the text book or from authoritative references, and they are '*y0 = k_BT/mg ≈ 1.0E+4 m, a ≈ 6.5 K/km, T0 = 300 K, α ≈ 2.5, G = 6.67E-20 N·m²/kg², ME = 5.98E24 kg, RE = 6317 km, v0 = 700 m/s*')**

**Firstly, I take air drag as a commom premise. Then I will the trojectory of cannon shell only affected by air drag**

* **This is its source codes**

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20code%201.py)

* **This is its figure results**

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%201.png)

#### **Figure:**

![!\[Figure1\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%201.png)][1]


**Secondly, (only) add the reduced air density - isothermal**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20code%202.py)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%202.png)

#### **Figure:**
![!\[Figure2\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%202.png)][2]


**Thirdly, (only) add the reduced air density - adiabatic**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20code%203.py)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%203.png)

#### **Figure:**
![!\[Figure3\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%203.png)][3]


**Fourthly, (only) add the *g*'s independence on altitude**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20code%204.py)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%204.png)

#### **Figure:**
![!\[Figure4\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%204.png)][4]

**Maybe, smart you have found something wrong. Yes, there is no comparison. To be more acurrate, there is forever a lonely curve in my previous figures. Hence, these are also naive programs which I would not like to show. It is because I hadn't thought up any simple approaches to plot many curves with different initial conditions in one figure. Luckily, finally, I made it with the help of my classmate.**

***So, here comes the improved version(Integrated edition, which means all infaormation are intergrated in only one figure)***

***

**There are some important skills in the new program:**

* **Class Inheritance**

* **Repeated Input**

* **New Matplotlib Skills**


**There are also some useful tricks in the new program:** 

* **some small and useful functions(in math, pl, ...)**

* **...**

**When it comes to the running results**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5(improved)%20code.py)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5(improved)%20figure.png)

#### **Figure:**

![Figure 5](https://raw.githubusercontent.com/yukangnineteen/computational_physics_N2014301020117/master/Exercise-5/5(improved)%20figure.png)

**Where there is a figure, there is a truth. Please ignore the fact that some of the cures are in the same color, which is simply because there isn't enough types of color for me to draw such plenty curves. Thank you!**

**Forget to tell that all the time steps are *0.01 s* because we have discussed the influence of it in the last homework**

**Sorry to say that the text is copied from my Cmd Markdown version, so there are some special errors that I may not well check out since I have no time to check it out carefully with patience with my time occupied by ssp**

***pity(locks) - no testing and furthur discussion and extension***

----------
## 4.Conclusion
#### First, I am sorry I fail to write smoothly in Cmd Markdown. So I drop the homework edition of Cmd Markdown.

#### Solution

* **EXERCISES 2.8.: **

**qualitative analysis: very small**

* **EXERCISES 2.9.:**

**quantative outcomes:**

> initial velocity: 70.0 m/s
  time step: 0.01 s
  maximum firing range: 0.4915 km
  corresponding firing angle: 44.9°. 
  
**(By the way, I find I forget to give the method of solving the maxmizing problem. To be Brief, SCANNING till the range decreases. The mathematical base is the monotonicity)**

#### Of course I still have many wonders that I can't solve now. In fact, I even manage thi improves program with an effort. Some more details are still to be understood.

#### Self-reflection

* **One of the drawbacks of my homework: verbose**

* **One of the progress of my homework: I begin to write notes in my programs**



----------
## 5.Acknowlegement
* our devoted Prof. Cai
* Shen Yang(B.B.-Big Brother)


  [1]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%201.png
  [2]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%202.png
  [3]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%203.png
  [4]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%204.png
