input_file = open("revegetate.in", "r")
output_file = open("revegetate.out", "w")
line1 = input_file.readline().split()
n = int(line1[0])
m = int(line1[1])
cows_with_favourite_pastures = [0]*m
pastures_with_seeds = [0]*n
seeds_for_pastures = ""

for i in range(0, m):
    line = input_file.readline()
    # Favourite pastures for cow i
    favourite_pastures = list(map(int, line.split()))
    # print(favourite_pastures)
    cows_with_favourite_pastures[i] = favourite_pastures

def prefered_pasture(cows, pasture_number):
    selected_cows = []
    for i in range(len(cows)):
        if cows[i][0] == pasture_number or cows[i][1] == pasture_number:
            selected_cows.append(i+1)
    return selected_cows

def is_pasture_favourite_of_cow(cow_number, pasture_number):
    if cows_with_favourite_pastures[cow_number-1][0] == pasture_number or cows_with_favourite_pastures[cow_number-1][1] == pasture_number:
        return True
    return False


def next_seed_number(selected_cows, cows_with_favourite_pastures, pastures_with_seeds,pasture_number):
    seeds = [1,2,3,4]
    if pasture_number == 1:
        return min(seeds)
    else:
        for p in range(1, pasture_number):
            for c in range(1, len(selected_cows) + 1):
                if is_pasture_favourite_of_cow(p,selected_cows[c-1]):
                    if seeds.count(pastures_with_seeds[p-1]) == 1:
                        seeds.remove(pastures_with_seeds[p-1])
        return min(seeds)
for p in range(1, n+1):
    a = prefered_pasture(cows_with_favourite_pastures,p)
    pastures_with_seeds[p-1] = next_seed_number(a,cows_with_favourite_pastures, pastures_with_seeds, p)

for i in range(0, len(pastures_with_seeds)):
    seeds_for_pastures = seeds_for_pastures + str(pastures_with_seeds[i])

output_file.write(seeds_for_pastures)
