A3 = int(input())
A2 = int(input())
A1 = int(input())

B3 = int(input())
B2 = int(input())
B1 = int(input())

Apple_3 = A3*3
Apple_2 = A2*2
Apple_1 = A1*1

Banana_3 = B3*3
Banana_2 = B2*2
Banana_1 = B1*1



Apple = Apple_3 + Apple_2 + Apple_1
Banana = Banana_3 + Banana_2 + Banana_1

if Apple>Banana:
    print("A")
elif Apple<Banana:
    print("B")
elif Apple==Banana:
    print("T")
