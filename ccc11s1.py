number_of_lines = int(input())
lines = [""]*number_of_lines
count_of_t = 0
count_of_s = 0
for i in range(0, number_of_lines):
    lines[i] = input()

for l in lines:
    for c in l:
        if c == "t" or c == "T":
            count_of_t += 1
        elif c == "s" or c == "S":
            count_of_s += 1
            
if count_of_t>count_of_s:
    print("English")
elif count_of_t<count_of_s:
    print("French")
elif count_of_t==count_of_s:
    print("French")