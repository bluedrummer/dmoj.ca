m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
b1 = 461
b2 = 431
b3 = 420
b4 = 0
d1 = 130
d2 = 160
d3 = 118
d4 = 0
s1 = 100
s2 = 57
s3 = 70
s4 = 0
des1 = 167
des2 = 266
des3 = 75
des4 = 0
total = 0
if m1 == 1:
    total += b1
elif m1 == 2:
    total += b2
elif m1 == 3:
    total += b3
if m2 == 1:
    total += d1
elif m2 == 2:
    total += d2
elif m2 == 3:
    total += d3
if m3 == 1:
    total += s1
elif m3 == 2:
:    total += s2
elif m3 == 3:
    total += s3
if m4 == 1:
    total += des1
elif m4 == 2:
    total += des2
elif m4 == 3:
    total += des3
print("Your total  Calorie count is " + str(total) + ".")