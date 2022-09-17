import numpy as np
import tools

def sigmoid(x):
    return 1/(1+np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return tools.max(0, x)

def relu2(x):
    return tools.max(-1, x)

def cutoff(x):
    return tools.min(1, x)