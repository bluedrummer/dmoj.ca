password = input()
uppercase = 0
lowercase = 0
numeric = 0
for c in password:
    if c.isupper():
        uppercase += 1
    elif c.islower():
        lowercase += 1
    elif c.isnumeric():
        numeric += 1

if len(password) >= 8 and len(password)<= 12 and uppercase >= 2 and lowercase >= 3 and numeric >= 1:
    print("Valid")
else:
    print("Invalid")
