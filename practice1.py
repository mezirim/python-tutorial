# rock paper scissors game 
import random as rn

restart = True
while restart == True:
    options = ["rock", "paper", "scissors"]
    computer_choice = rn.choice(options)
    # print(computer_choice)
    my_choice = input("choose an option")
    if my_choice not in options:
        print("invalid option")
    if computer_choice == "paper" and my_choice == "scissors":
        print("you've won this round")
        restart = False
    elif computer_choice == "scissors" and my_choice == "paper":
        print("you've lost this round")
        restart = False
    elif computer_choice == "paper" and my_choice == "rock":
        print("you've won this round")
        restart = False
    elif computer_choice == "rock" and my_choice == "paper":
        print("you've lost this round")
        restart = False
    elif computer_choice == "scissors" and my_choice == "rock":
        print("you've won this round")
        restart = False
    elif computer_choice == "rock" and my_choice == "scissors":
        print("you've lost this round")
        restart = False
    elif computer_choice == my_choice:
        print("its a tie")
        restart = True


#you can use break for restart = false and continue = true