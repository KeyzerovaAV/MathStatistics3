import numpy as np
import scipy.stats as stats

X1 = np.array([20, 17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
Y1 = np.array([20, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])
print(stats.wilcoxon(X1, Y1))

X2 = np.array([32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
Y2 = np.array([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])
print(stats.wilcoxon(X2, Y2))
