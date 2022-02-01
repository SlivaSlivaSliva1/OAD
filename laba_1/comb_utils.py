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
def _get_repeat_settings_and_el_set(el_count, repeated_el_dict):
    new_el_set = []

    for i in range(0, el_count):
        repeated_count = repeated_el_dict.get(i)
        if not repeated_count:
            repeated_count = 1
            # обновляем словарь повторений,
            # элемент встречается один раз
            repeated_el_dict.update({
                i: repeated_count,
            })

        # добавляем элемент в множество
        # repeated_count раз
        new_el_set.extend(
            [i] * repeated_count
        )

    # возвращаем множество с повторениями
    # и словарь с информацией о повторениях
    # каждого элемента множества
    return new_el_set, repeated_el_dict


def get_permutations(
    el_count,
    with_repeat=False,
    only_len_of_results=True,
    repeated_el_dict=None,
):
    """
    Функция получения размещений или их числа по заданным параметрам
     :param el_count: Количество используемых элементов во множестве
     :param with_repeat: Флаг необходимости повторений
     :param only_len_of_results: Флаг необходимости нахождения только
      количества размещений, если False - вернет все размещения
     :param repeated_el_dict: Словарь, ключом которого является повторяющийся
      элемент, а значение по ключу - количество повторений
     :return: Tuple
    """
    if not with_repeat:
        if not only_len_of_results:
            result = _permutations_without_repeat(
                el_set=range(0, el_count),
            )
        else:
            result = factorial(
                n=el_count,
            )
    else:
        el_set, repeated_el_dict = _get_repeat_settings_and_el_set(
            el_count=el_count,
            repeated_el_dict=repeated_el_dict,
        )

        if not only_len_of_results:
            result = _permutations_with_repeat(
                el_set=el_set,
            )
        else:
            # вычисляем факториал n из формулы
            fac_n = factorial(len(el_set))
            # вычисляем знаменатель из формулы
            # (применяем к каждому количеству
            # повторений функцию факториала и
            # суммируем результаты)
            znam = sum(map(
                factorial,
                repeated_el_dict.values(),
            ))

            # получаем результат
            result = fac_n // znam

    return result


def _permutations_with_repeat(el_set):
    # используем генерацию перестановок без
    # повторений, но передаем множество с повторениями
    # Парадоксально, но это приводит к правильному ответу
    return _permutations_without_repeat(
        el_set=el_set,
    )


def _permutations_without_repeat(el_set):
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
def get_placements(
    el_count,
    pos_count,
    with_repeat=False,
    only_len_of_results=True,
):
    """
    Функция получения размещений или их числа по заданным параметрам
     :param el_count: Количество используемых элементов во множестве
     :param pos_count: Количество позиций в размещении
     :param with_repeat: Флаг необходимости повторений
     :param only_len_of_results: Флаг необходимости нахождения только
      количества размещений, если False - вернет все размещения
     :return: Tuple
    """
    if not with_repeat:
        if not only_len_of_results:
            result = _placements_without_repeat(
                el_count=el_count,
                pos_count=pos_count,
            )
        else:
            fac_n = factorial(el_count)
            znam = factorial(el_count - pos_count)

            result = fac_n // znam
    else:
        if not only_len_of_results:
            result = _placements_with_repeat(
                el_count=el_count,
                pos_count=pos_count,
            )
        else:
            # колво_элементов в степени колва_позиций
            result = el_count**pos_count

    return result


def _placements_with_repeat(el_count, pos_count):
    """
    Размещение с повторениями.
    Генерирует размещение по аналогии с вычислением
    всех возможных чисел в системе счисления по
    основанию el_count с количеством разрядов в числе
    pos_count.
     :param el_count: Количество используемых элементов
      во множестве (основание системы счисления)
     :param pos_count: Количество позиций в размещении
      (количество разрядов в числе)
     :return: list[tuple]
    """
    # список счетчиков (разрядов), равны 0 в начале
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


def _placements_without_repeat(el_count, pos_count):
    """
    TODO: Неэффективный алгоритм много памяти и процессора кушац
    """
    all_placement = _placements_with_repeat(el_count, pos_count)
    results = []

    for x in all_placement:
        if len(set(x)) == pos_count:
            results.append(x)

    return results
# -------------------------------- РАЗМЕЩЕНИЯ --------------------------------


# -------------------------------- СОЧЕТАНИЯ --------------------------------
def get_combinations(
    el_count,
    pos_count,
    with_repeat=False,
    only_len_of_results=True,
):
    """
    Функция получения комбинаций или их числа по заданным параметрам
     :param el_count: Количество используемых элементов во множестве
     :param pos_count: Количество позиций в сочетании
     :param with_repeat: Флаг необходимости повторений
     :param only_len_of_results: Флаг необходимости нахождения только
      количества сочетаний, если False - вернет все сочетания
     :return:
    """
    if not with_repeat:
        if not only_len_of_results:
            result = _combinations_without_repeat(
                el_count=el_count,
                pos_count=pos_count,
            )
        else:
            fac_n = factorial(el_count)
            znam = factorial(pos_count) * factorial(el_count - pos_count)

            result = fac_n // znam
    else:
        if not only_len_of_results:
            result = _combinations_with_repeat(
                el_count=el_count,
                pos_count=pos_count,
            )
        else:
            el_count = el_count + pos_count - 1
            fac_n = factorial(el_count)
            znam = factorial(pos_count) * factorial(el_count - pos_count)

            result = fac_n // znam

    return result


def _combinations_with_repeat(el_count, pos_count):
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


def _combinations_without_repeat(el_count, pos_count):
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
