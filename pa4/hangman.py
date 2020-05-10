# assignment: programming assignment 4
# author: Haofan Wang
# date: 5/15/2020
# file: hangman.py is a program that asks user to guess a random word in the dictionary.txt
# input: size of word, number of lives, letters, play again or not
# output: guess right or wrong with number of lives present as □

from random import choice, random

dictionary_file = "dictionary.txt"


def ask_play_again():
    not_valid = True
    while not_valid:
        out = input("Would you like to play again [Y/N]? \n")
        if out == 'y' or out == 'Y' or out == 'n' or out == 'N':
            return out

def choose_letter():
    not_valid = True
    while not_valid:
        try:
            input_word = input("Please choose a new letter > \n")
            if len(input_word) == 1 and input_word.isalpha():
                not_valid = False
                return input_word
        except:
            not_valid = True


def init_dict(length):
    dictionary = {}
    for i in range(length+1):
        dictionary[i] = []
    return dictionary


def import_dictionary(dictionary_file):
    max_size = 12
    dictionary = init_dict(max_size)
    try:
        with open(dictionary_file, "r") as f:
            for word in f:
                word = word.replace(" ", "")
                word = word.replace("\n", "")
                length = len(word)
                if length >= max_size:
                    dictionary[max_size].append(word)
                else:
                    dictionary[length].append(word)
            return dictionary
    except Exception:
        print("can not read the file")


def print_dictionary(dictionary):
    for pair in dictionary.items():
        print(pair)


def get_game_options():
    try:
        size_word = int(input("Please choose a size of a word to be guessed [3 - 12, default any]: "))
        if 3 <= size_word <= 12:
            print("The word size is set to {}.".format(size_word))
    except:
        print("A dictionary word of any size will be chosen.")
        size_word = int(random() * 10 + 3)
    try:
        lives = int(input("Please choose a number of lives [1 - 10, default 5]: "))
        if 1 <= lives <= 10:
            print("You have {} lives.".format(lives))
        else:
            lives = 5
            print("You have {} lives.".format(lives))
    except:
        print("You have 5 lives.")
        lives = 5
    return size_word, lives


# main function starts here -----------------------------------
dictionary = import_dictionary(dictionary_file)
# print_dictionary(dictionary)   # debug
print("Welcome to Hangman Game!")
while True:
    size_word, lives = get_game_options()
    # print(dictionary[size_word])
    guess_word = choice(dictionary[size_word])
    # print(guess_word)
    guess_word_list = list()
    hidden_word = list()
    for letter in guess_word:
        if letter != '-':
            guess_word_list.append(letter.upper())
            hidden_word.append("__  ")
        else:
            guess_word_list.append('__')
            hidden_word.append("-  ")
    # print("the target word is " + guess_word)
    letters_chosen = ()
    lives_icon = list("O" * lives)
    lives += 1
    counter = 0
    while lives != 0 and ''.join(guess_word_list) != '__' * size_word:
        if len(letters_chosen) != 0:
            print("Letters chosen: ", end="")
            for i in range(len(letters_chosen) - 1):
                print(letters_chosen[i].upper(), end=",")
            if len(letters_chosen) != 0:
                print(letters_chosen[-1].upper())
        else:
            print("Letters chosen: ")
        print(''.join(hidden_word) + " lives: {} ".format(lives - 1) + ''.join(lives_icon))
        input_word = choose_letter()
        while input_word.upper() in letters_chosen:
            print("You have already chosen this letter.")
            input_word = choose_letter()
        letters_chosen += (input_word.upper(),)
        letter_chose = letters_chosen[-1]
        if letter_chose in guess_word.upper():
            print("You guessed right!\n")
            while letter_chose in guess_word_list:
                hidden_word[guess_word_list.index(letter_chose)] = letter_chose.upper() + "  "
                # hidden_word[guess_word_list.index(letter_chose) * 4 + 1] = ""
                guess_word_list[guess_word_list.index(letter_chose)] = '__'
        else:
            print("You guessed wrong, you lost one life.")
            lives -= 1
            try:
                lives_icon[counter] = "x"
                counter += 1
            except:
                a = 0
    if lives == 0:
        print("You lost! The word was {}!".format(guess_word.upper()))
        play_again = ask_play_again()
    else:
        print("Congratulations!!! You won! The word was {}!".format(guess_word.upper()))
        play_again = ask_play_again()
    if play_again == 'N' or play_again == 'n':
        break

print("Goodbye!")
