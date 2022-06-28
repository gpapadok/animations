import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np 

# number of periods
n_t = 10

# message
A_m = 2
w_m = .5
phi = 0

# carrier
A_c = 8
w_c = 2

# fm sensitivity
k_f = 2

color = '#54626F'

t = np.linspace(0, n_t * 2*np.pi, num=n_t*100)

# calculate plots
m = A_m * np.cos(w_m * t + phi)
c = A_c * np.cos(w_c * t)
am = (1 + m / A_c) * c
fm = A_c * np.cos(w_c * t + k_f * A_m / w_m * np.sin(w_m * t))
pm = A_c * np.cos(w_c * t + m)

fig, ax = plt.subplots(4,1)

line_m, = ax[0].plot(t, m, c=color)
line_am, = ax[1].plot(t, am, c=color)
line_am_mh, = ax[1].plot(t, m + A_c, '--k')
line_am_ml, = ax[1].plot(t, -m - A_c, '--k')
line_fm, = ax[2].plot(t, fm, c=color)
line_pm, = ax[3].plot(t, pm, c=color)

ax[0].set_axis_off()
ax[1].set_axis_off()
ax[2].set_axis_off()
ax[3].set_axis_off()

ax[0].set_ylim(-10,10)
ax[1].set_ylim(-10,10)
ax[2].set_ylim(-10,10)
ax[3].set_ylim(-10,10)

ax[0].set_title('message')
ax[1].set_title('am')
ax[2].set_title('fm')
ax[3].set_title('pm')


def update(t_step):
    m = A_m * np.cos(w_m * (t + t_step) + phi)
    c = A_c * np.cos(w_c * (t + t_step))
    am = (1 + m / A_c) * c
    fm = A_c * np.cos(w_c * (t + t_step) + k_f * A_m / w_m * np.sin(w_m * (t + t_step)))
    pm = A_c * np.cos(w_c * (t + t_step) + m)

    line_m.set_ydata(m)
    line_am.set_ydata(am)
    line_am_mh.set_ydata(m + A_c)
    line_am_ml.set_ydata(-m - A_c)
    line_fm.set_ydata(fm)
    line_pm.set_ydata(pm)


animation = FuncAnimation(fig, update,
                          frames=np.linspace(0,2*np.pi/w_m),
                          interval=100,
                          )

animation.save('modulations.gif', writer='imagemagick')

#plt.show()
