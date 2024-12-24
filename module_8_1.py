def add_everything_up(a,b):
    try:
        #  Записываем сложение переменных по правилам конкатенации и по правилам сложения
        # целых чисел и чисел с плавающей точкой
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        #  Оператор raise позволяет нам сигнализировать о возникновении ошибки или
        # неправильной ситуации в нашей программе, а именно, во всех остальных случаях,
        # оператор raise запускает TypeError - когда a и b окажутся разными типами
        # (числом и строкой), которые не описаны выше, а это -
        # (a, (int, float)) + (b, str) или (a, str) + (b, (int, float))
        else:
            raise TypeError
    except TypeError:
        #  Возвращаем строковое представление этих двух данных вместе (в том же порядке),
        # независимо от типа ввода данных в программу
        return f'{str(a)},{str(b)}'



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

#   Иногда необходимо перехватить одно исключение и запустить другое, предоставляя более
#   специфичную или полезную информацию. Это можно сделать с помощью оператора raise ... from,
#   который сохраняет исходное исключение в качестве причины для нового.
#   raise новое_исключение from старое_исключение

# class EmptyVariableError(Exception):
#     pass
#
# def check_non_empty(value):
#     if value == "":
#         raise ValueError("The variable is empty")
#
# try:
#     check_non_empty("")
# except ValueError as e:
#     raise EmptyVariableError("Empty variable detected") from e