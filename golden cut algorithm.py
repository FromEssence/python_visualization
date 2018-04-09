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

plt.style.use('ggplot')

fig, ax = plt.subplots()
dots, = ax.plot([], [], 'ro')


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
    newdot[0][1] = s+(t-s)*0.328
    newdot[0][3] = t
    newdot[0][2] = s+(t-s)*0.612
    newdot[1] = np.cos(newdot[0])
    print("yeild")
    yield newdot
def update_dots(newd):
    dots.set_data(newd[0], newd[1])
    return dots
    
ani = animation.FuncAnimation(fig, update_dots, frames = gen_dots, interval=5000, init_func=init, repeat=False)
plt.show()



