
# Importing Prettytable to display the result of the code in a tabular format

from prettytable import PrettyTable

name = input("Enter your full name: ").upper()

# Function to accept the courses and the course units, via user input, and collating them into a dictionary

def courses():
    course_dict = {}
    n = int(input("Enter number of courses offered: "))
    for i in range(n):
        course = input(f"Course {i + 1}: ").upper()
        num = int(input(f"Unit {i + 1}: "))
        print()
        course_dict[course] = num
    return course_dict


# Function to calculate CGPA

def cgpa():
    grade_list = []
    total_course_unit = 0
    course_unit = 0
    course = courses()
    print(course)
    print()
    
    for index, item in enumerate(course):
        grade = (input(f"Grade for {item}: ")).upper()
        print()
        grade_list.append(grade)
        
        if grade.isalpha():
            if grade == "A":
                unit = 4 * course[item]
            elif grade == "B":
                unit = 3 * course[item]
            elif grade == "C":
                unit = 2 * course[item]
            elif grade == "D":
                unit = 1 * course[item]
            else:
                unit = 0 * course[item]
        else:
            break
        
        course_unit += course[item]
        total_course_unit += unit

# Displaying the table 

    table = PrettyTable()
    table.title = name
    table.field_names = ["COURSE", "UNIT", "GRADE"]
    for (key, value), lst in zip(course.items(), grade_list):
        table.add_row([key, value, lst])
    print(table)

# Printing the total course units, course units, and cgpa

    print(f"Total course unit = {total_course_unit}")
    print(f"Course unit = {course_unit}")

# Rounding off the cgpa to 2 decimal places

    cgpa = round((total_course_unit / course_unit), 2)
    return(f"CGPA: {cgpa}")

# Calling the function

print(cgpa())
        
