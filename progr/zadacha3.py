#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply():
    """
    Перемножает введенные числа, до введения 0
    """
    result = 1
    while True:
        number = float(input("Введите число (введите 0 для завершения): "))
        if number == 0:
            break
        result *= number
    return result


if __name__ == '__main__':
    product = multiply()
    print(f"Произведение введенных чисел: {product}")