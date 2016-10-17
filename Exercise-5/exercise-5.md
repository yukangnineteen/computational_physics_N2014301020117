# Computational Physics Homework 5
***

#### Student class: 14 Hong Yi
#### Student name: Kang Yu
#### Student number: 2014301020117
***
# Computational Physics Homework 5


----------


## **1.Abstract**
> 抱歉作业更新晚了！2.2章作业任选一题。

#### Exercises
#### 2.8. In our model of the cannon shell trajectory we have assumed that the acceleration due to gravity, $g$, is a constant. It will, of course, depend on altitude. Add this to the model and calculate how much it affects the range.

#### 2.9. Calculate the trajectory of of our cannon shell including both air drag and the reduced air density at high altitudes so that you can reproduce the results in Figure 2.5. Perform your calculation for different firing angles and determine the value of the angle that gives the maximum range.

#### All in all, what I would like to do is to explore the effects of $g$'s independence on altitude, air drag and the reduced air density on the cannon shell trajectory.


----------


## **2.Background**
* **Projectile Motion**

#### On this topic, we have learned too much about it from our junior high schools to senior high schools, so I have nothing special to say.

* **gravitational acceleration**

#### In our problems, we will need to use the relation between $g$ and altitude:
\begin{equation}
g(y) = GM_E\frac{1}{(R_E + y) ^ 2}
\end{equation}
#### where $M_E$ is the mass of the Earth, $R_E$ is the average radius of the Earth, and $y$ is the distance between the cannon shell and the surface of the Earth.

* **air drag**

#### According to our textbook, it is not difficult to find by energy relation that:
\begin{equation}
F_{drag} \approx - \frac{1}{2}C\rho Av ^ 2
\end{equation}
#### where $C$ is known as the drag coefficient, and can be simply assumed to be $1$. To be more simplified, we have:
\begin{equation}
F_{drag} = - B_2 v ^ 2
\end{equation}
#### What really matters is that $B_2$ is proportional to $\rho$. So:
\begin{equation}
F^*_{drag} = \frac{\rho}{\rho_0}F_{drag}(y=0)
\end{equation}

* **air density**

**1.Isothermal model**

#### From our Thermaldynamics and Statistical Physics course, we have a conclusion :
\begin{equation}
\rho = \rho_0 exp(- y / y_0)
\end{equation}
#### where $y_0 = k_BT/mg \approx 1.0 × 10 ^ 4m$, and $\rho_0$ is density at sea level ($y = 0$).

#### From this and what I have emphasized before, we have:
\begin{equation}
F^*_{drag} = exp(- y / y_0)F_{drag}
\end{equation}

**2.Adiabatic model**

#### In the same way, we have a conclusion:
\begin{equation}
\rho = \rho_0 (1 - \frac{ay}{T_0}) ^ \alpha
\end{equation}
#### where $a \approx 6.5 K/km$, $T_0$ is the sea level temperature (in K), and the exponent $\alpha \approx 2.5$ for air.

#### From this and what I have emphasized before, we have:
\begin{equation}
F^*_{drag} = (1 - \frac{ay}{T_0}) ^ \alpha F_{drag}
\end{equation}


----------
## **3.Main**
### I still choose to use the dirty and quick method - The Euler Mehtod (So no more illumination is to be made) 

### Design of Program and Result (Declaration: The unit of distance is $km$, and other units are in SI)

**Firstly, I take air drag as a commom premise. This is the trojectory of cannon shell only affected by air drag**

