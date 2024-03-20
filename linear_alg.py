import numpy as np

a = np.ones((2, 3))
print(a)

# For matrix multiplication, 
# m1 = [m, n]
# m2 = [n, p]
# m1*m2 = [m, p]

b = np.full((3, 2), 2)
print(b)

print(np.matmul(a, b))

# Reference docs  (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...