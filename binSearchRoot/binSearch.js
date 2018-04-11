'''
二分搜索求解零点
f(x)=2*sin(x)-x=0
由于f(x)奇函数，且由准备工作中确定的零点范围，设定求解区间[1.5, 2.5]
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

plt.style.use('dark_background')

fig, ax = plt.subplots()
dots, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(1.3, 2.7)
    ax.set_ylim(-2, 2)    
    x = np.linspace(1.5, 2.5)
    y = 2*np.sin(x)-x
    l = ax.plot(x, y, color='g')
    return l

def gen_dots(err):
    l = 1.5
    r = 2.5
    newdot = np.zeros([2,3], order='C')
    newdot[0][0]=l
    newdot[0][1]=(l+r)/2
    newdot[0][2]=r
    newdot[1] = 2*np.sin(newdot[0])-newdot[0]
    print(newdot)
    yield newdot
    while(newdot[1][1]!=0 and r-l>err):
        if(newdot[1][1]*newdot[1][0]>0):
            l = newdot[0][1]
            newdot[0][0] = newdot[0][1]
        else:
            r = newdot[0][1]
            newdot[0][2] = newdot[0][1]
        newdot[0][1] = (l+r)/2
        newdot[1] = 2*np.sin(newdot[0])-newdot[0]
        
        yield newdot
    print("1")
    

def update_dots(newd):
    dots.set_data(newd[0], newd[1])
    return dots
            
ani = animation.FuncAnimation(fig, update_dots, frames = gen_dots(0.01), interval=1000, init_func = init)
plt.show()


