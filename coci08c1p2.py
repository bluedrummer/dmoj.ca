number_of_questions = int(input())
answers = input()
adrian = 0
bruno = 0
goran = 0
adrian_answer = "ABC"*34
bruno_answer = "BABC"*25
goran_answer = "CCAABB"*17

for i in range(0, number_of_questions):
    if adrian_answer[i] == answers[i]:
        adrian += 1
    if bruno_answer[i] == answers[i]:
        bruno += 1
    if goran_answer[i] == answers[i]:
        goran += 1
        
if adrian > bruno and adrian > goran:
    print(adrian)
    print("Adrian")
if bruno > adrian and bruno > goran:
    print(bruno)
    print("Bruno")
if goran > adrian and goran > bruno:
    print(goran)
    print("Goran")
    
if adrian == bruno and adrian > goran:
    print(adrian)
    print("Adrian")
    print("Bruno")
if adrian == goran and adrian > bruno:
    print(adrian)
    print("Adrian")
    print("Goran")
if bruno == goran and bruno > adrian:
    print(bruno)
    print("Bruno")
    print("Goran")
if adrian == bruno and bruno == goran:
    print(adrian)
    print("Adrian")
    print("Bruno")
    print("Goran")


    
    
