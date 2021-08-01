deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] + [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] + [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] + [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] 
number_of_cards = int(input())
sum_of_cards = 0
x = 0
greater_than_x = 0
less_than_x = 0  
for i in range(0, number_of_cards):
    card_number = int(input())
    deck.remove(card_number)
    sum_of_cards += card_number
x = 21 - sum_of_cards
greater_than_x = len(list(filter(lambda n: n > x, deck)))
less_than_x = len(list(filter(lambda n: n <= x, deck)))

if greater_than_x >= less_than_x:
    print("DOSTA")
else:
    print("VUCI")


        