4#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    """
    Вычисляет либо полную площадь цилиндра либо площадь боковой поверхности.
    """

    def circle(r):
        """
        Вычисляет площадь круга.
        """
        return math.pi * r ** 2


    r = float(input("Введите радиус цилиндра: "))
    h = float(input("Введите высоту цилиндра: "))

    side_area = 2 * math.pi * r * h

    sw = input(
        "Если вы хотите найти полную площадь цилиндра - введите 1\n" +
        "Площадь боковой поверхности цилиндра - введите любой другой символ\n"
        )

    if sw == "1":
        base_area = circle(r)
        full_area = side_area + 2 * base_area
        print(f"Полная площадь цилиндра: {full_area:.2f}")
    else:
        print(f"Площадь боковой поверхности цилиндра: {side_area:.2f}")


if __name__ == '__main__':
    cylinder()