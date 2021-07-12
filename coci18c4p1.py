current_owner = input()
number_of_battles = int(input())
list_of_owners = ""
list_of_owners = list_of_owners + current_owner
number_of_times_wand_has_changed_owners = 1
battles = [""]*number_of_battles

#hello
for i in range(0, number_of_battles):
    battles[i] = input()

for b in battles:
    if current_owner == b[2]:
        current_owner = b[0]
        if list_of_owners.count(current_owner) == 0: 
             number_of_times_wand_has_changed_owners += 1
             list_of_owners = list_of_owners + current_owner
        
print(current_owner)
print(number_of_times_wand_has_changed_owners)
    
    