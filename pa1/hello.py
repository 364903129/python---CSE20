# assignment: programming assignment 1

# author: (Haofan Wang)

# date: (April, 8 2020)

# file: hello.py is a program that asks the user to enter user’s name,

#        age, and favorite movie and outputs a greeting message that

#        include the information about the user

# input: string data

# output: string data

name = input("Hello! What is your name? >")
age = input("What is your age? >")
fav_Movie = input("What is your favorite movie? >")
print("Nice to meet you, {}.".format(name))
print("You are {} years old and your favorite movie is {}.".format(age, fav_Movie))
