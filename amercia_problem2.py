def read_cows(input_file,number_cows):
    favorites = []
    for i in range(number_cows):
        lst = input_file.readline().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favorites.append(lst)
    return favorites

def cows_with_favorite(favorites, pasture):
    cows = []
    for i in range(len(favorites)):
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
            cows.append(i)
    return cows

def types_used(favorites, cows, pasture_types):
    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used

def smallest_available(used):
    grass_type = 1
    while grass_type in used:
        grass_type = grass_type + 1
    return grass_type

def write_pastures(output_file, pasture_types):
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = "".join(pasture_types_str)
    output_file.write(output + '\n')

input_file = open("revegetate.in", "r")
output_file = open("revegetate.out", "w")

lst = input_file.readline().split()
number_pastures = int(lst[0])
number_cows = int(lst[1])
favorites = read_cows(input_file, number_cows)
pasture_types = [0]

for i in range(1, number_pastures + 1):
    cows = cows_with_favorite(favorites, i)
    eliminated = types_used(favorites, cows, pasture_types)
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()
