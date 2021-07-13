line = input()
s = line.split()[0]
r = line.split()[1]
r = float(r)
s = float(s)



square = s*s
circle = 3.14*r*r

if square>circle:
    print("SQUARE")
else:
    print("CIRCLE")