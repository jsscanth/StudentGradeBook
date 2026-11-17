from decimal import Decimal, InvalidOperation


def get_letter_grade(grade: Decimal):
    """Getting the letter grade based on student average grade.

    Args:
        grade (decimal): student average grade

    Returns:
        _type_: string of letter grade.
    """
    if grade >= Decimal("90"):
        return "A"
    elif grade >= Decimal("80"):
        return "B"
    elif grade >= Decimal("70"):
        return "C"
    elif grade >= Decimal("60"):
        return "D"
    else: return "F"

def get_average(grades: list):
    """Calculate average of student's grade and return the average.

    Args:
        grades (list): list of grade.

    Returns:
        _type_: Decimal
    """
    n = Decimal('0')
    for grade in grades:
        n += grade
        
    return n/len(grades) 

def type_check_grade(grade: Decimal):
    """Making sure the grade is in between of 0 and 100

    Args:
        grade (int): _description_
        
    Returns:
        type: 
    """
    if grade < 0:
        return "Grade is less than 0"
    elif grade > 100:
        return "Grade is more than 100"

def add_grade(book:dict, name:str, grade: str):
    """Adding grade to book.

    Args:
        book (dict): copy of current book
        name (str): name of student
        grade (int): grade of student

    Returns:
        _type_: dictionary of book after grade is written
    """
    book[name].append(Decimal(grade))
    return book

def type_check_name(book:dict, name: str):
    """Checking the current situation of name in book. Whether name is exist or not and making sure that name cannot be number.

    Args:
        book (dict): copy of current book 
        name (str): input of the name

    Returns:
        _type_: string
    """
    if name.isnumeric():
        return "Name is number(s)"
    elif name in book:
        return "Name is already exist"
    else:
        return "Name is not exist"
    

def add_student(book: dict, name: str):
    book[name] = []
    return book    

def main():
    book = {}
    option = 0
    while option != 5:
        print("====== GRADE BOOK ======")
        print("1. Add Student")
        print("2. Add Grade for A Student")
        print("3. View Student Report")
        print("4. View Class Summary")
        print("5. Exit")
        print("Student list:")
        print(f"{book}")
        
        try:
            option = int(input("Enter your option >>> ").strip())
            if option < 1 or option > 5:
                print("Enter the correct option >>> ")
                continue
        except ValueError:
            print("Enter the correct option >>> ")
            continue
            
        if option == 1:
            while True:
                name = ""
                try:
                    name = input("Enter student name: ").lower().strip()
                    if name == "":
                        break
                    else:
                        check = type_check_name(book, name)
                        if check == "Name is number(s)":
                            print("Enter new name. Name cannot be number.")
                        elif check == "Name is already exist":
                            print("Enter new name. Name already exist.")
                        elif check == "Name is not exist":
                            book = add_student(book, name) 
                            print(book)
                            break
                except (ValueError, TypeError):
                    print("Enter the correct name")
                    continue
        elif option == 2:
            while True:
                if not book:
                    print("Book grade is empty.")
                    break
                else:
                    try:
                        name = input("Enter student name: ").lower().strip()
                        check = type_check_name(book, name)
                        if name == "":
                            break
                        elif check == "Name is number(s)":
                            print("Enter the right name. Name cannot be number.")
                        elif check == "Name is not exist":
                            print("Please enter name again. Name is not exist")
                        elif check == "Name is already exist":
                            while True:
                                try:
                                    grade = input("Enter student grade: ").strip()
                                    if grade == "":
                                        break
                                    check = type_check_grade(Decimal(grade))
                                    if check == "Grade is less than 0":
                                        print("Grade cannot be less than zero. Please enter student grade again")
                                    elif check == "Grade is more than 100":
                                        print("Grade cannot be more than 100. Please enter student grade again.")
                                    else:
                                        book = add_grade(book, name, grade)
                                except(ValueError, InvalidOperation):
                                    print("Please enter the right grade.")
                    except (ValueError, TypeError):
                        print("Enter the right name.")
        elif option == 3:
            if not book:
                print("Grade book is empty.")
            else:
                for name, grade in book.items():
                    if grade:
                        print(f"{name.capitalize()}: {[float(value) for value in grade]}")
                    else:
                        print(f"{name.capitalize()}: No grades yet.")
                average_book = {name:get_average(grade) for name, grade in book.items() if grade}
                average_list = []
                # checking student grade and getting its average
                for name, grade in average_book.items():
                    average_list.append(grade)
                # Show the highest and lowest of average grade
                for name, grade in average_book.items():
                    if grade == max(average_list):
                        print(f"Highest average grade: {name.capitalize()}   {grade:.2f}")
                    if grade == min(average_list):
                        print(f"Lowest average grade: {name.capitalize()}    {grade:.2f}")
                # Show the letter grade of after the average grade.
                print("Average Letter Grade")
                for name, grade in average_book.items():
                    print(f"{name.capitalize()}: {get_letter_grade(grade)}")
        elif option == 4:
            if not book:
                print("Grade book is empty")
            else:
                average_book = {name:get_average(grade) for name, grade in book.items() if grade}
                average_list = []
                if not average_book:
                    print("No grades yet.")
                else:
                    # checking student grade and getting its average
                    for name, grade in average_book.items():
                        average_list.append(grade)
                    # Getting class average
                    class_average = get_average(average_list)
                    print(f"Class average: {class_average:.2f}")
                    # Top student
                    for name, grade in average_book.items():
                        if grade == max(average_list):
                            print(f"Top student: {name.capitalize()} {grade:.2f}")
                    # ranking
                    print("Class Rank")
                    ranked = sorted(average_book.items(), key= lambda pair:pair[1], reverse=True)
                    for key, value in ranked:
                        print(f"{key.capitalize()}: {value:.2f}")
            
    
if __name__ == "__main__":   
    main()