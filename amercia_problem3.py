input_file = open('citystate.in', 'r')
output_file = open('citystate.out', 'w')
n = int(input_file.readline())
combo_to_num = {}
for i in range(0,n):
    lst = input_file.readline().split()
    city = lst[0][:2]
    state = lst[1]
    if city != state:
        combo = city + state
        if not combo in combo_to_num:
            combo_to_num[combo] = 1
        else:
            combo_to_num[combo] = combo_to_num[combo] + 1
total = 0

for combo in combo_to_num:
    other_combo = combo[2:] + combo[:2]
    if other_combo in combo_to_num:
        total = total + combo_to_num[combo]*combo_to_num[other_combo]
out1 = str(total // 2) + '\n'
print(out1)
output_file.write(out1)
input_file.close()
output_file.close()
