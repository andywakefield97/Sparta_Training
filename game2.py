import random

player_list = []
red_black_list = ['Red', 'Black']
suit_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
number_list = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

Player1 = input("Player 1 please enter your name")
player_list.append(Player1)

Player2 = input("Player 2 please enter your name")
player_list.append(Player2)

Player3 = input("Player 3 please enter your name")
player_list.append(Player3)

Player4 =  input("Player 4 please enter your name")
player_list.append(Player4)

print(random.choice(player_list))
q1_input = input('Red or Black?')
q1_answer = random.choice(red_black_list)


if q1_input.upper() == q1_answer.upper():
    print('Correct!')
    q2_input = input('Pick a Suit! (Hearts, Diamonds, Clubs or Spades)')
    q2_answer = random.choice(suit_list)

    if q2_input.upper() == q2_answer.upper():
        print('Correct!')
        q3_input = input('Pick a Card Number! (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2)')
        q3_answer = random.choice(number_list)

        if q3_input.upper() == q3_answer.upper():
            print('YOU WIN!')
        elif q3_input.upper() != q3_answer.upper():
            print('Drink!')

    elif q2_input.upper() != q2_answer.upper():
        print('Drink!')
elif q1_input.upper() != q1_answer.upper():
    print('Drink!')












