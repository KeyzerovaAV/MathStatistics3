import numpy as np
import scipy.stats as stats

gr1 = np.array([0.5, 0.7, 1, 1.2, 1.4])
gr2 = np.array([1.3, 1.45, 1.6, 1.7, 1.8])
gr3 = np.array([6.2, 12.6, 13.2, 14.1, 14.2])
print(stats.kruskal(gr1, gr2, gr3))
