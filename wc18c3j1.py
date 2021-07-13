p = int(input())
b = int(input())
d = int(input())

total_caps = p//b
remainder = p%b
money = total_caps*d + remainder
print(money)