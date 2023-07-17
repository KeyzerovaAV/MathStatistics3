import numpy as np
import scipy.stats as stats

group1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
group2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
group3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
print(stats.kruskal(group1, group2, group3))

# при выборе уровня статистической значимости = 0.05 p-value больше, 
# что говорит о верности нулевой гипотезы, т.о. делаем вывод, 
# что статистически значимых различий нет
