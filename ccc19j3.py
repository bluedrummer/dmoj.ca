number_of_lines = int(input())

for i in range(0, number_of_lines):
    line = input()
    if line == "":
        print(line)
        continue
    previous_character = ""
    current_count = 0
    encoded_line = ""
    for c in line:
        if previous_character == c:
            current_count += 1
        elif previous_character != c and previous_character != "":
            encoded_line = encoded_line + str(current_count) + " " + previous_character + " "
            current_count = 1
            previous_character = c
        else:
            previous_character = c
            current_count += 1
    encoded_line = encoded_line + str(current_count) + " " + previous_character + " "
    print(encoded_line)      

