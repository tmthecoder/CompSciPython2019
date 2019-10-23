"""
Name: Tejas Mehta
Date: October 23rd, 2019
Lab Name: Lab4-Loops
Extra: Asked for user input on nested triangles
"""

# Return count of digits
def digitCounter(number):
    return len(str(number))

# return all digits added
def digitAdder(number):
    total = 0
    for num in str(number):
        total += int(num)
    return total

# return added divided by len for average
def digitAverage(number):
    return digitAdder(number) / digitCounter(number)

# return the even number count
def digitEvenCount(number):
    total = 0
    for num in str(number):
        if int(num) % 2 == 0:
            total += 1
    return total

# return the odd number count
def digitOddCount(number):
    total = 0
    for num in str(number):
        if not (int(num) % 2 == 0):
            total += 1
    return total

# print a nested triangle from numbers
def nestedTriangle(number):
    for x in range(number):
        print("#" * x)
    return "#" * number

# runner for counter
def counterRunner():
    val = int(input("Enter a number :: "))
    print(digitCounter(val))

# runner for adder
def adderRunner():
    val = int(input("Enter a number :: "))
    print(digitAdder(val))

# runner for average
def averageRunner():
    val = int(input("Enter a number :: "))
    print(digitAverage(val))

# runner for even counter
def evenRunner():
    print(digitEvenCount(234))
    print(digitEvenCount(10000))
    print(digitEvenCount(111))
    print(digitEvenCount(9005))
    print(digitEvenCount(84645))
    print(digitEvenCount(8547))
    print(digitEvenCount(123456789))
    print(digitEvenCount(5555672468))
    print(digitEvenCount(2548522125455))
    print(digitEvenCount(2545588514548))
    print(digitEvenCount(111111111))
    print(digitEvenCount(121212121212))

# runner for odd counter
def oddRunner():
    print(digitOddCount(234))
    print(digitOddCount(10000))
    print(digitOddCount(111))
    print(digitOddCount(9005))
    print(digitOddCount(84645))
    print(digitOddCount(8547))
    print(digitOddCount(123456789))
    print(digitOddCount(5555672468))
    print(digitOddCount(2548522125455))
    print(digitOddCount(2545588514548))
    print(digitOddCount(111111111))
    print(digitOddCount(121212121212))

# runner for nested creator
def nestedRunner():
    val = int(input("Enter a number: "))
    print(nestedTriangle(val))


while True:
    # get an input
    choice = input("Enter a lab number 1-6 or another key to quit")
    # check that it isn't an exit code
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        print("exiting....")
        exit(0)
    # run the picker
    picker = {
        "1": counterRunner,
        "2": adderRunner,
        "3": averageRunner,
        "4": evenRunner,
        "5": oddRunner,
        "6": nestedRunner
    }
    picker.get(choice)()
