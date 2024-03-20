import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before.shape)

# Reshape an array
after = before.reshape((8,1))
# print(after)

after_three_d = before.reshape((2, 2, 2))
# print(after_three_d)

# Vertically stacking matrices/vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1, v1, v2, v2, v2]))