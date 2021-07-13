car_spaces = int(input())
yesterday = input()
today = input()

total_car_spaces = 0

for space_index in range(0, car_spaces):
    if yesterday[space_index] == "C":
        if today[space_index] == "C":
            total_car_spaces += 1
print(total_car_spaces)
        
    
    
    