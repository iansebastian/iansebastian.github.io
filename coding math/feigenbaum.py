import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def log_model(coef, x):
    return coef * x * (1-x)

x = np.linspace(0, 1)
fig, ax = plt.subplots()
ax.plot(x, log_model(2, x), 'k')

plt.show()