import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

from scipy.stats import norm

##
n_points = 500
size = 400
delta = 5
dt = .8
##

x = np.zeros(n_points)
y = np.zeros(n_points)

fig, ax = plt.subplots()

points, = ax.plot(x, y, 'o', c="#1374ff")


def init_motion():
    ax.set_xlim([-size, size])
    ax.set_ylim([-size, size])

    ax.axis("off")
#    ax.set_title('Brownian motion')

    return points,


def motion(frame):
    global x, y
    dx = np.random.randn(n_points) * (delta**2 * dt)
    dy = np.random.randn(n_points) * (delta**2 * dt)

    x += dx 
    y += dy

    # bounce at boundaries
    idx = np.where(x >= size)
    x[idx] = size - abs(x[idx] - size)
    idx = np.where(y >= size)
    y[idx] = size - abs(y[idx] - size)

    points.set_data(x, y)
    return points,


animation = FuncAnimation(
    fig,
    motion,
    interval=1,
    init_func=init_motion,
    blit=True
    )

# plt.show()
animation.save("brownian_motion.gif", writer="imagemagick")
