"""
    Модуль с функциями для решения основных задач.
    Реализует вычисление перестановок, размещений
    и сочетаний без повторений с повторениями, вычисление
    факториала.
"""


# -------------- Служебные функции --------------
from itertools import permutations


def _get_permutations(elements):
    result = []
    elem_length = len(elements)

    copy_el = list(elements)
    for i in range(0, elem_length, 1):
        curr_el = copy_el.pop(i)

        pre_result = (
            curr_el,
            *copy_el,
        )
        if len(copy_el) == 2:
            j = elem_length - 1
            copy_el[j], copy_el[j - 1] = copy_el[j - 1], copy_el[j]

            result.append(pre_result)
        else:


        j -= 1

    copy_el.insert(i, curr_el)

    return result


print(_get_permutations((
    'a',
    'b',
    'c',
    'd',
)))

for x in permutations((
    'a',
    'b',
    'c',
    'd',
)):
    print(x, end=', ')
# -----------------------------------------------

def factorial(n):
    result = 1

    while n > 1:
        result *= n
        n -= 1

    return result


def placement_with_repeat(el_count, pos_count):
    """
    Размещение с повторениями.
    Генерирует размещение по аналогии с вычислением
    всех возможных чисел в системе счисления по
    основанию el_count с количеством разрядов в числе
    pos_count.
    Формула для вычисления кол-ва элементов:
    A = el_count**pos_count
    :param el_count: Количество используемых элементов
    (основание системы счисления)
    :param pos_count: Количество позиций в размещении
    (количество разрядов в числе)
    :return: list[tuple]
    """
    # список счетчиков (разрядов), равны 0 в начале,
    # самое первое размещение
    counters = [0] * pos_count
    # для экономии памяти будем собирать список кортежей
    combinations = [
        tuple(counters),
    ]

    # индекс последнего счетчика в списке
    i = pos_count - 1
    # цикл выполняется пока не начали
    # переносить единицу в несуществующий разряд
    while i > -1:
        counters[i] += 1

        if counters[i] == el_count:
            # когда счетчик в текущей позиции достиг
            # максимума его необходимо обнулить и
            # перейти к следующему счетчику
            counters[i] = 0
            i -= 1
        else:
            # если еще не достигли максимума, то необходимо
            # перейти к последнему счетчику (разряду единиц)
            # и запомнить получившееся размещение
            i = pos_count - 1
            combinations.append(
                tuple(counters)
            )

    return combinations
