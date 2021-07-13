number_of_questions =int(input())
student_answers = [""]*number_of_questions
correct_answers = [""]*number_of_questions
score = 0
for i in range(0, number_of_questions):
    student_answers[i] = input()
for i in range(0, number_of_questions):
    correct_answers[i] = input()
for i in range(0, number_of_questions):
    if student_answers[i] == correct_answers[i]:
        score += 1

print(score)
        