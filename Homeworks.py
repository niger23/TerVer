import math

def combination (n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
def placement (n,k):
    return math.factorial(n)/math.factorial(n-k)
def permutation (n):
    return math.factorial(n)

print("Задача 1\nИз колоды в 52 карты извлекаются случайным образом 4 карты.\na) Найти вероятность того, что все карты – крести.")
n = 52
k = 4
add = 13 # всего крестей 
print(f"Результат: {round(100*combination(add,k)/combination(n,k), 3)} %\n")

print("б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.")
add = 48 # карты без тузов
divisible = combination(k,1)*combination(add,3) + combination(k,2)*combination(add,2) + combination(k,3)*combination(add,1) + combination(k,4)*combination(add,0)
print(f"Результат: {round(100*divisible/combination(n,k), 3)} %\n")

print("Задача 2\nНа входной двери подъезда установлен кодовый замок, \
содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, \
которые нужно нажать одновременно. Какова вероятность того, что человек, \
не знающий код, откроет дверь с первой попытки?")

n = 10
k = 3
print(f"Результат: {round(100*1/combination(n,k), 3)} %\n")

print("Задача 3\nВ ящике имеется 15 деталей, из которых 9 окрашены. \
Рабочий случайным образом извлекает 3 детали. Какова вероятность того,\
что все извлеченные детали окрашены?")

n = 15
k = 3
add = 9 # всего окрашенных

print(f"Результат: {round(100*combination(add,k)/combination(n,k), 3)} %\n")

print("Задача 4\nВ лотерее 100 билетов. Из них 2 выигрышных. \
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?")

n = 100
k = 2
add = 2 # всего выигрышных

print(f"Результат: {round(100*combination(add,k)/combination(n,k), 3)} %\n")