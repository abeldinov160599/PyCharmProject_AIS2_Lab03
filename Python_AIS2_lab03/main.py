#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m, max_value=21):
    array = [] # основной массив
    for i in range(0, n):
        sub_array = [] # подмассив с числами
        for j in range(m):
            # от минимального числа (-20) до максимального -1 (max_value - 1 = 20) с шагом (1)
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number) # добавление случайного числа в подмассив
        array.append(sub_array) # добавление подмассива в массив
    return array # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array: # перебор по подмассивам(строкам)
        for j in i: # перебор по элементам строк
            print("%5.1f\t" % j, end='')
        print()


# функция для нахождения элементов условия (в этом случае максимум и минимум,
# может быть количество нулей, количество отрицательных числе и т.д.)
def counting(array):
    print()
    # как начальное значение для макс/мин берется первый элемент массива
    max_value = array[0][0]
    min_value = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] > max_value:
                max_value = array[i][j]
                max_i = i
                max_j = j
            if array[i][j] < min_value:
                min_value = array[i][j]
                min_i = i
                min_j = j
    print("Максимум: %d, минимум: %d, индексы максимума: %d, %d, индексы минимума: %d, %d" % (max_value, min_value, max_i, max_j, min_i, min_j))
    print()
    return max_value, min_value, max_i, max_j, min_i, min_j


def main():
    array = random_array(4, 5) # можно изменить размер
    print("Условие задания:\n"
          "Если сумма элементов массива больше ста,\n"
          "то поменять максимальный и минимальный элемент местами")
    # вызов функции вывода массива
    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    max_value, min_value, max_i, max_j, min_i, min_j = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1': # рандом, вывод и новые значения по условию нового массива
            array = random_array(4, 5)
            print_array(array)
            max_value, min_value, max_i, max_j, min_i, min_j = counting(array)
        elif key == '2':
            s = 0
            for i in range(len(array)):
                for j in range(len(array[i])):
                    s += array[i][j]

            # проверка выполнения условия
            if (s) < 100:
                print("Сумма элементов массива (%d) не больше ста " % (s))
                print("Задание не будет выполнено.")
            else:
                print("Cумма элементов массива больше ста (%d)" % (s))
                array[min_i][min_j], array[max_i][max_j] = array[max_i][max_j], array[min_i][min_j]
                print("Минимальный и максимальный элемент поменялись местами.")
                print_array(array)
                break # выход из цикла
        elif key == '3':
            exit(0) # выход из программы


if __name__ == '__main__':
    main()
