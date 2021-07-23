number_of_questions = int(input())
answers = input()
scores = {'Adrian':0, 'Bruno':0, 'Goran':0}
adrian_answer = "ABC"*34
bruno_answer = "BABC"*25
goran_answer = "CCAABB"*17

for i in range(0, number_of_questions):
    if adrian_answer[i] == answers[i]:
        scores['Adrian'] += 1
    if bruno_answer[i] == answers[i]:
        scores['Bruno'] += 1
    if goran_answer[i] == answers[i]:
        scores['Goran'] += 1


