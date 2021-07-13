mb_per_month = int(input())
number_of_months = int(input())
p = [0]*number_of_months
avaible_nb = 0
for i in range(0, number_of_months):
    p[i] = int(input())

for i in range(0, number_of_months):
    avaible_nb = avaible_nb + mb_per_month - p[i]
avaible_nb += mb_per_month
    

print(avaible_nb)
