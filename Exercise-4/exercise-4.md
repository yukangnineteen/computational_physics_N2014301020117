# Computational Physics Homework 4
***

#### Student class: 14级弘毅班
#### Student name: 余康
#### Student number: 2014301020117
***

## **1.Abstract（摘要）**
* 作业1.5

> 因为国庆放假，作业可推迟到10月9日提交

#### *1.5. Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are

![公式1](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN_B%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_A%7D%7B%5Ctau%7D%2C)

![公式2](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_B%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN_A%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_B%7D%7B%5Ctau%7D%2C)

#### where for simplicity we have assumed that the two types of decay are characterized by the same time constant, <img src="http://latex.codecogs.com/gif.latex?\tau." alt="" title="" /> Solve this system of equations for the numbers of nuclei, <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?N_B" alt="" title="" />, as functions of time. Consider different initial conditions, such as ![公式4](http://latex.codecogs.com/gif.latex?N_A%20%3D%20100%2C) ![公式5](http://latex.codecogs.com/gif.latex?N_B%20%3D%200%2C) etc., and take ![公式6](http://latex.codecogs.com/gif.latex?%5Ctau%20%3D%201) s. Show that your numerical results are consistent with the idea that the system reaches a stteady state in which <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?N_B" alt="" title="" /> are constant. In such a steady state, the time derivatives <img src="http://latex.codecogs.com/gif.latex?dN_A/dt" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?dN_B/dt" alt="" title="" /> should vanish.
***

## **2.Background（背景介绍）**
* **Double Decay:**

####　ProblemJust as the qustion-stems indicates, a better analogy for this problem would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energys. Although it is a decay problem with two types of nuclei, considering that the total number of two types of nuclei is constant, we can readily solve it in the same way as in the single decay problem.

* **The Euler Method:**

####　Still, I choose to use Euler method to deal with this problem. The principle of it, as we have all learned, is Taylor expansion. And the routine process is to substitute the given ordinary differential equation into the first-order derivative of the Taylor expansion and neglect infinitesimals of hiher order.

***

## **3.Main（正文）**
### Way of Thinking
* **An analytic approach**

　First of all, I find that in this problem A and B are completely symmetric. And another important fact is that the total number of nuclei A and B is constant, which means we can can konw either from the other. So, we can just take one of A and B as pivot element and I choose A.

![公式7](http://latex.codecogs.com/gif.latex?N%20%3D%20N_A%20&plus;%20N_B%20%3D%20N_A%280%29%20&plus;%20N_B%280%29%20%3D%20N_A%28t%29%20&plus;%20N_B%28t%29)

![公式8](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%28t%29%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN%20-%20N_A%28t%29%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_A%28t%29%7D%7B%5Ctau%7D%20%3D%20%5Cfrac%7BN%20-%202N_A%28t%29%7D%7B%5Ctau%7D)

![公式9](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%28t%29%7D%7BN%20-%202N_A%28t%29%7D%20%3D%20%5Cfrac%7Bdt%7D%7B%5Ctau%7D)

![公式10](http://latex.codecogs.com/gif.latex?-%20%5Cfrac%7B1%7D%7B2%7D%5Cln%20%7CN%20-%202N_A%28t%29%7C%20%3D%20%5Cfrac%7Bt%7D%7B%5Ctau%7D%20&plus;%20C)

　There are three situations: 

![公式11](http://latex.codecogs.com/gif.latex?N_A%28t%29%20%3E%20%5Cfrac%7BN%7D%7B2%7D)

![公式12](http://latex.codecogs.com/gif.latex?N_A%28t%29%20%3C%20%5Cfrac%7BN%7D%7B2%7D)

![公式13](http://latex.codecogs.com/gif.latex?N_A%28t%29%20%3D%20%5Cfrac%7BN%7D%7B2%7D)

　The first two situations are actually symmetric, i.e., the same, so I will only take the first situation as an example. And the third situation is s special situation.

　Considering all these, I have a solution:
 
![公式14](http://latex.codecogs.com/gif.latex?N_A%28t%29%20%3D%20%5Cfrac%7BN%7D%7B2%7D%20-%20%5Cfrac%7BN%20-%202N_A%280%29%7D%7B2%7De%5E%7B-%20%5Cfrac%7B2t%7D%7B%5Ctau%7D%7D) 

(It indeed satisfies the precoondition.)

OR

![公式15](http://latex.codecogs.com/gif.latex?N_A%28t%29%20%3D%20%5Cfrac%7BN%7D%7B2%7D)

* **A Numerical approach**

　First of all, all of our successional disscusion is based on the Taylor expansion for <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" />
 
![公式16](http://latex.codecogs.com/gif.latex?N_A%28%5CDelta%20t%29%20%3D%20N_A%280%29%20&plus;%20%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7Bd%5E2N_A%7D%7Bdt%5E2%7D%20%28%5CDelta%20t%29%5E2%20&plus;%20%5Cdots%20%2C)

　If we take ![公式17](http://latex.codecogs.com/gif.latex?%5CDelta%20t) to be small, then it is usually a good approximation to simply ignore the terms that involve second and higher powers of ![公式18](http://latex.codecogs.com/gif.latex?%5CDelta%20t), leaving us with
 
![公式19](http://latex.codecogs.com/gif.latex?N_A%28%5CDelta%20t%29%20%5Capprox%20N_A%280%29%20&plus;%20%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t)

　The same result can be obtained from the definition of a derivative. The derivative of <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" /> evaluated at time <img src="http://latex.codecogs.com/gif.latex?t" alt="" title="" /> can be written as
 
![公式20](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%7D%7Bdt%7D%20%5Cequiv%20%5Clim_%7B%5CDelta%20t%20%5Crightarrow%200%20%7D%5Cfrac%7BN_A%28t%20&plus;%20%5CDelta%20t%29%20-%20N_A%28t%29%7D%7B%5CDelta%20t%7D%20%5Capprox%20%5Cfrac%7BN_A%28t%20&plus;%20%5CDelta%20t%29%20-%20N_A%28t%29%7D%7B%5CDelta%20t%7D)

where in the last approximation we have assumed that ![公式21](http://latex.codecogs.com/gif.latex?%5CDelta%20t) is small but nonzero. We can rearrange this to obtain

![公式22](http://latex.codecogs.com/gif.latex?N_A%28t%20&plus;%20%5CDelta%20t%29%20%5Capprox%20N_A%28t%29%20&plus;%20%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t)

　From the physics of the problem we know the functional form of the derivative, and if we insert it into my last equation we obtain
 
 ![公式23](http://latex.codecogs.com/gif.latex?N_A%28t%20&plus;%20%5CDelta%20t%29%20%5Capprox%20N_A%28t%29%20&plus;%20%5Cfrac%7BN%20-%202N_A%7D%7B%5Ctau%7D%5CDelta%20t)
 
### Design of Program and Rsults

**Firstly I will show my first program which is completely imitated from Prof. Cai's sample program**

* **This is its source codes**

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(old).py)

* **This is its data file**

### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(old)%20data.txt)

* **This is its figure results**

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(old)%20figure.png)

![图像1](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(old)%20figure.png)

　　***As we see, this program is too naive!***

***

**So, here comes the improved version: I designed three situations of initial conditions**

* **Situation 1:　NA = 100,　NB = 0**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-1).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-1)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-1)%20figure.png)

![图像2](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-1)%20figure.png)

* **Situation 2:　NA = 75,　NB = 25**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-2).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-2)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-2)%20figure.png)

![图像3](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-2)%20figure.png)

* **Situation 3:　NA = 50,　NB = 50**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-3).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-3)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-3)%20figure.png)

