#!usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils import command
import sys
from datetime import date

def add_train(trains):
    """
    Добавить поезд.
    """
    train_number = input("Номер поезда: ")
    destination = input("Название пункта назначения: ")
    departure_time = input("Время отправления: ")

    train_info = {'номер поезда': train_number,
                  'название пункта назначения': destination,
                  'время отправления': departure_time}

    trains.append(train_info)

    if len(trains) > 1:
        trains.sort(key=lambda x: x['номер поезда'])


def list_trains(trains):
    """
    Отобразить список поездов.
    """
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print('| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
        "№",
        "Номер поезда",
        "Пункт назначения",
        "Время"
    ))
    print(line)

    for idx, train_info in enumerate(trains, 1):
        print('| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
            idx,
            train_info.get('номер поезда', ''),
            train_info.get('название пункта назначения', ''),
            train_info.get('время отправления', '')
        ))

    print(line)

def select_train(trains):
    """
    Выбрать поезд с заданным номером.
    """
    search_train_number = input("\nВведите номер поезда для поиска: ")
    found_train = None
    for train in trains:
        if train["номер поезда"] == search_train_number:
            found_train = train
            print(found_train)
            break

    if found_train is None:
        print(f"\nПоезда с номером {search_train_number} не найдено.")


def help_command():
    """
    Отобразить список команд.
    """
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("select - запросить поезд по номеру;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def main():
    """
    Главная функция программы.
    """
    trains = []

    while True:
        user_input = input(">>> ").lower()

        if user_input == 'exit':
            break

        elif user_input == 'add':
            add_train(trains)

        elif user_input == 'list':
            list_trains(trains)

        elif user_input == 'select':
            select_train(trains)

        elif user_input == 'help':
            help_command()

        else:
            print(f"Неизвестная команда {user_input}", file=sys.stderr)


if __name__ == '__main__':
    main()