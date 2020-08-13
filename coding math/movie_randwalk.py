import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML


def gen_pure_randwalk(len=260, drift=0, sigma=1):
    """
    Generates a pure random walk for data, with starting point 1, unless specified.

    Args
    ----
    len: int
        The length desired for data. Default value 260 (representing 260 days - 5 days a week, 52 weeks a year - annual)
    drift: int
        Defines the initial value desired for data. Default value 0.
    sigma: float
        The standard deviation desired for the random walk.

    Returns
    -------
        data:
            a NumPy array, containing values for random walk.
    """
    np.random.seed(np.random.randint(101108))
    data = np.empty(len)
    data[0] = drift
    for i in range(1, len):
        data[i] = data[i - 1] + np.random.randn() * sigma
        if data[i] <= 0:
            data[i] = data[i - 1]
    return data


def init():
    l.set_xdata([])
    l.set_ydata([])
    return l,

def update_line(num, data, line):
    line.set_xdata(np.arange(num))
    line.set_ydata(data[:num])
    return line,


fig = plt.figure()
ax = fig.add_subplot()

data = gen_pure_randwalk(len=1000, drift=5, sigma=0.1)
l, = ax.plot([], [], 'b-')

_ = ax.set_title("A Random Walk Down Wall Street")
_ = ax.set_xlim((0, 1000))
_ = ax.set_ylim((0, np.max(data)))
_ = ax.set_xlabel("Days since IPO")
_ = ax.set_ylabel("Closing Price")

anim = animation.FuncAnimation(
    fig, update_line, 1000, fargs=(data, l), interval=5, blit=True, init_func=init)

plt.show()
