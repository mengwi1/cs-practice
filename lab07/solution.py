import numpy as np

def reshape_rows(values, width):
    if width <= 0 or len(values) % width != 0:
        return []
    array = np.asarray(values, dtype = float).reshape(-1, width)
    return array.tolist()
