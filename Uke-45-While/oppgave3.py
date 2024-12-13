exit1 = False

def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

while not exit1:
    action = input("[INPUT] : ")
    if is_num(action):
        action = int(action)
        if action > 0:
            print(f"'{action}' is positive.")
        elif action == 0:
            print(f"'{action}' is 0.")
        else:
            print(f"'{action}' is negative.")
    elif action == "cmd":
        action = input("cmd/: ")
        match action:
            case "close":
                exit1 = True
    else:
        print("[INVALID INPUT] : [INPUT NUMBER]")