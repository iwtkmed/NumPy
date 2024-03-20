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
# print(x)

# Any other number
y = np.full((3,4,2), 69)
# print(y)

# Initialize array of random decimal numbers
d = np.random.rand(4, 5, 3)
# print(d)

# Initialize array of random integer values
i = np.random.randint(10, size=(3, 4, 5))
print(i)