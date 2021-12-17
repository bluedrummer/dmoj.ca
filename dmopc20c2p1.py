number_of_days = int(input())
net_worth_change = input()
max_number = 0
current = 0
min_number = 0
number_of_rows = 0
starting_row = 0

for i in range(0, len(net_worth_change)):
    if net_worth_change[i] == "^":
        if i > 0:
            if net_worth_change[i-1] == "^":
                current += 1
    if net_worth_change[i] == "v":
        if i > 0:
            if net_worth_change[i-1] == "v":
                current -= 1
            if net_worth_change[i-1] == ">":
                current -= 1
    if net_worth_change[i] == ">":
        if i > 0:
            if net_worth_change[i-1] == "^":
                current += 1
    if current > max_number:
        max_number = current
    if current < min_number:
        min_number = current

number_of_rows = abs(min_number) + abs(max_number) + 1
starting_row = max_number
chart = [ ["."]*number_of_days for i in range(number_of_rows)]

col = 0
row = starting_row

for n in range(0, len(net_worth_change)):
    if net_worth_change[col] == "^":
        chart[row][col] = "/"
        if col < (len(net_worth_change)-1):
            if net_worth_change[col+1] == "^":
                row -= 1
            if net_worth_change[col+1] == ">":
                row -= 1
    if net_worth_change[col] == "v":
        chart[row][col] = "\\"
        if col < (len(net_worth_change)-1):
            if net_worth_change[col+1] == "v":
                row += 1
    if net_worth_change[col] == ">" :
        chart[row][col] = "_"
        if col < (len(net_worth_change)-1):
            if net_worth_change[col+1] == "v":
                row += 1
    col += 1


for l in range(0, number_of_rows):
    print(''.join(chart[l]))
