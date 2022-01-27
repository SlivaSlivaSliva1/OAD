"""
Библиотека для комбинаций с повторениями
"""
from copy import (
    copy,
)


def get_permutation(n, k):
    """
    Получает комбинации с повторениями
    :param n: Число, до которого генерируем повторения
    :param k: Длина списка с повторениями
    :return:
    """
    # массив с комбинациями
    returned_list = []
    perm_list = [0 for i in range(k)]

    while True:
        print(perm_list)
        returned_list.append(
            copy(perm_list),
        )

        for i in range(k - 1, -1, -1):
            if perm_list[i] < n - 1:
                break
        else:
            # выходим из функции когда закончили
            # создавать комбинации
            return returned_list

        perm_list[i] += 1
        for j in range(i + 1, k):
            perm_list[j] = 0



get_permutation(9, 3)
