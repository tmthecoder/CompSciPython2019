"""
Name: Tejas Mehta
Date: October 15th, 2019
Lab Name: Lab1-Basics
Extra: They get to pick which lab part they want to run
"""
while (True):
    # ask for choice
    choice = input("pick a lab number (1-3) or any other key to quit")
    if choice == "1":
        # print the value
        print(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAA\n"
            "++++++++++++++++++++++++++\n"
            "+++                    +++\n"
            "+++                    +++\n"
            "+++                    +++\n"
            "+++                    +++\n"
            "+++     A+ CompSci     +++\n"
            "+++                    +++\n"
            "+++                    +++\n"
            "+++                    +++\n"
            "+++                    +++\n"
            "AAAAAAAAAAAAAAAAAAAAAAAAAAA\n"
            "+++++++++++++++++++++++++++")
    elif choice == "2":
        # ask their name, age, and bday
        name = input("What is your name?")
        age = input("What is your age?")
        year = input("What year was your last birthday?")
        # print name and age
        print("Your name is " + name + " and you are " + age + " years old")
        # Calc year and print it
        print("You were born in " + str(int(year) - int(age)))
    elif choice == "3":
        # print each number divided for frac to decimal
        print("2/3 = " + str(2 / 3.0))
        print("1/5 = " + str(1 / 5.0))
        print("5/10 = " + str(5 / 10))
        print("3/10 = " + str(3 / 10.0))
        print("167/555 = " + str(167 / 555.0))
        print("34/98 = " + str(34 / 98.0))
    else:
        #exit
        exit(0)
