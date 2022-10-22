# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

def FillArray():
    array = []
    array = [int(i) for i in input().split()]
    return array

def NewArray(array):
    new_array = []
    for i in array:
        if array.count(i) < 2:
            new_array.append(i)
    return new_array

print('Введите элементы списка через пробел: ')
array = FillArray()
print(f'Список неповторяющихся элементов: {NewArray(array)}')