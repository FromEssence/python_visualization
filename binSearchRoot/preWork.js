'''
二分搜索求解零点
2*sin(x)-x=0
将两个函数图像画在一起判断零点所在区间
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

plt.style.use('ggplot')

fig, ax = plt.subplots()

x1 = np.linspace(-1, 2*np.pi, 100)
y1 = 2*np.sin(x1)
x2 = np.linspace(-1, 2*np.pi, 100)
y2 = np.linspace(-1, 2*np.pi, 100)
ax.plot(x1, y1, color='g')
ax.plot(x2, y2)


plt.show()

