for i in range(0,10):
    bonus = 0
    line1 = input() # "4 5"
    number_of_franchises = int(line1.split()[0])
    number_of_days = int(line1.split()[1])
    data = []
    for d in range(0, number_of_days):
        line2 = input() # "4 3 2 4"
        line2_split = line2.split() #['4', '3', '2', '4']
        line2_int = []
        for i in range(0, len(line2_split)):
            line2_int.append(int(line2_split[i]))
        data.append(line2_int)
    for r in data:
        total = sum(r)
        if total % 13 == 0:
            bonus = bonus + (total // 13)
    for i in range(0, number_of_franchises):
        total = 0
        for j in range(0, number_of_days):
            total = total + data[j][i]
        if total % 13 == 0:
            bonus = bonus + (total // 13)
        
    print(bonus)
              
        
            
            
        
        
    
    