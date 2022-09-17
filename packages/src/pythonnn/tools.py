import numpy as np

def max(x, y):
    if x > y: return x
    else: return y

def min(x, y):
    if x < y: return x
    else: return y

def sigmoid(x):
    return 1/(1+np.exp(-x))