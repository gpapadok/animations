import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import ArtistAnimation

###
T = 5 * np.pi
Tp = 3 * T / 4
A = 1
f0 = 1 / T
###


a0 = A * Tp / T

x = np.linspace(-10 * np.pi, 10 * np.pi, num=10 ** 6)
y = np.zeros_like(x) + a0

def a_n(n):
    return 2 * A / (n * np.pi) * np.sin(n * np.pi * Tp / T)


fig, ax = plt.subplots()

lines = []
for n in range(1, 101):
    harmonic = a_n(n) * np.cos(n * 2 * np.pi * f0 * x)
    y += harmonic
    line, = ax.plot(x, y, 'teal')
    title = ax.text(.5, 1.19, f'n harmonics={n}', ha='center')
    lines.append([line, title])

animation = ArtistAnimation(
    fig,
    lines,
    repeat=False
    )

ax.axis('off')
#ax.set_title('Fourier series of Square pulse')
# plt.show()
animation.save("pulse.gif", writer="imagemagick")