![图像4](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-3)%20figure.png)


* **Three Situations in One Figure(for convenience of comparation)**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-4).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-4)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-4)%20figure.png)

![图像5](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-4)%20figure.png)

### Testing my program

* **Test 1: Three Different Time Steps: Time Step 1 = 0.05, Time Step 2 = 0.01, Time Step 3 = 0.1**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-5).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-5)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-5)%20figure.png)

![图像6](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-5)%20figure.png)

**Testing Results 1: The smaller time steps you choose, the bigger approximation values are**

* **Test 2: Compare Approximation Solution to the True Solution**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-6).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-6)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-6)%20figure.png)

![图像7](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-6)%20figure.png)


**Testing Results 2: In my approach, approximation values are smaller than the true values**

* **Test 3: Compare Approximation Solution to the True Solution in Different Time Steps(i.e., Combine Test 1 and Test 2)**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-7).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-7)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-7)%20figure.png)

![图像8](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-7)%20big%20figure.png)

**(Tips: I choose small x-axis limits to magnify the errors between approximation values and the true values)**

**Testing Results 3: The smaller time steps you choose, the smaller errors between approximation values and the true values are**

<br />
**Testing Results(in all): My programs are reasonable. But I have to say, there is a little trouble(especially with the true values) when the time step approaches the time constant. It may well be the arithmetic problem.**

**There are roughly two types of errors:**

* **Error 1: Time Step = 0.1, Time Constant = 0.05**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%201.py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%20data%201.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%20figure%201.png)

![图像9](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%20figure%201.png)

* **Error 2: Time Step = 0.05, Time Constant = 0.05**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%202.py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%20data%202.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%20figure%202.png)

![图像10](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-10)%20figure%202.png)

**Error Desciption: The curves gradually lose their smoothness, and the true value curve even begins to show vabrations**

**I am sorry I have no more time to explain these errors**

### Furthur Discussion and Extension

**A question occurs to me when I solved this double decay problem-"What if the time constants of two nuclei differ?" So I decide to change my programs a little bit to solve this new problem(generalization of the double decay problem)**

**There are roughly two situations:**


* **Situation 1: Time Constant A = 1, Time Constant B = 2**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-8).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-8)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-8)%20figure.png)

![图像11](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-8)%20figure.png)

* **Situation 2: Time Constant A = 2, Time Constant B = 1**

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-9).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-9)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-9)%20figure.png)

![图像12](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-9)%20figure.png)

* **Finally, I set different initial conditionals and put them in one figure(to check whehter their final numbers are the same)** 

#### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-14).py)

#### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-14)%20data.txt)

#### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-14)%20figure.png)

![图像13](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/4(improved-14).png)

**I am sorry that I skip the theoretical derivation and some theoretical proof, and omit some useful tips of plotting in python(matplotlib)**

***

## **4.Conclusion（结论）**

#### From the results of this problem and its generalization, I can draw a conclusion that the numbers of two types of nuclei will finally reach an equilibrium no matter whether the time constants of two types of nuclei are the same: And

* **If their time constants are the same, they will finally reach an equilibrium where the numbers of two types of nuclei are the same**

* **If their time constants are not the same, they will finally reach an equilibrium where the numbers of two types of nuclei are not the same. And the larger time constant one type of nuclei have, the larger the final number of them are. Besides, I also find that if their total number are the same, their final equilibrium are the same whatever the initial conditions(i.e., initial numbers) are.**

***

## **5.Acknowlegement（致谢）**
* our devoted Prof. Cai
* Stan(Tan Shan)
* Baidu(for plotting tips of python(matlotlib))










