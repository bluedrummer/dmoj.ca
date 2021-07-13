nb_of_times_butt_is_pressed = int(input())
previous = "A"
current = ""
for k in range(0, nb_of_times_butt_is_pressed):
    for c in previous:
        if c == "A":
            current = current + "B"
        elif c == "B":
            current = current + "BA"
    previous = current
    current = ""
    print(k)
count_of_a = previous.count("A")
count_of_b = previous.count("B")

print(str(count_of_a) + " " + str(count_of_b))