from scipy import stats
import math

print("Задача 1\n")
print("""Даны две  независимые выборки. Не соблюдается условие нормальности
x1  380,420, 290
y1 140,360,200,900
Сделайте вывод по результатам, полученным с помощью функции\n""")
x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]
print(stats.mannwhitneyu(x1,y1))
print("     Т.к. pvalue = 0.629, то при статистической важности 5% мы принимаем нулевую гипотезу, т.е. статистически значимых различий не обнаружено\n")


print("Задача 2\n")
print("""Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?
1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150,  130, 135
3е измерение через 30 минут: 130, 130, 120, 130, 125\n""")
x1 = [150, 160, 165, 145, 155]
x2 = [140, 155, 150,  130, 135]
x3 = [130, 130, 120, 130, 125]
print(stats.friedmanchisquare(x1,x2,x3))
print("     Т.к. pvalue = 0.01, то при статистической важности 5% мы принимаем альтернативную гипотезу, т.е. обнаружены статистически значимые отличия\n")

print("Задача 3\n")
print("""3 ) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.\n""")
print(stats.wilcoxon(x1,x2))
print("     Т.к. pvalue = 0.06, то при статистической важности 5% мы принимаем нулевую гипотезу, т.е. статистически значимых различий не обнаружено\n")


print("Задача 4\n")
print("""Даны 3 группы  учеников плавания.
В 1 группе время на дистанцию 50 м составляют:
56, 60, 62, 55, 71, 67, 59, 58, 64, 67
Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54\n""")
x1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
x2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
x3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]
print(stats.kruskal(x1,x2,x3))
print("     Т.к. pvalue = 0.07, то при статистической важности 5% мы принимаем нулевую гипотезу, т.е. статистически значимых различий не обнаружено\n")


print("Задача 5\n")
print(""" Заявляется, что партия изготавливается со средним арифметическим 2,5 см. Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. Объем выборки 10, уровень статистической значимости 5%
2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34\n""")
arr = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
m = 2.5
mean = sum(arr)/len(arr)
sum_up = 0
for i in arr:
    sum_up += pow(i - mean, 2)
s = sum_up/(len(arr)-1)
t = (mean - m)/math.sqrt(s/len(arr))
print(f"Наблюдаемое значение критерия: {t:.4f}")
print(f"Табличное значение критерия с уровнем значимости 5%: {stats.t.ppf(0.975,9):.4f}")
print("    Т.к. наблюдаемое значение меньше табличного, мы принимаем нулевую гипотезу, т.е. статистически значимых различий не обнаружено\n")