user_what = input("Type help > ")
class Calculator:
    while True:
        def add(num1, num2):
            return num1 + num2


        def subtract(num1, num2):
            return num1 - num2


        def divide(num1, num2):
            return num1 / num2


        def multiply(num1, num2):
            return num1 * num2
        home_screen = True
        help_window = False
        if user_what.lower() == "help":
            print("""add - addition
sub - subtraction
divide - division 
multiply - multiplication
back - go back
quit - close the program
    """)
            help_window = True
            user_what = input(" > ")
        if user_what.lower()== "back":
            print("Back to home")
            user_what = input(" > ")


        elif user_what.lower() == "add":
            try:
                num1 = int(input("num 1 > "))
                num2 = int(input("num2 > "))
                sum = add(num1,num2)
                print(sum)
                print("use it again?")
                user_what = input(" > ")

            except:
                print("numbers only on calculator terminal try again")
        elif user_what.lower() == "sub":
            try:
                num1 = int(input("num 1 > "))
                num2 = int(input("num2 > "))
                diff = subtract(num1, num2)
                print(diff)
                print("use it again?")
                user_what = input(" > ")
            except:
                print("numbers only on calculator terminal try again")
        elif user_what.lower() =="multiply":
            try:
                num1 = int(input("num 1 > "))
                num2 = int(input("num2 > "))
                multiply = multiply(num1, num2)
                print("multiply")
                print("use it again?")
                user_what = input(" > ")
            except:
                print("numbers only on calculator terminal try again")
        elif user_what.lower() =="divide":
            try:
                num1 = int(input("num 1 > "))
                num2 = int(input("num2 > "))
                divide = divide(num1, num2)
                print(divide)
                print("use it again?")
                user_what = input(" > ")
            except:
                print("numbers only on calculator terminal try again")
        elif user_what.lower() =="quit":
            print("Exiting program")
            n = range(1,4)
            for number in reversed(n):
                print(number)
            print("program closed")
            break

        else:
            print("I dont know this command, try again")
            user_what = input(" > ")
