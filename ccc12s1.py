year_given = int(input())

def is_distinct(year):
    year_start = [c for c in str(year)]
    seen = set(year_start)
    if len(seen) != len(year_start):
        return False
    return True

for i in range(year_given + 1, 20000):
    if is_distinct(i):
        print(i)
        break
