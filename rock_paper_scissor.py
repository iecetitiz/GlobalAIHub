import random

round_number = int(input("how many round do you want?"))

actions = ["rock", "paper", "scissor"]
player1_counter = 0
player2_counter = 0

for i in range(round_number):
    print("Round Number: ", (i + 1))
    player1_choice = random.choice(actions)
    player2_choice = random.choice(actions)

    print(player1_choice)
    print(player2_choice)

    #print(type(player2_choice))

    if player1_choice == player2_choice:
        print("Tie! Both players chose the same action")
    elif ((player1_choice == "paper" and player2_choice == "rock") or (player1_choice == "scissor" and player2_choice == "paper")
        or (player1_choice == "rock" and player2_choice == "scissor")):
        print("player 1 won")
        player1_counter += 1
    else:
        print("player 2 won")
        player2_counter += 1

if player1_counter > player2_counter:
    print("winner is: player1")
elif player1_counter == player2_counter:
    print("tie!")
else:
    print("winner is: player 2")
