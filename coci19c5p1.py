d = input().split()
d = list(map(int, d))
rectangle = 0
drawing = [ ["."]*d[1] for i in range(d[0])]

for i in range(d[0]):
    l = input()
    for n in range(0, len(l)):
        drawing[i][n] = l[n]

for n in range(d[0]):
    for m in range(0, d[1]):
        if drawing[n][m] == "*":
            #First line
            if n == 0:
                #first character
                if m == 0:
                    rectangle += 1
                # second character or after
                else:
                    if drawing[0][m-1] == ".":
                        rectangle += 1
            #second line charcter or after
            else:
                #fist character
                if m == 0:
                    if drawing[n-1][0] == ".":
                        rectangle += 1
                #second character or after
                else:
                    if drawing[n][m-1] == "." and drawing[n-1][m] == ".":
                        rectangle += 1

print(rectangle)
