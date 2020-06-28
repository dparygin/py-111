"""
Сорт
Дано: массив из 10**6 целых чисел,
каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее
эффективным способом
"""
import random

A = 13
B = 25
sum_dig = (10**6)

def data_gen(A, B, sum_dig):
    """
    Генератор списка с данными
    :return: Data List
    """
    listmass = []
    for i in range(sum_dig):
        listmass.append(random.randint(A, B))
    return listmass


def sort_list():
    """
    Генератор словоря учета
    :return:
    """
    dict = {}
    for i in range(A, B+1):
        dict.update({i: 0})
    return dict

def summ_list(dg, sl):
    """
    Схлопываем список в один
    словарь, за один проход.
    А затем разворачиваем в
    правильном порядке.
    :param dg: Несортированный список
    :param sl: Начальный сортированный
    словарь
    :return: Отсортированный словарь
    """
    flist = []
    for i in dg:
        sl.update({i: (sl.get(i) + 1)})
    for key, vaule in sl.items():
        for _ in range(vaule):
            flist.append(key)
    return flist

def main():
    sl = sort_list()
    dg = data_gen(A, B, sum_dig)
    print("Сгенерированный несортированный список")
    print(dg)
    print("Отсортированный")
    print(summ_list(dg, sl))

if __name__ == '__main__':
    main()
