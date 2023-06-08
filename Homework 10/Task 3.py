# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args, result', [
    ([0, 1, 2, 3], 0),
    pytest.param([15, 5, 2, 1], 1.5, marks=pytest.mark.smoke)])
def test_positive(args, result):
    assert all_division(*args) == result


@pytest.mark.parametrize('args, result', [
    pytest.param([1, 2, 0, 3], ZeroDivisionError, marks=pytest.mark.skip('zero division test')),
    ([1, '2', 3, 4], TypeError),
    ([], IndexError)])
def test_negative(args, result):
    with pytest.raises(result):
        all_division(*args)
