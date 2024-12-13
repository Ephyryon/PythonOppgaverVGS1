exit1 = False

def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

while not exit1:
    action = input("Input first number: ")
    if is_num(action):
        action = int(action)
        action2 = input("Input second number: ")
        if is_num(action2):
            action2 = int(action2)
            if action > action2:
                print(f"{action} is the biggest number.")
            elif action == action2:
                print(f"'{action}' and '{action2}' is equal.")
            else:
                print(f"{action2} is the biggest number.")
    elif action == "cmd":
        action = input("cmd/: ")
        match action:
            case "close":
                exit1 = True
    else:
        print("Invalid input. Input number.")