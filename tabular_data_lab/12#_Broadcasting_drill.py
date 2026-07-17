import numpy as np

A = np.random.randn(100,5)

col_mean = A.mean(axis=0)
col_std = A.std(axis=0)

A_normalize = (A-col_mean)/col_std

print(A_normalize)
