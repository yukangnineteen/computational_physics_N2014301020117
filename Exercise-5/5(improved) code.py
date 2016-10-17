#Learn from the BigBrother(B.B.)
import pylab as pl
import math
pl.ion()
#Initialize and calculate
class cannon_shell:
    def __init__(self, initial_velocity = 0, firing_angle = 0, time_step = 0):
        self.x = [0]
        self.y = [0]
        self.theta = firing_angle
        self.v_x = [initial_velocity * math.cos(self.theta / 180 * math.pi) / 1000]
        self.v_y = [initial_velocity * math.sin(self.theta / 180 * math.pi) / 1000]
        self.dt = time_step
        self.C = 0
        self.G = 6.67E-20
        self.M_E = 5.98E+24
        self.R_E = 6371
        self.g = []
        
    def calculate(self):
        i = 0
        while(True):
            self.C = 4E-2 * math.pow(1 - 6.5 * self.y[i] / 300, 2.5)
            self.g.append(self.G * self.M_E / (self.R_E + self.y[i]) ** 2)
            self.x.append(self.x[i] + self.v_x[i] * self.dt)
            self.y.append(self.y[i] + self.v_y[i] * self.dt)
            self.v_x.append(self.v_x[i] - self.C * math.hypot(self.v_x[i], self.v_y[i]) * self.v_x[i] * self.dt)
            self.v_y.append(self.v_y[i] - self.g[i-1] * self.dt - self.C * math.hypot(self.v_x[i], self.v_y[i]) * self.v_y[i] * self.dt)
            i += 1
            if self.y[i] < 0:
                break
#For the falling point
        self.x[i] = - self.y[i-1] * (self.x[i] - self.x[i-1]) / (self.y[i] - self.y[i-1]) + self.x[i-1]
        self.y[i] = 0

#Maxmize the range and find the corresponding firing angle
class extreme_problem(cannon_shell):
    def maxmize(self):
        max_range = 0
        tmp_max = 0
        theta = 0
        print("\n===============")
        print("Calculating, please wait a moment...︿(￣︶￣)︿\n")
        while(True):
            cannon_shell.__init__(self, _input.initial_velocity, theta, _input.time_step)
            cannon_shell.calculate(self)
            tmp_max = self.x[-1]
            if (max_range <= tmp_max):
                max_range = tmp_max
                theta += 0.1
            else:
                theta -= 0.1
                break
        print("initial velocity:", _input.initial_velocity, "m/s")
        print("time step:", _input.time_step, "s")
        print("maximum firing range: %.4f km"%max_range)
        print("corresponding firing angle: %.1f°."%theta, "\n")
        
#Plot the projectory
class show_results:
    def show_results_prepare(self):
        font = {'family': 'serif',
                'color':  'k',
                'weight': 'normal',
                'size': 13,
        }
        pl.figure(1)
        pl.title('The Trajectory of Cannon Shells', fontdict = font)
        pl.xlabel('x / $km$')
        pl.ylabel('y / $km$')
        pl.xlim(0, 60)
        pl.ylim(0, 20)
        pl.grid(True)
        pl.text(2, 16.5, 'With air drag, the reduced air density \n        and g varying with altitudes', fontdict = font)
        pl.show()
        
    def show_results_plot(self):
        pl.figure(1)
        pl.plot(self.x, self.y,label = "firing angle = %.1f °"%self.theta)
        pl.draw()
        pl.legend(loc='upper right', shadow=True, fontsize='small')
        print("\n initial velocity:", _input.initial_velocity, "m/s")
        print("time step:", _input.time_step, "s")
        print("firing angle:", self.theta, "°")
        print("falling fange:%.4f km"%self.x[-1], "\n")
        
#Users input the initial values 
class _input:
    initial_input = input("Please input initial velocity（m/s) and time step（s）, taking care to seperate the two values with a blank space: o(*^＠^*)o \n")
    initial_value = [float(n) for n in initial_input.split()]
    initial_velocity = initial_value[0]
    time_step = initial_value[1]

#Plotting in respond to the inputted by users
class _output:
    c = cannon_shell()
    show_results.show_results_prepare(c)
    while(True):
        firing_angle = float(input("=============== \nPlease input firing angle value（in degree measure，0 ~ 180）（If you input 666, maximum firing range will be calculated）: o(*^＠^*)o \n"))
        if firing_angle != 666:
            c = cannon_shell(_input.initial_velocity, firing_angle, _input.time_step)
            c.calculate()
            show_results.show_results_plot(c)
        else:
            break
    e = extreme_problem(_input.initial_velocity, firing_angle, _input.time_step)
    e.maxmize()
    
#Run the programm
_input()
_output()
end = input("\n\n\nPush enter to close the program...ヾ(￣▽￣)Bye~Bye~")