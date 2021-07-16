playlist = ["A", "B", "C", "D", "E"]
button = 0
number = 0

while button != 4:
    button = int(input())
    number = int(input())
    if button == 1:
        for n in range(0, number):
            temp = ["a"]*5
            for i in range(0, 5):
                temp[i] = playlist[i]
            playlist[0] = temp[1]
            playlist[1] = temp[2]
            playlist[2] = temp[3]
            playlist[3] = temp[4]
            playlist[4] = temp[0]
    if button == 2:
        for n in range(0, number):
            temp = ["a"]*5
            for i in range(0, 5):
                temp[i] = playlist[i]
            playlist[1] = temp[0]
            playlist[2] = temp[1]
            playlist[3] = temp[2]
            playlist[4] = temp[3]
            playlist[0] = temp[4]
    if button == 3:
        for n in range(0, number):
            temp = ["a"]*5
            for i in range(0, 5):
                temp[i] = playlist[i]
            playlist[0] = temp[1]
            playlist[1] = temp[0]
    if button == 4:
        print(playlist[0] + " " + playlist[1] + " " + playlist[2] + " " + playlist[3] + " " + playlist[4])
            
