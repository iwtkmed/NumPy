import numpy as np

x = np.ones((5, 5), dtype="int16")
x[1:4, 1:4] = 0
x[2, 2] = 9
print(x)