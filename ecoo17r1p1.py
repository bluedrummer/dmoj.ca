costs = [12, 10, 7, 5]

for n in range(0, 10):
    money = 0
    students_each_year = []
    cost_of_trip = int(input())
    student_years = input().split()
    number_of_students = int(input())
    
    for i in range(len(student_years)):
        student_years[i] = float(student_years[i])
        
    for c in student_years:
        student = round(number_of_students*c + 0.5)
        students_each_year.append(student)
        
    for i in range(0, len(students_each_year)):
        money = money + students_each_year[i]*costs[i]
        
    if (money / 2) < cost_of_trip:
        print("YES")
    else:
        print("NO")
    
   

    
