"""
    Модуль с функциями для решения основных задач.
    Реализует вычисление перестановок, размещений
    и сочетаний без повторений с повторениями, вычисление
    факториала.
"""


def factorial(n):
    """
    Функция нахождения факториала
    :param n: аргумент факториала
    :return: int
    """
    result = 1

    while n > 1:
        result *= n
        n -= 1

    return result


# -------------------------------- ПЕРЕСТАНОВКИ --------------------------------
def placement_with_repeat(el_set, repeated_el, repeat_count):
    first_placement = []
    for curr in el_set:
        # вставляем в базовую комбинацию элемент
        first_placement.append(
            curr
        )

        # если текущий в цикле элемент - повторяющийся
        # то вставим его еще (repeat_count - 1) раз
        if curr == repeated_el:
            counter = 1

            while counter < repeat_count:
                first_placement.append(
                    curr
                )
                counter += 1

    return placement_without_repeat(
        el_set=first_placement,
    )


def placement_without_repeat(el_set):
    """
    Перестановка без повторений.
    Использует алгоритм Нарайаны для генерации.
    :param el_set: элементы во множестве
    :return: list[tuple]
    """
    n = len(el_set)
    base_placement = list(el_set)

    # первое размещение надо запомнить
    results = [
        tuple(base_placement)
    ]

    while True:
        # 1 шаг алгоритма - найти i
        # для которого А[i] < A[i + 1]
        max_i = None
        for i in range(n - 2, -1, -1):
            if base_placement[i] < base_placement[i + 1]:
                # нашли нужный i
                max_i = i
                break

        # если не нашли элемента, подходящего под условие, то
        # прерываем генерацию размещений
        if max_i is None:
            break

        # 2 шаг алгоритма - найти j для которого А[j] > A[i]
        max_j = None
        for j in range(n - 1, -1, -1):
            if base_placement[j] > base_placement[max_i]:
                # нашли нужный j
                max_j = j
                break

        # 3 шаг алгоритма - поменять местами A[i] и A[j]
        base_placement[max_i], base_placement[max_j] = (
            base_placement[max_j], base_placement[max_i]
        )
        # 4 шаг алгоритма - реверсировать последовательность
        # A[i + 1]...A[j]
        max_i += 1
        base_placement = base_placement[:max_i] + base_placement[n - 1:max_i - 1:-1]
        results.append(
            tuple(base_placement)
        )

    return results
# -------------------------------- ПЕРЕСТАНОВКИ --------------------------------


# -------------------------------- РАЗМЕЩЕНИЯ --------------------------------
def get_all_placement_with_repeat(el_count, pos_count):
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
    # индекс счетчика должен лежать в пределах
    # существующих счетчиков [0; pos_count - 1]
    while 0 <= i <= pos_count - 1:
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


def get_all_placement_without_repeat(el_count, pos_count):
    """
    TODO: A теперь, после всего пережитого, надо все задокументировать
     !!!(ЗАКОММЕНТИТЬ)!!!
    """
    all_placement = placement_without_repeat(range(0, el_count))
    results = []

    for x in all_placement:
        results.append(
            x[:pos_count]
        )

    return results
# -------------------------------- РАЗМЕЩЕНИЯ --------------------------------


# -------------------------------- СОЧЕТАНИЯ --------------------------------
def get_combinations_with_repeat(el_count, pos_count):
    """
    TODO: A теперь, после всего пережитого, надо все задокументировать
     !!!(ЗАКОММЕНТИТЬ)!!!
    """
    counters = [0] * pos_count
    combinations = []

    i = pos_count - 1
    while counters[0] is not (el_count - 1):
        combinations.append(
            tuple(counters)
        )

        # пытаемся найти позицию счетчика, который
        # не достиг максимального значения
        while counters[i] == (el_count - 1):
            i -= 1

        counters[i] += 1
        counters = counters[:i + 1] + [counters[i]] * (pos_count - (i + 1))
        i = pos_count - 1

    # запомним последнюю комбинацию
    combinations.append(
        tuple(counters)
    )
    return combinations


def get_combinations_without_repeat(el_count, pos_count):
    """
    TODO: A теперь, после всего пережитого, надо все задокументировать
     !!!(ЗАКОММЕНТИТЬ)!!!
    """
    first_comb_max_el = el_count - pos_count + 1
    counters = list(
        range(0, pos_count)
    )
    combinations = []

    while counters[0] is not first_comb_max_el:
        i = pos_count - 1
        combinations.append(
            tuple(counters)
        )

        # пытаемся найти позицию счетчика, который
        # не достиг максимального значения
        while counters[i] == (first_comb_max_el + i):
            i -= 1

        counters[i] += 1
        for j in range(i + 1, pos_count):
            counters[j] = counters[j - 1] + 1

    # запомним последнюю комбинацию
    combinations.append(
        tuple(counters)
    )
    return combinations
# -------------------------------- СОЧЕТАНИЯ --------------------------------
