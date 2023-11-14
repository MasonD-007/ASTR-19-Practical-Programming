"""
Write a Python program that writes out a table of the function sin(x) vs. x, 
where x is tabulated between 0 and 2 with a thousand entries. 
Follow the basic Python program structure, including a main program function.
"""
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    x = np.linspace(0, 2, 1000)
    plt.plot(x, np.sin(x), 'r--', label='sin(x)')
    plt.legend()
    plt.show()