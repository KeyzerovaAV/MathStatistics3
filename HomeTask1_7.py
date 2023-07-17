import numpy as np
import scipy.stats as stats

x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])
print(stats.mannwhitneyu(x1, y1))

# даже при выборе уровня статистической значимости = 0.1 p-value больше, 
# что говорит о верности нулевой гипотезы, т.о. делаем вывод, 
# что статистически значимых различий между двумя выборками нет