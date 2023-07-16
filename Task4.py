import numpy as np
import scipy.stats as stats

A = np.array([3.5, 3.3, 4.9, 3.6])
B = np.array([8.6, 5.4, 8.8, 5.6])
C = np.array([5.1, 8.6, 7.7, 5.0])
print(stats.friedmanchisquare(A, B, C))
