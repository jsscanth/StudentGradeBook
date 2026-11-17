from decimal import Decimal

from main import get_letter_grade, get_average, type_check_grade, add_grade, type_check_name, add_student

def test_letter_grade_boundaries():
    assert get_letter_grade(Decimal("90")) == "A"
    assert get_letter_grade(Decimal("89.99")) == "B"
    assert get_letter_grade(Decimal("75")) == "C"
    assert get_letter_grade(Decimal("60")) == "D"
    assert get_letter_grade(Decimal("59")) == "F"
    assert get_letter_grade(get_average([Decimal("89.99")])) == "B"

def test_average():
    assert get_average([Decimal("90"), Decimal("90")]) == Decimal("90")
    assert get_average([Decimal("85"), Decimal("90"), Decimal("80")]) == Decimal("85")
    assert get_average([Decimal("89.99")])

def test_check_name():
    book = {"ana": []}
    assert type_check_name(book, "ana") == "Name is already exist" 
    assert type_check_name(book, "90") == "Name is number(s)"
    assert type_check_name(book, "ben") == "Name is not exist"
    
def test_check_grade():
    assert type_check_grade(Decimal("101")) == "Grade is more than 100"
    assert type_check_grade(Decimal("-5")) == "Grade is less than 0"
    assert type_check_grade(Decimal("0")) == None
    assert type_check_grade(Decimal("100")) == None
    
def test_add_student_grades():
    book = {}
    assert add_student(book, "ana") == {"ana": []}
    assert add_grade(book, "ana", "89.99") == {"ana": [Decimal("89.99")]} 
