distances = input().split()
distances = list(map(int, distances))
ex_string = ""

def check_distance(distance_table, city_1, city_2):
    distance = 0
    if city_1 > city_2:
        distance = distance_table[city_2:city_1]
    if city_2 >= city_1:
        distance = distance_table[city_1:city_2]
    distance = sum(distance)
    return distance

for i in range(0, 5):
    ex_string = ""
    for n in range(0, 5):
        ex_string = ex_string + str(check_distance(distances, i, n))
        ex_string = ex_string + " "
    ex_string = ex_string.rstrip()
    print(ex_string)

#print(check_distance(distances,4,1))
