"""
This is just an example program using 'if statements' with operators and comparing them with strings and integers.

Tuples and lists are basically the same thing they are both containers that store different pieces of informations.
However there's a few key differences that makes tuples unique to lists, just as strings and numbers they are immutable.
once you create a tuple it does it as it is.

I personally would use tuples in data where i would not change or modify them.
"""

def y_n():
    want_lists = input('Do you want to load tuples and lists? y/n: ')
    if want_lists == 'y':
        lists_tuples()
    elif want_lists == 'n':
        want_nums = input('Okay, do you want to write 3 numbers and detect the max num? (y/n): ')
    if want_nums == 'y':
        max_num()
    elif want_nums == 'n':
        print('Ending the program.')

def lists_tuples():
    print('I loaded \'people\' and \'tuples\' list.\n')

    lucky_numbers = [
        (80, 49, 78)
    ]

    people = [
        ["Adams", 20],
        ["Baker", 21],
        ["Clark", 14],
    ]

    for x in people:
        print(f"{x[0]} has age {x[1]}.")

    for y in lucky_numbers:
        print(f"{y[0]} - {y[1]} - {y[2]}")

def max_num():

    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))
    num3 = int(input('Third number: '))

    if num1 >= num2 and num1 >= num3:
        print(str(num1) + ' is the big number.') # Not using f-strings because the difference in speed is minimal.
    elif num2 >= num1 and num2 >= num3:
        print(str(num2) + ' is the big number.')
    else:
        print(str(num3) + ' is the big number.')

def say_hi(name):
    print("Hi " + name +".")

say_hi("wallen") # The string inside the function call is only a piece of information that we are passing to 'name' parameter.
y_n()

