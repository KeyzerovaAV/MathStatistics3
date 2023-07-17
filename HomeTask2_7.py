import numpy as np
import scipy.stats as stats

measuring1 = np.array([150, 160, 165, 145, 155])
measuring2 = np.array([140, 155, 150, 130, 135])
measuring3 = np.array([130, 130, 120, 130, 125])
print(stats.friedmanchisquare(measuring1, measuring2, measuring3))

# даже при выборе уровня статистической значимости = 0.01 p-value меньше, 
# что говорит о неверности нулевой гипотезы, т.о. делаем вывод, 
# что имеются статистически значимые различия
