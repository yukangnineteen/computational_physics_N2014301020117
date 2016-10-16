import pylab as pl
import math
class cannon_shell:
    def __init__(self, a = 6.5, alpha = 2.5, sea_level_temperature = 300, B_2_over_mass = 4 * 10 ** (- 2), time_step = 0.1, initial_velocity = 0.7, gravitational_acceleration = 9.8 * 10 ** (-3), firing_angle = float(input("Please input the launch angle:")) * math.pi / 180):
        self.x = [0]
        self.y = [0]
        self.theta = firing_angle
        self.v = [initial_velocity]
        self.v_x = [self.v[0] * math.cos(self.theta)]
        self.v_y = [self.v[0] * math.sin(self.theta)]
        self.t = [0]
        self.c = B_2_over_mass
        self.a = a
        self.alpha = alpha
        self.T_0 = sea_level_temperature
        self.g = gravitational_acceleration
        self.dt = time_step
        
    def run(self):
        while(self.y[-1] >= 0):
            self.x.append(self.x[-1] + self.v_x[-1] * self.dt)
            self.y.append(self.y[-1] + self.v_y[-1] * self.dt)
            self.v_x.append(self.v_x[-1] - (1 - self.a * self.y[-1] / self.T_0) ** self.alpha * self.c * self.v[-1] * self.v_x[-1] * self.dt)
            self.v_y.append(self.v_y[-1] - self.g * self.dt - (1 - self.a * self.y[-1] / self.T_0) ** self.alpha * self.c * self.v[-1] * self.v_y[-1] * self.dt)
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
                'size': 12,
        }
        pl.plot(self.x, self.y, 'c', label='firing angle = 45°')
        pl.title('The Trajectory of a Cannon Shell', fontdict = font)
        pl.xlabel('x (k$m$)')
        pl.ylabel('y ($km$)')
        pl.xlim(0, 60)
        pl.ylim(0, 20)
        pl.grid(True)
        pl.legend(loc='upper right', shadow=True, fontsize='large')
        pl.text(34.5, 16, '       With both air drag and \n reduced air density-adiabatic', fontdict = font)
        pl.show()

a = cannon_shell()
a.run()
a.show_results()