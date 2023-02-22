import math

def combination (n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def bernulli (n,k,p):
    return combination(n,k)*pow(p,k)*pow(1-p,n-k)

def puasson (n,k,p):
    return (pow(n*p,k)/math.factorial(k))*pow(math.e,-n*p)

print("Задача 1\nВероятность того, что стрелок попадет в мишень, \
      выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз. \
      Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.")
n = 100
k = 85
p = 0.8

print(f"Результат: {round(bernulli(n,k,p)*100,2)} %\n")

print("Задача 2\nВероятность того, что лампочка перегорит в течение \
      первого дня эксплуатации, равна 0.0004. В жилом комплексе после \
      ремонта в один день включили 5000 новых лампочек.")
print("Какова вероятность, что ни одна из них не перегорит в первый день?")
n = 5000
k = 0
p = 0.0004

print(f"Результат: {round(puasson(n,k,p)*100,2)} %\n")

print("Какова вероятность, что перегорят ровно две?")
n = 5000
k = 2
p = 0.0004

print(f"Результат: {round(puasson(n,k,p)*100,2)} %\n")

print("Задача 3\nМонету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?")
      
n = 144
k = 70
p = 0.5

print(f"Результат: {round(bernulli(n,k,p)*100,2)} %\n")

print("Задача 4\nВ первом ящике находится 10 мячей, из которых 7 - белые. \
      Во втором ящике - 11 мячей, из которых 9 белых. Из каждого ящика \
      вытаскивают случайным образом по два мяча.")
print("Какова вероятность того, что все мячи белые?")
print(f"Результат: {round((7/10)*(6/9)*(9/11)*(8/10)*100,2)} %\n")
print("Какова вероятность того, что ровно два мяча белые?")
print(f"Результат: {round((((7/10)*(6/9)*(2/11)*(1/10))+4*((7/10)*(3/9)*(9/11)*(2/10))+((3/10)*(2/9)*(9/11)*(8/10)))*100,2)} %\n")
print("Какова вероятность того, что хотя бы один мяч белый?")
print(f"Результат: {round((1-(3/10)*(2/9)*(2/11)*(1/10))*100,2)} %\n")