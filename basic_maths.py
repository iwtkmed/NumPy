import numpy as np

a = np.array([1,2,3])

# will change the original a array as well
# b = a

# copy original array
b = a.copy()
b[0] = 100

print(b)
print(a)