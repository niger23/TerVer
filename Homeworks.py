import numpy as np
import math

def combination (n,k):
    return math.factorial(n)/math.factorial(k)*math.factorial(n-k)
def placement (n,k):
    return math.factorial(n)/math.factorial(n-k)
def permutation (n):
    return math.factorial(n)

print("Задача 1")
