import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = 0
player_2 = 0

dealer = random.choice(deck)
print(f"player 1 cards: {dealer}")
player_2 += random.choice(deck)
print(f"player 2 cards: {player_2}")
player_2 += random.choice(deck)
print(f"player 2 cards: {player_2}")


answer = input("Do you want another card? If so, type 'yes. If not, type 'no'.\n")
if answer == 'no':
    xtra_card = False
elif answer == 'yes':
    xtra_card = True
    
while xtra_card == True:
    player_2 += random.choice(deck)
    print(player_2)
    if player_2 > 21:
        print(f"{player_2} is more than 21. You lose.")
        xtra_card = False
    elif player_2 <= 21:
        answer = input("Do you want another card? If so, type 'yes. If not, type 'no'.\n")
        if answer == 'no':
            xtra_card = False

dealer += random.choice(deck)
while dealer < 17:
    dealer += random.choice(deck)

if dealer <= 21 and player_2 <= 21:
    if dealer > player_2:
        print(f"D wins: {dealer}")
        print(f"Pl 2: {player_2}")
    elif dealer < player_2:
        print(f"D: {dealer}")
        print(f"Pl 2 wins: {player_2}")
    else:
        print("It's a draw")
        print(f"D: {dealer}")
        print(f"Pl 2: {player_2}")

