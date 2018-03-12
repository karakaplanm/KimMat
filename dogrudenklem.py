import numpy as np
x = np.array([1, 2, 3, 4,5])
y = np.array([3, 5, 7, 9, 11])
A = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(A, y)[0]
print(a, b)
