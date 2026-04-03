import re

def f1():
    print("STUDENT REGISTRATION AND GRADING SYSTEM")

def f2(percentage, limit=20):
    if percentage > limit:
        print("Warning! Your absence is above the allowed limit.")
    else:
        print("Your absence is within the allowed limit.")

def f3(course_number, marks):
    grade = ""
    status = ""

    if marks >= 60:
        status = "Pass"
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        else:
            grade = "D"
    else:
        status = "Fail"
        grade = "F"
    return status, grade

def f4():
    try:
        cor_nm = int(input("How many courses you study? "))
    except ValueError:
        print("Error! Input should be integer")
        return 0.0

    marks_l = []
    total_gpa = 0
    
    for i in range(cor_nm):
        val = input(f"Enter mark for Course {i+1}: ")
        
        if re.findall(r'[A-Za-z]', val):
            print("Wrong input. Marks should be in numbers")
            break
            
        try:
            current_mark = float(val)
        except ValueError:
            print("Invalid format. Please enter a number.")
            break

        if current_mark < 0 or current_mark > 100:
            print("Invalid mark! Please enter a value between 0 and 100.")
            break 

        marks_l.append(current_mark)
        
        get_status = lambda m: "Pass" if m >= 60 else "Fail" 
        print(f"Status: {get_status(current_mark)}")
        
        status, grade = f3(i+1, current_mark)
        
        gpa = 0.0
        if grade == "A":
            gpa = 4.0
        elif grade == "B":
            gpa = 3.0
        elif grade == "C":
            gpa = 2.0
        elif grade == "D":
            gpa = 1.0
        else:
            gpa = 0.0
            
        total_gpa = total_gpa + gpa
        print(f"Grade: {grade} (GPA: {gpa})")

    marks_l.sort(reverse=True)
    print("Your marks:", marks_l)
    
    if cor_nm > 0:
        return total_gpa / cor_nm
    else:
        return 0.0
