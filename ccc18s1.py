number_of_villages = int(input())
villages = []
neighborhood_sizes = []
for i in range(0, number_of_villages):
    villages.append(int(input()))

villages.sort()

for i in range(1, number_of_villages-1):
    s = (villages[i] - villages[i-1])/2 + (villages[i+1] - villages[i])/2
    neighborhood_sizes.append(s)
    
neighborhood_sizes.sort()
print(neighborhood_sizes[0])

 
