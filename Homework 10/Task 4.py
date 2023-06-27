# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('time_class')
class TestClass:

    @pytest.mark.parametrize('args, result', [
        ([0, 1, 2, 3], 0),
        pytest.param([15, 5, 2, 1], 1.5, marks=pytest.mark.smoke)])
    def test_positive(self, args, result, time_tests):
        time.sleep(2)
        assert all_division(*args) == result

    @pytest.mark.parametrize('args, result', [
        pytest.param([1, 2, 0, 3], ZeroDivisionError, marks=pytest.mark.skip('zero division test')),
        ([1, '2', 3, 4], TypeError),
        ([], IndexError)])
    def test_negative(self, args, result):
        with pytest.raises(result):
            all_division(*args)