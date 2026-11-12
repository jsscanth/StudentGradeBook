from decimal import Decimal, InvalidOperation
import math

def menu(): # showing menu
    option = 0
    while True:
        print("====== Grade Book ======")
        print("1. Add student")
        print("2. Add grade for a student")
        print("3. View student report")
        print("4. View class summary")
        print("5. Exit")
        try:
            option = int(input("Choose an option: "))
            if option < 1 or option > 5:
                print("Enter the correct number of option")
                continue
            else:
                break
        except ValueError:
            print("Enter the correct option from menu.")  
    return option   
    

def main():
    book = {} # where the name and grades are stored
    average_dict = {} # where the name and average of grades are stored
    all_average_grade = [] # where all average grade of the class is stored
    average_list = [] # where only average is contained
    name = "" # to store name temporarily
    grade = 0 # to store grade temporarily
    
    while True: # keep the program running until option 5 quit is executed.
        option = menu()
        if option == 5:
            break
        
        elif option == 1:
            while True:
                name = input("Enter student name (type 101 exit): ").lower().strip()
                if name == "101":
                    break
                elif name.isnumeric(): # check if the given name is number 
                    print("Name cannot be number")
                elif name in book: # check if the name already exist
                    print(f"{name.capitalize()} already exist")
                else:
                    book[name] = [] # assign the name to book record.
                    break
            
            print(f"List of name so far:")
            for key, value in book.items():
                print(f"- {key}: {value}")
                    
        elif option == 2:
            while True: # keep the input running until the name is found.
                name = input("Enter student name: ").lower().strip()
                if name not in book:
                    print("Name cannot be found.")
                    continue
                else: break
            while True: # keep the input running until the input grade is right.
                try:
                    grade = Decimal(input("Enter student grade (type 101 to exit): "))
                    if not grade.is_finite():
                        print("Enter the correct grade.")
                        continue
                    if grade == 101: 
                        break
                    elif grade < 0 or grade > 100:
                        print("Enter the correct grade.")
                        continue
                    else: book[name].append(grade)

                except (ValueError, InvalidOperation):
                    print("Enter the right name and grade")
            
        elif option == 3:
            print("====== All Grades ======")
            for x, y in book.items(): # showing all grades
                print(f"{x.capitalize()}: {[float(z) for z in y]}")
            print("-----------------------")
            print("====== Average ======")
            for name, grade in book.items(): # show name and average grade of name.
                average_dict[name] = get_average(grade) # keeping the average to another dictionary.
                print(f"{name.capitalize()}: {average_dict[name]: .2f}")
            print("=====================")
            
            average_list = [grade for grade in average_dict.values()] # store list of average grades only
            highest = highest_grade(average_list) # store the highest grade
            lowest = lowest_grade(average_list) # store the lowest grade
            highest_name_list = [key for key, value in average_dict.items() if value == highest] # store the name of student with highest grade
            lowest_name_list = [key for key, value in average_dict.items() if value == lowest] # store the name of students with lowest grade
            for name in highest_name_list:
                print(f"Highest Average Grade   {name}: {highest: .2f}")
            
            for name in lowest_name_list:
                print(f"Lowest Average Grade    {name}: {lowest: .2f}")           
            
            print("====== Letter Grades ======")
            for name, grade in average_dict.items():
                print(f"{name}: {letter_grade(grade)}")
            print("===========================")
            
            # for name, grade in book.items():
            #     print("For loop is good")
            #     print(f"{name.capitalize()}: {str(grade)}")
                
        elif option == 4:
            # Show class average
            if average_dict == []:
                print("Choose option 3 first to count student average")
            else:
                for grade in average_dict.values():
                    all_average_grade.append(grade)
                average_class = get_average(all_average_grade)
                print(f"Class average: {average_class}")
                
                # show highest class average
                highest = highest_grade(average_list) # store the highest grade
                print(f"Highest grade: {highest}")
                
                # list all average score sequencely from highest to lowest
                print("Highest Average to Lowest")
                for grade in average_list:
                    for name in average_dict.keys():
                        if average_dict[name] == grade:
                            print(f"{name.capitalize()}: {grade: .2f}")
                    
                
            
            
            

def get_average(grades):
    return math.fsum(grades)/len(grades)

def highest_grade(grades):
    return max(grades)

def lowest_grade(grades):
    return min(grades)

def letter_grade(grades):
    if grades >= Decimal("90"):
        return "A"
    elif grades >= Decimal("80"):
        return "B"
    elif grades >= Decimal("70"):
        return "C"
    elif grades >= Decimal("60"):
        return "D"
    else: return "F"
    


if __name__ == "__main__":
    main()
    

'''
notes:
[v] fix option 2. can the variable 'name' be really used outside while loop?
[v] can option 2 receive more than one grades at once? using while loop until the user input 101 to exit the loop?
[v] option 3: how to show grades without 'Decimal' show up as an output
[v] option 3: how to show list without '[]' around the values.
[v] option 4: finish it
[v] option 4: store all grade in a single variable and count its average
[v] option 4: show highest class average
[v] option 4: list the average score form highest to lowest
'''
