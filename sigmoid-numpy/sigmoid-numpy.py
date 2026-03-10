import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x, dtype=float)   # convert input to NumPy array
    return 1 / (1 + np.exp(-x))