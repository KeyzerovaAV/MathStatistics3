import numpy as np
import scipy.stats as stats

measuring1 = np.array([150, 160, 165, 145, 155])
measuring2 = np.array([140, 155, 150, 130, 135])
print(stats.wilcoxon(measuring1, measuring2))

# при выборе уровня статистической значимости = 0.05 p-value больше, 
# что говорит о верности нулевой гипотезы, т.о. делаем вывод, 
# что статистически значимых различий нет
