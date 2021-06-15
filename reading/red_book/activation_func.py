import numpy as np


def step_function(x):
    if isinstance(x, np.ndarray):
        y = x > 0
        return y.astype(np.int)
    return int(x > 0)
def sigmoid(x):
    return 1 / ( 1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

import matplotlib.pylab as plt

x = np.arange(-5,5,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-1,6)
plt.show()
