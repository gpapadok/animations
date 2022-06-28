import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np


# np.random.seed(9999)
pivot_col = '#E30022' # red
curr_col = '#006B3C' # green
part_col = '#2A52BE' # gray
other_col = '#91A3B0' # blue


class quicksort_gen:
    def __init__(self, arr, random_pivot=False):
        self.arr = arr 
        self.lo = 0
        self.hi = len(arr) - 1

        self.random_pivot = random_pivot

    def partition(self):
        pivot = self.arr[self.hi]
        i = self.lo
        yield self.arr, self.hi, self.lo, self.hi, i

        for j in range(self.lo, self.hi):
            yield self.arr, self.hi, self.lo, self.hi, j
            if self.arr[j] < pivot:
                if j != i:
                    self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
                    yield self.arr, self.hi, self.lo, self.hi, j
                i += 1 

        self.arr[i], self.arr[self.hi] = self.arr[self.hi], self.arr[i]
        self.pivot = i 
        yield self.arr, pivot, self.lo, self.hi, -1

    def __iter__(self):
        if len(self.arr) <= 1:
            return self.arr 

        if self.lo < self.hi:
            # random pivot
            if self.random_pivot:
                idx = np.random.randint(low=self.lo, high=self.hi+1)
                self.arr[idx], self.arr[self.hi] = self.arr[self.hi], self.arr[idx]

            yield from self.partition()

            loR = self.lo 
            hiR = self.pivot - 1 

            loL = self.pivot + 1 
            hiL = self.hi 

            self.lo = loR
            self.hi = hiR
            yield from self.__iter__()
            self.lo = loL
            self.hi = hiL
            yield from self.__iter__()


# initialize array
y = np.random.randint(100, size=20)
x = list(range(len(y)))

qsort = quicksort_gen(y)
qsort_iter = iter(qsort)


# initialize figure
fig, ax = plt.subplots()
       

bars = ax.bar(x, y)


def init():
    ax.set_xticks([])
    ax.set_yticks([])
#    ax.set_title('Quicksort animated')


def animate(state):
    arr, pivot, lo, hi, curr = state

    # update bar heights
    for k, (val, rec) in enumerate(zip(arr, bars)):
        # update bar heights
        rec.set_height(val)

        # update colors
        if k == pivot:
            rec.set_color(pivot_col)
        elif k == curr:
            rec.set_color(curr_col)
        elif k >= lo and k < hi:
            rec.set_color(part_col)
        else:
            rec.set_color(other_col)

    return bars,


animation = FuncAnimation(fig, animate,
                          frames=qsort_iter,
                          interval=100,
                          init_func=init,
                          repeat=False,
                          )

animation.save("quicksort.gif", writer="imagemagick")
# plt.show()
