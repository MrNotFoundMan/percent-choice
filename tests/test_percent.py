#``` bash: pip install percent_choice \n pip install pytest
import pytest
from percent_choice import Percent, SecurePercent


# =========================
# Percent
# =========================

def test_percent_returns_allowed_object():
    chance = Percent(
        ["green", "blue", "red"],
        [10, 30, 60]
    )

    result = chance.get()

    assert result in {"green", "blue", "red"}


def test_percent_returns_correct_objects_many_times():
    chance = Percent(
        ["green", "blue", "red"],
        [10, 30, 60]
    )

    for _ in range(10_000):
        result = chance.get()

        assert result in {"green", "blue", "red"}


def test_percent_empty_objects():
    with pytest.raises(ValueError):
        Percent([], [])


def test_percent_different_lengths():
    with pytest.raises(ValueError):
        Percent(
            ["green", "blue", "red"],
            [50, 50]
        )


def test_percent_chances_must_be_100():
    with pytest.raises(ValueError):
        Percent(
            ["green", "blue"],
            [30, 30]
        )


def test_percent_chances_cannot_be_negative():
    with pytest.raises(TypeError):
        Percent(
            ["green", "blue", "red"],
            [50, -10, 60]
        )


def test_percent_chances_must_be_int():
    with pytest.raises(TypeError):
        Percent(
            ["green", "blue"],
            [50, 50.0]
        )
from percent_choice import Percent,SecurePercent
#для того чтобы работать с моим модулем нужно передать список с названиями класами и так далее
#затем надо передать список с процентами, 0 индекс в первом списке равен 0 индексу во втором списке

#To work with my module, you need to pass a list containing class, names and so on.
#Then you need to pass the list of percentages; the element at index 0 in the first list corresponds to the element at index 0 in the second list.
choice = Percent(["Common","Uncommon","Rare","Epic","Mythical","Legendary"],[40,30,20,8.99,1,0.01])
#например шанс у Common равен 40% так как индекс 0 в первом списке равен индексу 0 во втором
#For example, the chance for "Common" is 40%, since index 0 in the first list corresponds to index 0 in the second.



#тест на время милион итераций всего за 0.42462172900013684 Timing test: a million iterations in just 0.42462172900013684.
"""import time
start = time.perf_counter()
for _ in range(1_000_000):
    choice.get()
end = time.perf_counter()
print(end - start)"""





#тест на работу процентов  Percentage calculation test
"""from collections import Counter
results = Counter(choice.get() for _ in range(1_000_000))
print(results)
for name, count in results.items():
    print(name,count / 1_000_000 * 100,"%")"""
#за милион раз прокручиваний получились такие ответы  After running through the process a million times, these are the answers I got.
#Counter({'Common': 399745, 'Uncommon': 300666, 'Rare': 199788, 'Epic': 89733, 'Mythical': 9972, 'Legendary': 96})
# такой ответ + - он совпадает  This answer matches + - .
"""Common 39.960699999999996 %
Epic 9.006599999999999 %
Uncommon 29.976999999999997 %
Rare 20.0342 %
Mythical 1.0109 %
Legendary 0.0106 %"""

# =========================
# SecurePercent
# =========================

def test_secure_percent_returns_allowed_object():
    chance = SecurePercent(
        ["green", "blue", "red"],
        [10, 30, 60]
    )

    result = chance.get()

    assert result in {"green", "blue", "red"}


def test_secure_percent_returns_correct_objects_many_times():
    chance = SecurePercent(
        ["green", "blue", "red"],
        [10, 30, 60]
    )

    for _ in range(10_000):
        result = chance.get()

        assert result in {"green", "blue", "red"}


def test_secure_percent_empty_objects():
    with pytest.raises(ValueError):
        SecurePercent([], [])


def test_secure_percent_different_lengths():
    with pytest.raises(ValueError):
        SecurePercent(
            ["green", "blue", "red"],
            [50, 50]
        )


def test_secure_percent_chances_must_be_100():
    with pytest.raises(ValueError):
        SecurePercent(
            ["green", "blue"],
            [30, 30]
        )


def test_secure_percent_chances_cannot_be_negative():
    with pytest.raises(TypeError):
        SecurePercent(
            ["green", "blue", "red"],
            [50, -10, 60]
        )


def test_secure_percent_chances_must_be_int():
    with pytest.raises(TypeError):
        SecurePercent(
            ["green", "blue"],
            [50, 50.0]
        )


#test 2
from collections import Counter


def test_percent_distribution():
    chance = Percent(
        ["green", "blue", "red"],
        [10, 30, 60]
    )

    results = Counter(
        chance.get()
        for _ in range(100_000)
    )

    green_percent = results["green"] / 100_000
    blue_percent = results["blue"] / 100_000
    red_percent = results["red"] / 100_000

    assert 0.09 <= green_percent <= 0.11
    assert 0.29 <= blue_percent <= 0.31
    assert 0.59 <= red_percent <= 0.61

def test_secure_percent_distribution():
    chance = SecurePercent(
        ["green", "blue", "red"],
        [10, 30, 60]
    )

    results = Counter(
        chance.get()
        for _ in range(100_000)
    )

    green_percent = results["green"] / 100_000
    blue_percent = results["blue"] / 100_000
    red_percent = results["red"] / 100_000

    assert 0.09 <= green_percent <= 0.11
    assert 0.29 <= blue_percent <= 0.31
    assert 0.59 <= red_percent <= 0.61