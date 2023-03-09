from scipy import stats
import math

print("Задача 1\n")
print("""Известно, что генеральная совокупность распределена нормально
со средним квадратическим отклонением, равным 16.
Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
если выборочная средняя M = 80, а объем выборки n = 256.\n """)
m = 80
n = 256
str = 16
z = stats.norm.ppf(0.975)

left_value = m - (z*str/math.sqrt(n))
right_value = m + (z*str/math.sqrt(n))

print(f"Результат: [ {left_value:.2f} ; {right_value:.2f} ]\n")

print("Задача 2\n")
print("""В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
значение с доверительной вероятностью 0,95.\n """)
arr = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
t = stats.t.ppf(0.975, len(arr) - 1)
mean = sum(arr)/len(arr)
sum_up = 0
for i in arr:
    sum_up += pow(i - mean, 2)
d = sum_up/(len(arr)-1)
left_value = mean - t*math.sqrt(d/len(arr))
right_value = mean + t*math.sqrt(d/len(arr))

print(f"Результат: [ {left_value:.2f} ; {right_value:.2f} ]\n")

print("Задача 3\n")
print("""Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.\n """)
arr1 = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
arr2 = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]

mean1 = sum(arr1)/len(arr1)
mean2 = sum(arr2)/len(arr2)
delta = abs(mean1-mean2)
sum_up1 = 0
for i in arr1:
    sum_up1 += pow(i - mean1, 2)
d1 = sum_up1/(len(arr)-1)
sum_up2 = 0
for i in arr2:
    sum_up2 += pow(i - mean2, 2)
d2 = sum_up2/(len(arr)-1)

d = (d1+d2)/2
s = math.sqrt(d/len(arr1)+d/len(arr2))

t = stats.t.ppf(0.975, (len(arr1) - 1) + (len(arr2) - 1))

left_value = delta - t*s
right_value = delta + t*s

print(f"Результат: [ {left_value:.2f} ; {right_value:.2f} ]\n")