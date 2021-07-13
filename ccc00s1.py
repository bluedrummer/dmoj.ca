quarters_in_jar = int(input())
slot_1_turns_since_win = int(input())
slot_2_turns_since_win = int(input())
slot_3_turns_since_win = int(input())
turns_played = 0 
current_slot = 1


while quarters_in_jar>0:
    if current_slot == 1:
        if slot_1_turns_since_win == 34:
            quarters_in_jar += 29
        else:
            quarters_in_jar -= 1
        current_slot = 2
        turns_played += 1
        if slot_1_turns_since_win == 35:
            slot_1_turns_since_win = 1
        else:
            slot_1_turns_since_win += 1
    elif current_slot == 2:
        if slot_2_turns_since_win == 99:
            quarters_in_jar += 59
        else:
            quarters_in_jar -= 1
        current_slot = 3
        turns_played += 1
        if slot_2_turns_since_win == 100:
            slot_2_turns_since_win = 1
        else:
            slot_2_turns_since_win += 1
    elif current_slot == 3:
        if slot_3_turns_since_win == 9:
            quarters_in_jar += 8
        else:
            quarters_in_jar -= 1
        current_slot = 1
        turns_played += 1
        if slot_3_turns_since_win == 10:
            slot_3_turns_since_win = 1
        else:
            slot_3_turns_since_win += 1
print("Martha plays " + str(turns_played) + " times before going broke.")
        
                
          
    
    
