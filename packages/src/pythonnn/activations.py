import numpy as np


def max(x, y):
    if x > y: return x
    else: return y

def min(x, y):
    if x < y: return x
    else: return y

class Sigmoid:
    def __init__(self):
        pass

    def use(self, x):
        return 1 / (1 + np.exp(-x))


class Tanh:
    def __init__(self):
        pass

    def use(self, x):
        return np.tanh(x)


class ReLU:
    def __init__(self):
        pass

    def use(self, x):
        return max(0, x)


class ReLU2:
    def __init__(self):
        pass

    def use(self, x):
        return max(-1, x)


class Cutoff:
    def __init__(self):
        pass

    def use(self, x):
        return min(1, x)
