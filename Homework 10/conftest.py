import time
import pytest


@pytest.fixture(scope='class')
def time_class():
    """Выводим время начала и окончания выполнения класса с тестами"""
    print(f'Время начала выполнения класса с тестами: {time.strftime("%H:%M:%S", time.localtime())}')
    yield
    print(f'\nВремя окончания выполнения класса с тестами: {time.strftime("%H:%M:%S", time.localtime())}')


@pytest.fixture()
def time_tests():
    """Выводим время выполнения теста"""
    start = time.time()
    yield
    end = time.time()
    print(f'\nВремя выполнения теста {end - start}')