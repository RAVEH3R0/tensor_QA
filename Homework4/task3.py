# Напишите функцию sum_digits, которая принимает положительное число num,
# и возвращает сумму цифр our_sum.
# Например (Ввод --> Вывод) :
#
# 39 --> 12
# 999 --> 27
# 4 --> 4

def sum_digits(num):
    """
    Функция sum_digits принимает положительное число num, и возвращает сумму цифр our_sum
    :param num: Положительное число
    :return: (our_sum) Сумма цифр
    """
    if num < 10:
        return num
    else:
        our_sum = num % 10 + sum_digits(num // 10)
        print(our_sum)
    return our_sum

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    12, 4, 7, 27, 10, 27
]


for i, d in enumerate(data):
    assert sum_digits(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
