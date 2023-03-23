from scipy import stats
import numpy as np
import math


print("Задача 1\n")
print("""Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.\n""")
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(zp)
b1 = (n*np.sum(zp*ks) - np.sum(zp)*np.sum(ks))/(n*np.sum(zp**2) - np.sum(zp)**2)
b0 = np.mean(ks)-b1*np.mean(zp)
print(f"Получены коэффициенты b0 = {b0} и b1 = {b1}")
y_pred = b0 + b1*zp
print(y_pred)
zp1 = zp.reshape(len(zp),1)
ks1 = ks.reshape(len(ks),1)
b = np.dot(np.linalg.inv(np.dot(zp1.T, zp1)), zp1.T @ ks1)
print(f"Коэффициент без интерсепта: {b}\n")

print("Задача 2\n")
print("""Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).\n""")
def mse_(b1, zp, ks):
    return np.sum((b1*zp - ks)**2)/len(zp)
print(mse_(b,zp,ks))
alpha = 1e-06
b1 = 0.1
for i in range (3001):
    b1 -=alpha*(2/len(zp))*np.sum((b1*zp - ks)*zp)
    if i%500 == 0:
        print("Итерация = {i}, b1 = {b1}, mse = {mse}".format(i = i, b1  = b1, mse = mse_(b1,zp,ks)))
print(f"\nПолучено значение b1 = {b1}\n")
print("Задача 3\n")
print("""Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).\n""")
def mse2_(b0, b1, zp, ks):
    return np.sum((b0+b1*zp - ks)**2)/len(zp)
alpha = 5e-05
b0 = 0.1
b1 = 0.1
for i in range (1000000):
    b0 -=alpha*(2/len(zp))*np.sum((b0 + b1*zp - ks))
    b1 -=alpha*(2/len(zp))*np.sum((b0 + b1*zp - ks)*zp)
    if i%200000 == 0:
        print("Итерация = {i}, b0 = {b0}, b1 = {b1}, mse = {mse}".format(i = i, b0 = b0, b1  = b1, mse = mse2_(b0,b1,zp,ks)))
print(f"\nПолучены значения b0 = {b0}, b1 = {b1}\n")


