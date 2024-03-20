import numpy as np

# INITIALIZING DIFFERENT TYPES OF ARRAYS

# All 0's matrix
a = np.zeros((5))
# print(a)

b = np.zeros((3, 4))
# print(b)

c = np.zeros((4, 3, 3))
# print(c)

# print(c.dtype) # automatically is float64; can reassign

# All 1's matrix
x = np.ones((2, 3, 3), dtype="int16")
print(x)