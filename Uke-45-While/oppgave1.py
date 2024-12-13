exit1 = False
number = 0

while not exit1:
    action = input("Input number(Input 0 to end): ")
    if action == "0":
        print(f"'0' inputed. Totalsum: {number} ")
        exitNOT = True
    elif action.isdigit():
        action = int(action)
        was = number
        number += action
        print(f"{action} added to {was}. Number is now {number}.")
    else:
        print(f"'{action}' isn't a number.")
