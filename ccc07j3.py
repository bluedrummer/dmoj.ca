number_of_cases_opened = int(input())
cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
cases1 = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
for i in range(0, number_of_cases_opened):
    cases1.remove(cases[int(input())-1])
bankers_offer = int(input())
if (sum(cases1) / len(cases1)) >  bankers_offer:
    print("no deal")
else:
    print("deal") 

        
    
    
    
    
    
    