bowl_1 = int(input())
bowl_2 = int(input())
bowl_3 = int(input())

if bowl_1>bowl_2 and bowl_1<bowl_3:
    print(bowl_1)
elif bowl_1<bowl_2 and bowl_1>bowl_3:
    print(bowl_1)
elif bowl_2>bowl_1 and bowl_2<bowl_3:
    print(bowl_2)
elif bowl_2<bowl_1 and bowl_2>bowl_3:
    print(bowl_2)
elif bowl_3>bowl_1 and bowl_3<bowl_2:
    print(bowl_3)
elif bowl_3<bowl_1 and bowl_3>bowl_2:
    print(bowl_3)