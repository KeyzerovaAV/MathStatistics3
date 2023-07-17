import numpy as np
import scipy.stats as stats

wares = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
average = 2.5
t_calculated = (np.mean(wares) - average) / (np.std(wares, ddof=1) / np.sqrt(len(wares)))
print(t_calculated)

t_tabulated = stats.t.ppf(0.975, len(wares) - 1)
print(t_tabulated)

# поскольку проводим двусторонний тест, t_calculated (= 0.56) лежит в области между -2.26 и 2.26, 
# т.е. в области нулевой гипотезы, т.о. делаем вывод, что нулевая гипотеза верна, 
# а значит статистически значимых различий от генеральной совокупности нет
