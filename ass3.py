import random

# play_again = "yes"

# while play_again == "yes":
#     rnd_num = random.randint(0,50)
#     max_attempts = 10

#     print("Choose a number")


#     for max_attempts in range(1, max_attempts + 1):
#         guess = int(input(f"attempts {max_attempts}/10 - enter your guess"))
    
#         if guess > rnd_num:
#             print("Too high")
#         elif guess < rnd_num:
#             print ("Too low")
#         else:
#             print (f"congratulations you got the answer right in {max_attempts} attempts.")
#     else:
#         print(f"you have run out of attempts. the number was {rnd_num}")

#     play_again = input("Do you want to play again? (yes/no): ")
   
# print("Thanks for playing")


# define a random number between 1 and 50
# the player plays the game 10 times
# for each guess ask the user to input thier number
# tell them if thier guess is too high, too low, or correct
# print a congratulatory message, tell them how times they guessed
# if they run of of attempts tell them the correct number
# after the game ask the player if they want to play again

random_no = random.randint(1,50)
print(random_no)
play_round = 0

while play_round < 10:
    guess_no = int(input("choose a number between 1 and 50 - "))
    print(type(guess_no))

    play_round = play_round + 1
    print(play_round)

    if guess_no > random_no:
        print("guess is too high")
    elif guess_no < random_no:
        print("guess is too low")
    else:
        print(f" congratualtions your guess is correct, you guessed it in {play_round} number of times")
#nested if statement
    if play_round == 10:
        print(f"you have ran out of attempt, the correct guess is {random_no}")
        play_again = input("do you want to play again, yes/no - ")
        if play_again == "yes" or play_again == "Yes":
            play_round = 0
        elif play_again == "no":
            play_round = 10
            break
            print("thank you for playing")