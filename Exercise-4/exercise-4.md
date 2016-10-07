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
* An analytic approach

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

* A Numerical approach

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

* Firstly I will show my first program which is completely imitated from Prof. Cai's sample program
### [Code: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204(old).py)

```python
import pylab as pl
class nuclei_decay:
    """
    Simulation of a decay problem with two types of nuclei
    Program to solve Chapter 1 Exercise *1.5. of 'Computational Physics' by Prof. Cai
    """
    def __init__(self, number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05 ):
        self.n_A = [number_of_nuclei_A]
        self.n_B = [number_of_nuclei_B]
        self.N = number_of_nuclei_A + number_of_nuclei_B
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei A ->", number_of_nuclei_A)
        print("Initial number of nuclei B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("Time step ->", time_step)
        print("Total time ->", time_of_duration)

    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.n_A[i] + (self.N - 2 * self.n_A[i]) / self.tau * self.dt
            tmp_B = self.N - tmp_A
            self.n_A.append(tmp_A)
            self.n_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
           
    def show_results(self):
        pl.plot(self.t, self.n_A)
        pl.plot(self.t, self.n_B)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        
    def store_results(self):
        myfile = open('computational_physics homework 4 data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_A[i], self.n_B[i], file = myfile)
        myfile.close()

#matplotlib inline
a = nuclei_decay()
a.calculate()
a.show_results()
a.store_results()
```

* This is its data file
### [Data: Please Click Here](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204%20data(old).txt)

> 0 100 0
0.05 95.0 5.0
0.1 90.5 9.5
0.15000000000000002 86.45 13.549999999999997
0.2 82.805 17.194999999999993
0.25 79.5245 20.475499999999997
0.3 76.57205 23.427949999999996
0.35 73.914845 26.085155
0.39999999999999997 71.5233605 28.476639500000005
0.44999999999999996 69.37102445 30.628975550000007
0.49999999999999994 67.433922005 32.566077995
0.5499999999999999 65.6905298045 34.3094701955
0.6 64.12147682405 35.878523175949994
0.65 62.70932914164501 37.29067085835499
0.7000000000000001 61.43839622748051 38.56160377251949
0.7500000000000001 60.294556604732456 39.705443395267544
0.8000000000000002 59.26510094425921 40.73489905574079
0.8500000000000002 58.33859084983329 41.66140915016671
0.9000000000000002 57.50473176484996 42.49526823515004
0.9500000000000003 56.75425858836496 43.24574141163504
1.0000000000000002 56.078832729528465 43.921167270471535
1.0500000000000003 55.47094945657562 44.52905054342438
1.1000000000000003 54.923854510918055 45.076145489081945
1.1500000000000004 54.43146905982625 45.56853094017375
1.2000000000000004 53.988322153843626 46.011677846156374
1.2500000000000004 53.589489938459266 46.410510061540734
1.3000000000000005 53.23054094461334 46.76945905538666
1.3500000000000005 52.907486850152004 47.092513149847996
1.4000000000000006 52.6167381651368 47.3832618348632
1.4500000000000006 52.355064348623124 47.644935651376876
1.5000000000000007 52.119557913760815 47.880442086239185
1.5500000000000007 51.90760212238473 48.09239787761527
1.6000000000000008 51.71684191014626 48.28315808985374
1.6500000000000008 51.54515771913163 48.45484228086837
1.7000000000000008 51.39064194721847 48.60935805278153
1.7500000000000009 51.25157775249662 48.74842224750338
1.800000000000001 51.12641997724696 48.87358002275304
1.850000000000001 51.01377797952227 48.98622202047773
1.900000000000001 50.91240018157004 49.08759981842996
1.950000000000001 50.82116016341304 49.17883983658696
2.000000000000001 50.73904414707174 49.26095585292826
2.0500000000000007 50.665139732364565 49.334860267635435
2.1000000000000005 50.59862575912811 49.40137424087189
2.1500000000000004 50.5387631832153 49.4612368167847
2.2 50.484886864893774 49.515113135106226
2.25 50.436398178404396 49.563601821595604
2.3 50.39275836056396 49.60724163943604
2.3499999999999996 50.35348252450756 49.64651747549244
2.3999999999999995 50.31813427205681 49.68186572794319
2.4499999999999993 50.286320844851126 49.713679155148874
2.499999999999999 50.257688760366015 49.742311239633985
2.549999999999999 50.231919884329415 49.768080115670585
2.5999999999999988 50.20872789589647 49.79127210410353
2.6499999999999986 50.18785510630683 49.81214489369317
2.6999999999999984 50.16906959567614 49.83093040432386
2.7499999999999982 50.15216263610853 49.84783736389147
2.799999999999998 50.136946372497675 49.863053627502325
2.849999999999998 50.123251735247905 49.876748264752095
2.8999999999999977 50.11092656172311 49.88907343827689
2.9499999999999975 50.0998339055508 49.9001660944492
2.9999999999999973 50.089850514995724 49.910149485004276
3.049999999999997 50.08086546349615 49.91913453650385
3.099999999999997 50.072778917146536 49.927221082853464
3.149999999999997 50.065501025431885 49.934498974568115
3.1999999999999966 50.0589509228887 49.9410490771113
3.2499999999999964 50.05305583059983 49.94694416940017
3.2999999999999963 50.047750247539845 49.952249752460155
3.349999999999996 50.04297522278586 49.95702477721414
3.399999999999996 50.03867770050728 49.96132229949272
3.4499999999999957 50.034809930456554 49.965190069543446
3.4999999999999956 50.0313289374109 49.9686710625891
3.5499999999999954 50.02819604366981 49.97180395633019
3.599999999999995 50.025376439302825 49.974623560697175
3.649999999999995 50.02283879537254 49.97716120462746
3.699999999999995 50.02055491583529 49.97944508416471
3.7499999999999947 50.018499424251765 49.981500575748235
3.7999999999999945 50.01664948182659 49.98335051817341
3.8499999999999943 50.01498453364393 49.98501546635607
3.899999999999994 50.01348608027954 49.98651391972046
3.949999999999994 50.01213747225159 49.98786252774841
3.999999999999994 50.01092372502643 49.98907627497357
4.049999999999994 50.00983135252379 49.99016864747621
4.099999999999993 50.008848217271414 49.991151782728586
4.149999999999993 50.00796339554427 49.99203660445573
4.199999999999993 50.00716705598985 49.99283294401015
4.249999999999993 50.006450350390864 49.993549649609136
4.299999999999993 50.00580531535178 49.99419468464822
4.3499999999999925 50.0052247838166 49.9947752161834
4.399999999999992 50.00470230543494 49.99529769456506
4.449999999999992 50.00423207489145 49.99576792510855
4.499999999999992 50.003808867402306 49.996191132597694
4.549999999999992 50.003427980662075 49.996572019337925
4.599999999999992 50.00308518259587 49.99691481740413
4.6499999999999915 50.00277666433628 49.99722333566372
4.699999999999991 50.002498997902656 49.997501002097344
4.749999999999991 50.00224909811239 49.99775090188761
4.799999999999991 50.00202418830115 49.99797581169885
4.849999999999991 50.001821769471036 49.998178230528964
4.899999999999991 50.00163959252393 49.99836040747607
4.94999999999999 50.00147563327154 49.99852436672846
4.99999999999999 50.001328069944385 49.998671930055615

* This is its figure results
### [Figure](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204(old).png)

![图像1](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-4/computational_physics%20homework%204(old).png)





　














