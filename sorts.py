#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2024 Fomenko A V

from time import time
from itertools import permutations
from random import shuffle, sample, randint


class BogoSort(object):
    """
    Болотная сортировка. Получает список который надо отсортировать.
    Выбирайте размер списка осторожно, а то можно затянуться!!!
    """

    def __init__(self, source_list):
        super(BogoSort, self).__init__()
        self.source_list = list(source_list)

    def sort(self):
        while (self.check()):
            shuffle(self.source_list)

        return self.source_list

    def check(self):
        for i in range(0, len(self.source_list)-1):
            if self.source_list[i] > self.source_list[i+1]:
                return True
        return False


class BozoSort(object):
    """
    Случайно переставляет два элемента в последовательности, до готовности
    """

    def __init__(self, source_list):
        super(BozoSort, self).__init__()
        self.arr = list(source_list)

    def sort(self):
        while (self.check()):
            j = sample(range(len(self.arr)), k=2)
            self.arr[j[0]], self.arr[j[1]] = self.arr[j[1]], self.arr[j[0]]

        return self.arr

    def check(self):
        for i in range(0, len(self.arr)-1):
            if self.arr[i] > self.arr[i+1]:
                return True
        return False


class StoogeSort(object):
    """
    Берём отрезок массива (вначале это весь массив) и сравниваем элементы на 
    концах отрезка. Если слева больше чем справа, то, естественно, меняем 
    местами.
    Затем, если в отрезке не менее трёх элементов, то тогда:
    1) вызываем Stooge sort для первых 2/3 отрезка;
    2) вызываем Stooge sort для последних 2/3 отрезка;
    3) снова вызываем Stooge sort для первых 2/3 отрезка.
    """

    def __init__(self, arr):
        super(StoogeSort, self).__init__()
        self.arr = list(arr)

    def sort(self, source_list=None, lo=None, hi=None):
        if (not source_list):
            source_list = self.arr
        if (not lo):
            lo = 0
        if (not hi):
            hi = len(source_list)-1

        if (source_list[lo] > source_list[hi]):
            source_list[lo], source_list[hi] = source_list[hi], source_list[lo]

        if (lo+1 >= hi):
            return

        third = int((hi - lo + 1) / 3)

        self.sort(source_list, lo, hi-third)
        self.sort(source_list, lo+third, hi)
        self.sort(source_list, lo, hi-third)

        return source_list


class PermSort(object):
    """
    Сортировка перестановками, перебирает все перестановки, пока не найдет 
    отсортированную
    """

    def __init__(self, arr):
        super(PermSort, self).__init__()
        self.arr = list(arr)

    def sort(self):
        for i in permutations(self.arr):
            if (self.check(i)):
                return list(i)

    def check(self, arr):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True


class DinasourSort(object):
    """TODO"""

    def __init__(self, arg):
        super(DinasourSort, self).__init__()
        self.list = []
        for i in arg:
            self.list.append(str(i))

        self.right_egg = ['egg', 'chiken']

    def sort(self):
        self.list.sort()
        return(self.right_egg + self.list)


class StalinSort(object):
    """
    Однопроходная сортировка с линейной сложностью O(n). Сталинская сортировка.
    Проходим по каждому элементу проверяя находится ли элемент на своем месте 
    или нет. Если элемент не на своем месте то просто его уничтажаем. В конце 
    имеем отсортированое множество.
    """

    def __init__(self, arg):
        super(StalinSort, self).__init__()
        self.arg = list(arg)

    def sort(self):
        max_val = self.arg[0]
        result = []
        for x in self.arg:
            if (x >= max_val):
                max_val = x
                result.append(x)

        return result


def gen(n: int) -> tuple:
    '''
    Генерирует список заданного размера из случайных целых чисел
    '''
    numbers = []
    while(n):
        numbers.append(randint(0, 1000))
        n -= 1
    return tuple(numbers)


def run(sort_obj):
    start = time()
    result = sort_obj.sort()
    end = time()
    tt = end - start
    print(f'{type(sort_obj).__name__} - {result} - {tt} s or {tt/60} min')


def main():
    arr = gen(int(input("Введите размер массива: ")))
    print(f"Ваш массив {arr}\n")

    sort_objs = (StoogeSort(arr), StalinSort(arr), PermSort(arr),
                 BozoSort(arr), BogoSort(arr), DinasourSort(arr))

    for i in sort_objs:
        run(i)


if __name__ == '__main__':
    main()
