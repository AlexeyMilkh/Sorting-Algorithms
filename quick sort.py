"""Общая идея алгоритма состоит в следующем:

1. Выбрать из массива элемент, называемый опорным. Это может быть любой из элементов массива. От выбора опорного
элемента не зависит корректность алгоритма, но в отдельных случаях может сильно зависеть его эффективность.

2. Сравнить все остальные элементы с опорным и переставить их в массиве так, чтобы разбить массив на три
непрерывных отрезка, следующих друг за другом: «элементы меньшие опорного», «равные» и «большие».

3. Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же последовательность операций, если длина
отрезка больше единицы."""
from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:  # Если длина массива меньше или равна единице
        return nums

    elem = nums[0]  # Инициализация опорного элемента
    left = list(filter(lambda x: x < elem, nums))  # В левую часть помещаются элементы меньше опорного
    center = [i for i in nums if i == elem]  # Список с элементами, равными опорному
    right = list(filter(lambda x: x > elem, nums))  # В правую часть помещаются элементы больше опорного

    return quick_sort(left) + center + quick_sort(right)  # Алгоритм рекурсивно вызывается для левой и правой части


print(quick_sort([7, 6, 10, 5, 9, 8, 3, 4]))
