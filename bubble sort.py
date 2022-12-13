"""Алгоритм состоит из повторяющихся проходов по сортируемому массиву. За каждый проход элементы последовательно
сравниваются попарно и, если порядок в паре неверный, выполняется перестановка элементов. Проходы по массиву
повторяются N−1 раз или до тех пор, пока на очередном проходе не окажется, что обмены больше не нужны,
что означает — массив отсортирован. При каждом проходе алгоритма по внутреннему циклу очередной наибольший элемент
массива ставится на своё место в конце массива рядом с предыдущим «наибольшим элементом», а наименьший элемент
перемещается на одну позицию к началу массива («всплывает» до нужной позиции, как пузырёк в воде — отсюда и название
алгоритма)."""
from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    for j in range(len(nums)-1):  # Внешний цикл (длина массива, в котором будет попарное сравнение элементов)
        for i in range(len(nums) - 1 - j):  # Внутренний цикл (наибольший элемент поставится в конце массива)
            if nums[i] > nums[i + 1]:  # Сравнение попарно левого и правого элементов
                nums[i], nums[i + 1] = nums[i + 1], nums[i]  # Происходит перестановка элементов
    return nums


print(bubble_sort([5, 7, 4, 3, 8, 2]))
print(bubble_sort([-4, 1, 0, -7, 3, 3]))
print(bubble_sort([8]))
