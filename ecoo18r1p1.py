for n in range(0, 10):
    line = input()
    T = int(line.split()[0])
    N = int(line.split()[1])
    dataset = []
    extra_days = 0
    for i in range(0, N):
        dataset.append(input())
    for i in range(0, N):
        if dataset[i] == "E":
            if extra_days > 0:
                extra_days -= 1 
#            print(extra_days)
        elif dataset[i] == "B":
            extra_days += T-1
#            print(extra_days)
    print(extra_days)
         
    







