# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

import os
os.system("cls")

n = int(input('Enter n = '))

for i in range(2, n):
    if n % i == 0:
        print(i)
        exit()

print(n)