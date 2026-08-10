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