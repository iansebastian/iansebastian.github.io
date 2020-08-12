import matplotlib.pyplot as plt
import numpy as np


def collatz_count(x):
    """
    Iteratively applying Collatz's rules to a number x, until it converges to 1.
    :param x: int
        the initial number.
    :return: int
        number of repetitions when x converges to 1.
    """
    result = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        result += 1
    return result


def create_collatz_plot(start, stop):
    """
    Using collatz_count to all integers from start to stop -- plots it.
    :param start:
    :param stop:
    :return:
        fig, ax : Matplotlib objects.
    """
    counts = np.array([collatz_count(start + i) for i in range(stop+1 - start)])
    x_space = np.arange(start, stop+1)
    _ = plt.plot(x_space, counts,
                 linestyle='none',
                 marker='o',
                 color='red',
                 markersize = 0.2)

    _ = plt.title("Looking at the Collatz Conjecture")
    _ = plt.xlabel("Initial Value")
    _ = plt.ylabel("Number of Repetitions")
    _ = plt.show()

    return counts
