exit1 = False

while not exit1:
    def is_number(s):
        try: 
            float(s)
            return True
        except ValueError:
            return False
    question1 = input("Input a number, decimals are allowed.  Number: ")
    if is_number(question1):
        num = float(question1)
        if num < 0:
            print("Your number is less than zero.")
            exit1 = True
        elif num == 0:
            print("Your number is zero.")
            exit1 = True
        else:
            print("Your number is greater than zero.")
            exit1 = True
    else:
        print("Invalid input, please enter a number.")