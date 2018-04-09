"""
黄金分割搜索算法
求解函数 y = cos(x), x in [-PI/2, PI/2]
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.lines import Line2D
import math
import matplotlib.pyplot as plt

plt.style.use('dark_background')

fig, ax = plt.subplots()
dots, = ax.plot([], [], 'ro')
err = 0.01

def init():
    ax.set_xlim(-0.5*np.pi-1, 0.5*np.pi+1)
    ax.set_ylim(-1, 1.5)

    x = np.linspace(-0.5*np.pi, 0.5*np.pi, 100)
    y = np.cos(x)
    l = ax.plot(x, y, color='g')
    return l

def gen_dots():
    s = -0.5*np.pi
    t = 0.5*np.pi
    newdot = np.empty([2, 4], order='C')
    
    newdot[0][0] =s
    newdot[0][1] = s+(t-s)*0.382
    newdot[0][2] = s+(t-s)*0.618
    newdot[0][3] = t
    newdot[1] = np.cos(newdot[0])
    while (t-s>err):
        yield newdot
        if(newdot[1][1]>newdot[1][2]):
            t = newdot[0][2]
            newdot[0][3] = t
            newdot[0][2] = newdot[0][1]
            newdot[0][1] = s+(t-s)*0.382
            newdot[1] = np.cos(newdot[0])
        else:
            s = newdot[0][1]
            newdot[0][0] = s
            newdot[0][1] = newdot[0][2]
            newdot[0][2] = s+(t-s)*0.618
            newdot[1] = np.cos(newdot[0])
        #print("yield")
        
def update_dots(newd):
    dots.set_data(newd[0], newd[1])
    ax.set_xlim(newd[0][0]-0.5, newd[0][3]+0.5) #动态更改X坐标轴范围，点更清晰，但是每次是哪个点变化就看不清了
    return dots
    
ani = animation.FuncAnimation(fig, update_dots, frames = gen_dots, interval=2000, init_func=init, repeat=False)
plt.show()



