exit1 = False

def is_even(num):
    return num % 2 == 0

while not exit1:
    number = input("Number: ")
    if number.isdigit():
        number = int(number)
        if is_even(number):
            print(f"{number} is even.")
            exit1 = True
        else:
            print(f"{number} is odd.")
            exit1 = True
    else:
        print("!NoT NumbeR!")