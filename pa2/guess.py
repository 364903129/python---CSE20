# assignment: programming assignment 2
# author:(Haofan Wang)
# date:(April 14. 2020)
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import random

Game_running = True
print("Play a game: Guess My Number.")
while Game_running:
    guess_right = False
    prev_win = False
    my_number = int(random() * 10 + 1)
    print("You have three attempts to guess my number.")
    guess_number = int(input("Please enter a number from 1 to 10: "))
    for attempt in range(2):
        # guess right!
        if guess_number == my_number:
            prev_win = True
            guess_right = True
            print("You guessed right. Congratulations you won!")
            play_again = input("Would you like to play again [Y/N]? ")
            if play_again == "y" or play_again == "Y":
                Game_running = True
                break
            elif play_again == "n" or play_again == "N":
                Game_running = False
                break
        # guess wrong!
        elif guess_number < my_number:
            print("You guessed wrong. Your number is smaller than mine.")
            guess_number = int(input("Guess again. Please enter a number: "))
            if guess_number == my_number:
                guess_right = True
        elif guess_number > my_number:
            print("You guessed wrong. Your number is bigger than mine.")
            guess_number = int(input("Guess again. Please enter a number: "))
            if guess_number == my_number:
                guess_right = True
    if not guess_right:
        if guess_number < my_number:
            print("You guessed wrong. Your number is smaller than mine.")
        if guess_number > my_number:
            print("You guessed wrong. Your number is bigger than mine.")
        print("Sorry, you lost. My number is {}.".format(my_number))
        play_again = input("Would you like to play again [Y/N]? ")
        if play_again == "n" or play_again == "N":
            break
        else:
            continue

    elif guess_right and not prev_win:
        print("You guessed right. Congratulations you won!")
        play_again = input("Would you like to play again [Y/N]? ")
        if play_again == "n" or play_again == "N":
            break

print("Goodbye!")
