# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

import os
os.system("cls")

n = int(input('Enter n = '))
a = 0

for i in range(n):
    a = a + n - i
    i += 1

print(a)
