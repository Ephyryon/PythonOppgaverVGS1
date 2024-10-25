exit1 = False

while not exit1:
    question1 = input("Input First Number: ")
    if question1.isdigit():
        num1 = int(question1)
        while not exit1:
            question2 = input("Input Second Number: ")
            if question2.isdigit():
                num2 = int(question2)
                if num1 > num2:
                    print(f"Your first number({num1}) is greater than your second number({num2}).")
                    exit1 = True
                elif num1 == num2:
                    print(f"Both your first and second number is {num1}.")
                    exit1 = True
                else:
                    print(f"Your first number({num1}) is lesser than your second number({num2}).")
                    exit1 = True
            else:
                print("Invalid Input")
    else:
        print("Invalid Input")
