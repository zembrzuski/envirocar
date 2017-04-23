import matplotlib.pyplot as plt
import numpy as np


def line_plotting_one_dimension(inp):
    plt.plot(inp)
    plt.show()


def line_plotting_two_dimensions(matrix):
    x = list(map(lambda x: x[0], matrix))
    y = list(map(lambda x: x[1], matrix))

    plt.plot(x, y)
    plt.show()
