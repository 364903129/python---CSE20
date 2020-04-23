# assignment: programming assignment 3
# author: (Haofan Wang)
# date: (4/20/2020)
# file: calculator.py is a program that calculates basic operation such as
# addition, subtraction, multiplication and division
# input: Operation - A,S,M,D    First number and Second number
# output: The operation result
import decimal


def isfloat(token):
    dot = False
    minus = False
    for char in token:
        if char.isdigit():  # allow many digits in a string
            continue
        elif char == ".":  # allow only one dot in a string
            if not dot:
                dot = True
            else:
                return False
        elif char == "-" and token[0] == "-":  # allow one minus in front
            if not minus:
                minus = True
            else:
                return False
        else:  # do not allow any other characters in a string
            return False
    return True


def format_number(token):
    tup_token = decimal.Decimal(token).as_tuple()  # (sign, digits, exponent)
    delta = len(tup_token.digits) + tup_token.exponent
    digits = ''.join(str(digit) for digit in tup_token.digits)  # join the digits
    if delta <= 0:  # numbers that are less than 1
        zeros = abs(tup_token.exponent) - len(tup_token.digits)
        val = '0.' + ('0' * zeros) + digits
    else:
        val = digits[:delta] + ('0' * tup_token.exponent) + '.' + digits[delta:]
    val = val.rstrip('0')  # delete the trailing 0
    if val[-1] == '.':
        val = val[:-1]
    if tup_token.sign:  # if the number is negative, return negative number
        if val.isdigit():
            return -round(int(val))
        else:
            return -round(float(val), 2)
    if val.isdigit():  # if the number is positive, return positive number
        return round(int(val))
    else:
        return round(float(val), 2)


def addition(a, b):  # add two number
    return decimal.Decimal(a) + decimal.Decimal(b)


def subtraction(a, b):  # subtract two number
    return decimal.Decimal(a) - decimal.Decimal(b)


def multiply(a, b):  # multiply two number
    return decimal.Decimal(a) * decimal.Decimal(b)


def divide(a, b):  # divide two number
    return decimal.Decimal(a) / decimal.Decimal(b)


print("Welcome to Calculator Program!")
game_running = True
while game_running:
    # ask the user to enter an operation
    operation = input("Please choose one of the following operations:\n"
                      "Addition - A\n"
                      "Subtraction - S\n"
                      "Multiplication - M\n"
                      "Division - D\n"
                      ">")
    # when the user did not choose the correct operation, ask them again
    while operation != "A" and operation != "S" and operation != "M" and operation != "D":
        print("You did not choose correctly.")
        operation = input("Please choose one of the following operations:\n"
                          "Addition - A\n"
                          "Subtraction - S\n"
                          "Multiplication - M\n"
                          "Division - D\n"
                          ">")
    # operation == A S M D
    if operation == "A":
        print("You chose addition.")
    if operation == "S":
        print("You chose subtraction.")
    if operation == "M":
        print("You chose multiplication.")
    if operation == "D":
        print("You chose division.")
    # enter the first number
    first_number = input("Please enter the first number: ")
    # when user did not choose a valid number
    while not isfloat(first_number):
        print("You did not choose a number.")
        first_number = input("Please enter the first number: ")
    print("The first number is {}".format(format_number(first_number)))
    # enter the second number
    second_number = input("Please enter the second number: ")
    # when user did not choose a valid number
    while not isfloat(second_number):
        print("You did not choose a number.")
        second_number = input("Please enter the second number: ")
    print("The second number is {}".format(format_number(second_number)))

    # perform the addition, and output in correct output as instruct
    if operation == "A":
        result = addition(first_number, second_number)
        print("{} + {} = {}".format(format_number(first_number), format_number(second_number), format_number(result)))

    # perform the subtraction, and output in correct output as instruct
    if operation == "S":
        result = subtraction(first_number, second_number)
        print("{} - {} = {}".format(format_number(first_number), format_number(second_number), format_number(result)))

    # perform the multiplication, and output in correct output as instruct
    if operation == "M":
        result = multiply(first_number, second_number)
        print("{} x {} = {}".format(format_number(first_number), format_number(second_number), format_number(result)))

    # perform the division, and output in correct output as instruct
    if operation == "D":
        # second number can't be 0 because any number divide by 0 is prohibit in this assignment
        if float(second_number) == 0.0:
            print("The division by zero is prohibited!")
        else:
            result = divide(first_number, second_number)
            print(
                "{} / {} = {}".format(format_number(first_number), format_number(second_number), format_number(result)))

    # ask the player to play again or not to play again
    play_again = input("Do you want to continue? [Y/N] > ")
    if play_again == "y" or play_again == "Y":
        game_running = True
    if play_again == "n" or play_again == "N":
        game_running = False

# game ends!
print("Goodbye!")