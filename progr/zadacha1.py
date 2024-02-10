#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    """
    Запросить целое число и вызвать соответствующую функцию.
    """
    num = int(input("Введите целое число: "))
    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        return


def positive():
    """
    Вывести на экран 'Положительное'.
    """
    print("Положительное")


def negative():
    """
    Вывести на экран 'Отрицательное'.
    """
    print("Отрицательное")


if __name__ == '__main__':
    test()