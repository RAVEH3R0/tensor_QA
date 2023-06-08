# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    """
    Генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
    """
    while True:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        string_one = ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
        string_two = ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
        yield string_one + ' ' + string_two


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
