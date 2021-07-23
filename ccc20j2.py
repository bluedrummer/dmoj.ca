total_people_infected= int(input())
people_on_day0 = int(input())
r = int(input())
day = 0
sick_on_current_day = people_on_day0
tally = people_on_day0
while tally <= total_people_infected:
    day += 1
    sick_on_current_day = sick_on_current_day * r
    tally += sick_on_current_day


print(day)