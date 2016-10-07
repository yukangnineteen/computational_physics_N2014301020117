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

![公式1](http://latex.codecogs.com/gif.latex?dN_A%20%3D%20%5Cfrac%7BN_B%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_A%7D%7B%5Ctau%7D%2C)

![公式2](http://latex.codecogs.com/gif.latex?dN_B%20%3D%20%5Cfrac%7BN_A%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_B%7D%7B%5Ctau%7D%2C)

#### where for simplicity we have assumed that the two types of decay are characterized by the same time constant, <img src="http://latex.codecogs.com/gif.latex?\tau." alt="" title="" /> Solve this system of equations for the numbers of nuclei, <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?N_B" alt="" title="" />, as functions of time. Consider different initial conditions, such as ![公式4](http://latex.codecogs.com/gif.latex?N_A%20%3D%20100%2C) ![公式5](http://latex.codecogs.com/gif.latex?N_B%20%3D%200%2C) etc., and take ![公式6](http://latex.codecogs.com/gif.latex?%5Ctau%20%3D%201) s. Show that your numerical results are consistent with the idea that the system reaches a stteady state in which <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?N_B" alt="" title="" /> are constant. In such a steady state, the time derivatives <img src="http://latex.codecogs.com/gif.latex?dN_A/dt" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?dN_B/dt" alt="" title="" /> should vanish.
***

## **2.Background（背景介绍）**
* 　Double Decay:

　ProblemJust as the qustion-stems indicates, a better analogy for this problem would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energys. Although it is a decay problem with two types of nuclei, considering that the total number of two types of nuclei is constant, we can readily solve it in the same way as in the single decay problem.

* 　The Euler Method:

　Still, I choose to use Euler method to deal with this problem. The principle of it, as we have all learned, is Taylor expansion. And the routine process is to substitute the given ordinary differential equation into the first-order derivative of the Taylor expansion and neglect infinitesimals of hiher order.

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
 
![公式14](http://latex.codecogs.com/gif.latex?N_A%28t%29%20%3D%20%5Cfrac%7BN%7D%7B2%7D%20&plus;%20%5Cfrac%7BN%20-%202N_A%28t%29%7D%7B2%7De%5E%7B-%20%5Cfrac%7B2t%7D%7B%5Ctau%7D%7D) 

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
 
### Design of Program

* **Firstly I will show my first program which is completely imitated from Prof. Cai's sample program**

### [　　Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204(old).py)

* **This is its data file**

### [　　Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204%20data(old).txt)

* **This is its figure results**

### [　　Figure: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204(old).png)

![图像1](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204(old).png)

　　***As we see, this program is too naive!***

***

* **So, here comes the improved version**







　














