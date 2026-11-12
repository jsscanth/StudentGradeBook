from decimal import Decimal

from main import get_average, highest_grade, lowest_grade, letter_grade


# Tests for get_average()
def test_get_average():
    assert get_average([80, 90, 100]) == 90


def test_get_average_with_decimal_values():
    assert get_average([Decimal("80"), Decimal("90"), Decimal("100")]) == 90


def test_get_average_with_one_grade():
    assert get_average([75]) == 75


# Tests for highest_grade()
def test_highest_grade():
    assert highest_grade([70, 90, 80]) == 90


def test_highest_grade_when_all_grades_are_equal():
    assert highest_grade([80, 80, 80]) == 80


# Tests for lowest_grade()
def test_lowest_grade():
    assert lowest_grade([70, 90, 80]) == 70


def test_lowest_grade_when_all_grades_are_equal():
    assert lowest_grade([80, 80, 80]) == 80


# Tests for letter_grade()
def test_letter_grade_a():
    assert letter_grade(Decimal("90")) == "A"


def test_letter_grade_b():
    assert letter_grade(Decimal("80")) == "B"


def test_letter_grade_c():
    assert letter_grade(Decimal("70")) == "C"


def test_letter_grade_d():
    assert letter_grade(Decimal("60")) == "D"


def test_letter_grade_f():
    assert letter_grade(Decimal("59")) == "F"


def test_letter_grade_at_upper_boundary():
    assert letter_grade(Decimal("89.99")) == "B"
