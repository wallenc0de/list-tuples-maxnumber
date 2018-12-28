# This only contains examples with tuples and a list of lists.

def lists_tuples():
    print('I loaded \'people\' list.\n')

    lucky_numbers = [(2, 59, 58), (28, 49, 59)]
    people = [
        ["User_1", 20],
        ["User_2", 30],
        ["User_3", 14],
    ]
    
    for x in people:
        print(f"{x[0]}, age - {x[1]}")

    for n in lucky_numbers:
        print(f"{n[0]} - {n[1]}")

def say_hi(name):
    print(f"Hi {name}.")

say_hi("wallen")
lists_tuples()
