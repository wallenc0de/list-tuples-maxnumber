"""
Tuples and lists are basically the same thing they are both containers that store different pieces of informations, 
however there's a few key differences that makes tuples unique to lists.
Just as strings and numbers they are immutable, once you create a tuple it does it as it is.

I personally would use tuples in data where i would not change or modify them.
"""

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

def say_hi(name):
    print("Hi " + name +".") # I'm often not using f-string, because the difference in speed is really minimal.


say_hi("wallen") # The string inside the function call is only a piece of information that we are setting to "name" parameter.
lists_tuples()
