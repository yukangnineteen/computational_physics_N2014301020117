import math
import pylab as pl
import numpy as np
# import modules above
l=9.8
g=9.8
# define constants above
class Chaos:
    def __init__(self,Fd=1.2,OmegaD=2./3,q=0.5,theta0=0.2,omega0=0,time=1000,step=1000):
        self.Fd=Fd
        self.OmegaD=OmegaD
        self.theta0=theta0
        self.omega0=omega0
        self.step=step
        self.cycle=2*math.pi/OmegaD
        self.dt=self.cycle/step
        self.time=time
        self.Theta=[self.theta0]
        self.originTheta=[self.theta0]
        self.Omega=[self.omega0]
        self.T=[0]
        self.q=q
        return None
    def sway(self):
        while not self.T[-1]>self.time:
            newOmega=self.Omega[-1]+(-math.sin(self.Theta[-1])-self.q*self.Omega[-1]+self.Fd*math.sin(self.OmegaD*self.T[-1]))*self.dt
            self.Omega.append(newOmega)
            newTheta=self.Theta[-1]+newOmega*self.dt
            self.originTheta.append(newTheta)
            if newTheta<-math.pi:
                newTheta=newTheta+2*math.pi
            if newTheta>math.pi:
                newTheta=newTheta-2*math.pi
            self.Theta.append(newTheta)
            newT=self.T[-1]+self.dt
            self.T.append(newT)
        return 0
    def plotTheta(self,style='black',slogan=''):
        pl.title(r"$\theta$ v.s. Time")
        pl.xlabel('Time [s]')
        pl.ylabel(r'$\theta\quad [rad]$')
        pl.xlim(min(self.T),max(self.T))
        pl.ylim(-4,4)
        pl.yticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
        pl.plot(self.T,self.Theta,style,label=slogan)
        return 0
    def plotPhase(self,color='black',slogan=''):
        pl.title("Phase Trajectory")
        pl.xlabel(r'$\theta$ [rad]')
        pl.ylabel(r'$\omega$ [$s^{-1}$]')
        pl.xlim(-4,4)
        pl.xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
        pl.scatter(self.Theta,self.Omega,s=0.5,c=color,label=slogan)
        return 0        
    def PoincareSection(self,init,color,slogan):
        "init is a value from zero to one"
        n=int(self.time//self.cycle)
        PoincareTheta=[]
        PoincareOmega=[]
        for i in range(n):
            PoincareTheta.append(self.Theta[int((i+init)*self.step)])
            PoincareOmega.append(self.Omega[int((i+init)*self.step)])
        pl.scatter(PoincareTheta,PoincareOmega,s=0.5,c=color,label=slogan)
        return 0
def bifurcation(init=0,F_D=1.2,frequency=2./3,friction=0.5,color='black',slogan=''):
    B=Chaos(Fd=F_D,OmegaD=frequency,q=friction,time=400*2*math.pi/frequency,)
    B.sway()
    bifurcationTheta=[]
    for i in range(100):
        bifurcationTheta.append(B.Theta[(300+i+init)*B.step])
    bifurcationFd=[F_D]*len(bifurcationTheta)   
    return (bifurcationFd,bifurcationTheta)

fd=[]
theta=[]
for i4 in np.arange(1.5,3.,0.01):
    som=bifurcation(F_D=i4,frequency=4./3)
    fd.extend(som[0])
    theta.extend(som[1])
pl.subplot(224)
pl.scatter(fd,theta,s=0.1,c='black',label=r'$\Omega_D=4/3$')
pl.legend(loc='upper right',frameon=False)