citizens = int(input())
#jolliness = input().split()
count = 0

jolliness1 = list(map(int, input().split()))
jolliness1.sort()

#while len(jolliness1) != 0:
#    a = jolliness1[0]
#    jolliness2 = jolliness1.copy()
#    for i in range(1, len(jolliness1)):
#        if jolliness1[i]%a == 0:
#            jolliness2[i]='.'
#    count += 1
#    jolliness2[0]='.'
#    jolliness1 = list(filter(('.').__ne__, jolliness2))

tmp = []
tmp.append(jolliness1[0])

for i in range(1, len(jolliness1)):
    add = True
    value = jolliness1[i]
    for n in range(0, len(tmp)):
        if jolliness1[i]%tmp[n] == 0:
            add = False
            break
    if add == True:
        tmp.append(value)



print(len(tmp))
