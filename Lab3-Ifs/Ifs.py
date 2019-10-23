"""
Name: Tejas Mehta
Date: October 23rd, 2019
Lab Name: Lab3-Ifs
Extra: Allowed the user to pick between the labs
"""


# method to check if the year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and not(year % 400 == 0)


# method to check whether a number is even or odd
def isOdd(ann):
    return not(ann % 2 == 0)


# method to return greater less or equal given 2 nums
def check(a, b):
    if a > b:
        return "yes"
    elif a < b:
        return "no"
    else:
        return "aplus"


# method to get a discount if needed
def getPrice(ann):
    if ann > 2000:
        ann /= .9
    return ann


# method to add subtract or multiply
def addsubmult(a, b):
    if a > b:
        return a - b
    elif a < b:
        return b - a
    else:
        return a * b


# method calling all add subtract multiply samples
def asm():
    print(addsubmult(10, 20))
    print(addsubmult(20, 10))
    print(addsubmult(20, 20))
    print(addsubmult(10, 10))
    print(addsubmult(0, 1))
    print(addsubmult(1, 0))
    print(addsubmult(3.1, 5.7))
    print(addsubmult(5.2, 3.8))
    print(addsubmult(55342, 323))


# method calling all odd check samples
def oddcheck():
    print(isOdd(-11))
    print(isOdd(18))
    print(isOdd(17))
    print(isOdd(100))
    print(isOdd(99))
    print(isOdd(-100))
    print(isOdd(32767))
    print(isOdd(-32768))


# method calling all discount samples
def discount():
    print(getPrice(-11))
    print(getPrice(180))
    print(getPrice(2170))
    print(getPrice(3100))
    print(getPrice(9339))
    print(getPrice(2001))


# method calling all comparison samples
def bigOrSmall():
    print(check(10, 20))
    print(check(20, 10))
    print(check(20, 20))
    print(check(10, 10))
    print(check(0, 1))
    print(check(1, 0))
    print(check(3, 5))
    print(check(5, 3))
    print(check(55342, 323))


# method calling leap year input
def leapYear():
    year = int(input("Enter a year :: "))
    print(is_leap_year(year))


# loop to iterate between labs
while True:
    # Get a year
    choice = str(input("Enter a lab name (1-5) or another key to quit"))
    # check if they need to exit
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print('exiting...')
        exit(0)
    # make a chooser going to functions
    chooser = {
        "1": bigOrSmall,
        "2": asm,
        "3": leapYear,
        "4": discount,
        "5": oddcheck,
    }
    # call chooser based on choice
    chooser.get(choice)()
