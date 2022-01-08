def clean_address(address):
    plus_index = address.find("+")
    if plus_index != -1:
        at_index = address.find("@")
        address = address[:plus_index] + address[at_index:]
    at_index = address.find("@")
    before_at = ""
    i = 0
    while i < at_index:
        if address[i] != ".":
            before_at = before_at + address[i]
        i+=1
    cleaned = before_at + address[at_index:]
    cleaned = cleaned.lower()
    return cleaned

for d in range(0, 10):
    number_of_emails = int(input())
    addresses = set()
    for i in range(number_of_emails):
        address = input()
        address = clean_address(address)
        addresses.add(address)
    print(len(addresses))
