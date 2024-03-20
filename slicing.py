import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a.shape)
print(a)

# Get a specific element [row, column]
print(a[0, 6])

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 6])