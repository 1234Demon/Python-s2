# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

import os
os.system("cls")

n = int(input('Enter amount of coin: '))
countCoins = 0

for i in range(n):
    coin = int(input('Enter coin: '))
    if coin == 1:
        countCoins += 1

print(countCoins if countCoins<n/2 else n-countCoins)
