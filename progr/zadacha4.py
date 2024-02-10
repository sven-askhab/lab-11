#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    """
    Возвращает введённую строку
    """
    user_input = input("Введите строку: ")
    return user_input


def test_input(value):
    """
    Возвращает True, если значение возможно преобразовать в int, иначе False.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    """
    Возвращает преобразованное значение в целочисленный тип.
    """
    return int(value)


def print_int(value):
    """
    Выводит значение в консоль.
    """
    print(value)


if __name__ == '__main__':
    input_str = get_input()

    if test_input(input_str):
        integer_value = str_to_int(input_str)
        print_int(integer_value)
    else:
        print("Введенное значение не может быть преобразовано в целое число.")