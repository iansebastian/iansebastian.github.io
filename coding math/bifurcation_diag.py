import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt


def logistic_model(r, x):
    return r * x * (1-x)


iters=10000

x_plot = np.empty(1)
y_plot = np.empty(1)

x = 1e-5 * np.ones(iters)
r = np.linspace(2.5, 4, iters)

x_plot = np.empty(0,)
r_plot = np.empty(0,)
for i in range(iters):
    x = logistic_model(r, x)
    if i >= iters-100:
        r_plot = np.append(r_plot, np.linspace(2.5, 4, iters))
        x_plot = np.append(x_plot, x)

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(12,8))

l, = ax.plot([], [], ',r', alpha=.2)

def init():
    _ = l.set_xdata([])
    _ = l.set_ydata([])
    return l,


def update_line(i, line, r_plot, x_plot):
    _ = line.set_xdata(np.linspace(2.5, 4, i))
    _ = line.set_ydata(x_plot[r_plot <= 2.5 + 1.5*i/10000])
    return line,


_ = ax.set_xlim(2.5, 4)

bifu_anim = animation.FuncAnimation(fig, update_line, fargs=(l, r_plot, x_plot),
                                    interval=5, blit=True, init_func=init)

_ = plt.show()
