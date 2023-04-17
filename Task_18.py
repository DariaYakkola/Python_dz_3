# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X . Если таких значений
# больше одного, вывести первый найденный.
from random import randint
size = int(input('Сколько будет элементов? '))
array = [randint(1, 10) for _ in range(size)]
number = int(input('Введите число: '))
min_minus = min_result = array[0]
for i in range(size):
    result = number - array[i]
    if result < 0:
        result *= -1
    if (result < min_result) and (result != 0):
        min_result = result
        min_minus = array[i]
        if min_result == 1:
            break
print(f'В массиве {array} ближайшее по величине к числу '
      f'{number} - это число {min_minus}')
