#Park the Bus Drinking Game in Python
#Players are asked to select a color of a card its suit and then its value/number.
#To win the game a player must correctly guess all 3 aspects of the card
#If a player guesses incorrectly they are asked to take a drink

import random

#Lists for players and deck of cards

player_list = []
red_black_list = ['Red', 'Black']
suit_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
number_list = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

#Up to 4 Players can input their names
#IF statements mean that if only 1, 2 or 3 players want to play this is also possible

Player1 = input("Player 1 please enter your name")
player_list.append(Player1)

P2 = input('Is there another player? (Y/N)')
if P2 == 'Y':
    Player2 = input("Player 2 please enter your name")
    player_list.append(Player2)

    P3 = input('Is there another player? (Y/N)')
    if P3 == 'Y':
        Player3 = input("Player 3 please enter your name")
        player_list.append(Player3)

        P4 = input('Is there another player? (Y/N)')
        if P4 == 'Y':
            Player4 = input("Player 4 please enter your name")
            player_list.append(Player4)


#A random player is selected to guess the colour of a card
print(random.choice(player_list))
q1_input = input('Red or Black?')

#Using the 'random' package an answer is selected
q1_answer = random.choice(red_black_list)

#If correct they are asked to guess the suit
if q1_input.upper() == q1_answer.upper():
    print('Correct!')
    q2_input = input('Pick a Suit! (Hearts, Diamonds, Clubs or Spades)')
    q2_answer = random.choice(suit_list)

#If they are correct in question 2 they are finally asked to select the value/number of the card
    if q2_input.upper() == q2_answer.upper():
        print('Correct!')
        q3_input = input('Pick a Card Number! (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2)')
        q3_answer = random.choice(number_list)

        if q3_input.upper() == q3_answer.upper():
            print('YOU WIN!')

#If a player is wrong they are told to drink and given the correct answer
        elif q3_input.upper() != q3_answer.upper():
            print('Drink!')
            print('The correct answer was', q3_answer)

    elif q2_input.upper() != q2_answer.upper():
        print('Drink!')
        print('The correct answer was', q2_answer)
elif q1_input.upper() != q1_answer.upper():
    print('Drink!')
    print('The correct answer was', q1_answer)












