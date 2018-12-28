# This only contains examples with a list of lists and tuples.

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
        print(f"\n{y[0]} - {y[1]} - {y[2]}")

def say_hi(name):
    print("Hi " + name +".") # im often not using f-string, because the difference in terms of speed is really minimal ..

# The string inside the function call is only a piece of information that we are setting to "name" parameter.
say_hi("wallen")
lists_tuples()
