sentence = input()
count_happy = sentence.count(":-)")
count_sad = sentence.count(":-(")

if count_happy == 0 and count_sad == 0:
    print("none")
elif count_happy == count_sad:
    print("unsure")
elif count_happy>count_sad:
    print("happy")
elif count_happy<count_sad:
    print("sad")