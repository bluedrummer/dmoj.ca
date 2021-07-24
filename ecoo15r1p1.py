#orange ones, then blue, green, yellow, pink, violet, brown and finally red.
for n in range(0, 10):
    orange = 0
    blue = 0
    green = 0
    yellow = 0
    pink = 0
    violet = 0
    brown = 0
    red = 0
    time = 0 
    smartie = " "
    
    
    def smartie_calc_time(count):
        if count%7 > 0:
            return (count//7+1)*13
        else:
            return (count//7)*13
    
    while smartie != "end of box":
        smartie = input()
        if smartie == "orange":
            orange += 1
        if smartie == "blue":
            blue += 1
        if smartie == "green":
            green += 1
        if smartie == "yellow":
            yellow += 1
        if smartie == "pink":
            pink += 1   
        if smartie == "violet":
            violet += 1
        if smartie == "brown":
            brown += 1
        if smartie == "red":
            red += 1
    
    time = time + smartie_calc_time(orange)
    time = time + smartie_calc_time(blue)
    time = time + smartie_calc_time(green)
    time = time + smartie_calc_time(yellow)
    time = time + smartie_calc_time(pink)
    time = time + smartie_calc_time(violet)
    time = time + smartie_calc_time(brown)
    time = time + red*16
    
    print(time)






    