#### **Codes**:
```python
import pylab as pl
import math
class cannon_shell:
    def __init__(self, B_2_over_mass = 4 * 10 ** (- 2), time_step = 0.1, initial_velocity = 0.7, gravitational_acceleration = 9.8 * 10 ** (-3), firing_angle = float(input("Please input the launch angle:")) * math.pi / 180):
        self.x = [0]
        self.y = [0]
        self.theta = firing_angle
        self.v = [initial_velocity]
        self.v_x = [self.v[0] * math.cos(self.theta)]
        self.v_y = [self.v[0] * math.sin(self.theta)]
        self.t = [0]
        self.c = B_2_over_mass
        self.g = gravitational_acceleration
        self.dt = time_step

    def run(self):
        while(self.y[-1] >= 0):
            self.x.append(self.x[-1] + self.v_x[-1] * self.dt)
            self.y.append(self.y[-1] + self.v_y[-1] * self.dt)
            self.v_x.append(self.v_x[-1] - self.c * self.v[-1] * self.v_x[-1] * self.dt)
            self.v_y.append(self.v_y[-1] - self.g * self.dt - self.c * self.v[-1] * self.v_y[-1] * self.dt)
            self.v.append(math.sqrt(self.v_x[-1] ** 2 + self.v_y[-1] ** 2))
        else:
            r = - self.y[-1] / self.y[-2]
            x_l = (self.x[-2] + r * self.x[-1]) / (r + 1)
            y_l = 0
            self.x[-1] = x_l
            self.y[-1] = y_l
            print("The fall point of the cannon shell is: x =",x_l)

    def show_results(self):
        font = {'family': 'serif',
                'color':  'k',
                'weight': 'normal',
                'size': 14,
        }
        pl.plot(self.x, self.y, 'c', label='firing angle = 45°')
        pl.title('The Trajectory of a Cannon Shell', fontdict = font)
        pl.xlabel('x (k$m$)')
        pl.ylabel('y ($km$)')
        pl.xlim(0, 60)
        pl.ylim(0, 20)
        pl.grid(True)
        pl.legend(loc='upper right', shadow=True, fontsize='large')
        pl.text(41, 16, 'Only with air drag', fontdict = font)
        pl.show()

a = cannon_shell()
a.run()
a.show_results()
```

#### **Figure:**
![!\[Figure1\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%201.png)][1]

**Secondly, (only) add the reduced air density - isothermal**

#### **Codes: (I will only show the parts that I have made some sigificant changes)**
```
python
self.v_x.append(self.v_x[-1] - math.exp(- self.y[-1] / self.y_0) * self.c * self.v[-1] * self.v_x[-1] * self.dt)
self.v_y.append(self.v_y[-1] - self.g * self.dt - self.c * self.v[-1] * math.exp(- self.y[-1] / self.y_0) * self.v_y[-1] * self.dt)
```

#### **Figure:**
![!\[Figure2\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%202.png)][2]


**Thirdly, (only) add the reduced air density - adiabatic**

#### **Codes:**
```
python
self.v_x.append(self.v_x[-1] - (1 - self.a * self.y[-1] / self.T_0) ** self.alpha * self.c * self.v[-1] * self.v_x[-1] * self.dt)
self.v_y.append(self.v_y[-1] - self.g * self.dt - (1 - self.a * self.y[-1] / self.T_0) ** self.alpha * self.c * self.v[-1] * self.v_y[-1] * self.dt)
```

#### **Figure:**
![!\[Figure3\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%203.png)][3]


**Fourthly, (only) add the $g$'s independence on altitude**

#### **Codes:**
```
python
self.v_y.append(self.v_y[-1] - self.G * self.ME * (self.RE + self.y[-1]) ** (- 2) * self.dt - self.c * self.v[-1] * self.v_y[-1] * self.dt)
```

#### **Figure:**
![!\[Figure4\](https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%204.png)][4]



----------
## 4.Conclusion
#### I am sorry I fail to write smoothly in Cmd Markdown.



----------
## 5.Acknowlegement
* our devoted Prof. Cai
* Shen Yang(B.B.-Big Brother)


  [1]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%201.png
  [2]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%202.png
  [3]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%203.png
  [4]: https://github.com/yukangnineteen/computational_physics_N2014301020117/blob/master/Exercise-5/5%20figure%204.png
