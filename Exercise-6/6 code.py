#The sixth homework of computational physics by Prof. Cai.
#Units of physical quantities are in SI.
#Assume that  the temperature of sea level is 273K.
import pylab as pl
import math

class targeted_baseball:
    def __init__(self, initial_velocity, firing_angle, time_step, velocity_of_wind, angle_of_wind):
        self.x = [0]
        self.y = [0]
        self.theta = firing_angle
        self.alpha = angle_of_wind
        self.v_x = [initial_velocity * math.cos(self.theta / 180 * math.pi)]
        self.v_y = [initial_velocity * math.sin(self.theta / 180 * math.pi)]
        self.v0 = initial_velocity
        self.v = initial_velocity
        self.v_w = velocity_of_wind
        self.v_w_x = self.v_w * math.cos(self.alpha / 180 * math.pi)
        self.v_w_y = self.v_w * math.sin(self.alpha / 180 * math.pi)
        self.v_rel_x = self.v_x[0] - self.v_w_x
        self.v_rel_y = self.v_y[0] - self.v_w_y
        self.v_rel_module = math.hypot(self.v_rel_x, self.v_rel_y)
        self.C = 0
        self.B_2 = 0
        self.g = 9.8
        self.dt = time_step
        
    def calculate(self):
        i = 0
        while(True):
            self.B_2 = 0.0039 + 0.0058 / (1 + math.exp((self.v - 35) / 5))
            self.C = math.pow(1 - 0.0065 * self.y[i] / 273, 2.5)
            self.x.append(self.x[i] + self.v_x[i] * self.dt)
            self.y.append(self.y[i] + self.v_y[i] * self.dt)
            self.v_x.append(self.v_x[i] - self.C * self.B_2 * self.v_rel_module * self.v_rel_x * self.dt)
            self.v_y.append(self.v_y[i] - self.g * self.dt - self.C * self.B_2 * self.v_rel_module * self.v_rel_y * self.dt)
            self.v = math.hypot(self.v_x[i + 1], self.v_y[i + 1])
            self.v_rel_x = self.v_x[i + 1] - self.v_w_x
            self.v_rel_y = self.v_y[i + 1] - self.v_w_y
            self.v_rel_module = math.hypot(self.v_rel_x, self.v_rel_y)
            i += 1
            if self.y[i] <= -100:
                break
        self.x[-1]=((-100 - self.y[-1])*(self.x[-1] - self.x[-2]) / (self.y[-1] - self.y[-2])) + self.x[-1]
        self.y[i] = -100
        global a
        a = self.x[-1]

    def show_complex(self):
        font = {'family': 'serif',
                'color':  'k',
                'weight': 'normal',
                'size': 16,
        }
        pl.title('The Trajectory of Tageted Baseball\n with air flow in adiabatic model', fontdict = font)
        pl.plot(self.x, self.y, label = '$v_0 = %.5f m/s$'%self.v0 + ', ' + '$\\theta = %.4f \degree$'%self.theta)
        pl.xlabel('x $m$')
        pl.ylabel('y $m$')
        pl.xlim(0, 300)
        pl.ylim(-100, 20)
        pl.grid()
        pl.legend(loc = 'upper right', shadow = True, fontsize = 'small')
        pl.text(15, -90, 'scan to approach the minimum velocity and corresponding launching angle', fontdict = font)
        pl.show()
        
    def show_simple(self):
        font = {'family': 'serif',
                'color':  'k',
                'weight': 'normal',
                'size': 16,
        }
        pl.title('The Trajectory of Tageted Baseball\n with air flow in adiabatic model', fontdict = font)
        pl.plot(self.x, self.y, label ='$\\alpha = %.0f \degree$'%self.alpha)
        pl.xlabel('x $m$')
        pl.ylabel('y $m$')
        pl.xlim(0, 400)
        pl.ylim(-100, 200)
        pl.grid()
        pl.legend(loc = 'upper right', shadow = True, fontsize = 'medium')
        pl.text(5, -80, 'trojectories varing with angles of wind', fontdict = font)
        pl.show()


class plotting():
    def single_plot(self):
        t = targeted_baseball(110, 45, 0.01, 10, 135)
        t.calculate()
        t.show_complex()
    
    def multiple_plot(self):
        variable_alpha = 85
        while 85 <= variable_alpha <= 95 :
            t = targeted_baseball(110, 45, 0.01, 10, variable_alpha)
            t.calculate()
            t.show_simple()
            variable_alpha += 1
            
            
            

            
class why_inherit:
    def nothing(self):
        print('Why do I need to inherit class?')



class explore_minimum_velocity():
    def double_scan(self):
        v_0 = 81.09589
        while 0 <= v_0:
            theta_0 = 7.1610
            while 7.1610 <= theta_0 < 7.1620:
                t = targeted_baseball(v_0, theta_0, 0.01, 10, 135)
                t.calculate()
                t.show()
                if a < 220:
                    theta_0 = theta_0 + 0.0001
                else:
                    print(a, '\n', v_0,'\n', theta_0)
                    break
            v_0 = v_0 + 0.00001
            if a >= 220:
                break

        
      
            

        
        

        

        
        















