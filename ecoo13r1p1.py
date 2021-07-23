current_number = int(input())
student_status = " "
late_students = 0
students_served = 0
late_served = 0

while "EOF" not in student_status:
    if current_number == 1000:
        current_number = 1
    student_status = " " 
    late_students = 0
    late_served = 0
    students_served = 0
    while student_status != "CLOSE":
        student_status = input()
        if student_status == "TAKE":
            late_students += 1
            current_number += 1
        if current_number == 1000:
            current_number = 1
        if student_status == "SERVE":
            students_served += 1
        if student_status == "CLOSE":
            late_served = late_students - students_served
            print(str(late_students) + " " + str(late_served) + " " + str(current_number))
        if student_status == "EOF":
            break
    if student_status == "EOF":
        break    
        
        