Player_a = 0
Player_b = 0
deck_of_cards = []
Player = "A"
scored = 0
def no_high(lst):

    if "jack" in lst:
        return False
    if "queen" in lst:
        return False
    if "king" in lst:
        return False
    if "ace" in lst:
        return False
    return True

for i in range(0, 52):
    deck_of_cards.append(input())
for n in range(0, 52):
    scored = 0
    remaining_cards = 52 - n - 1
    #print(remaining_cards)
    if deck_of_cards[n] == "jack" and remaining_cards >= 1 and no_high(deck_of_cards[n+1:n+2]):
        scored = 1
    elif deck_of_cards[n] == "queen" and remaining_cards >= 2 and no_high(deck_of_cards[n+1:n+3]):
        scored = 2
    elif deck_of_cards[n] == "king" and remaining_cards >= 3 and no_high(deck_of_cards[n+1:n+4]):
        scored = 3
    elif deck_of_cards[n] == "ace" and remaining_cards >= 4 and no_high(deck_of_cards[n+1:n+5]):
        scored = 4
    if scored > 0:
        print(f'Player {Player} scores {scored} point(s).')

    if Player == "A":
        Player_a = Player_a + scored
        Player = "B"
    elif Player == "B":
        Player_b = Player_b + scored
        Player = "A"

print(f'Player A: {Player_a} point(s).')
print(f'Player B: {Player_b} point(s).')
