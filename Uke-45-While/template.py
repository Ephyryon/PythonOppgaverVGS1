exit1 = False

while not exit1:
    action = input("Input: ")
    if action:
        print("")
    elif action == "cmd":
        action = input("cmd/: ")
        match action:
            case "close":
                exit1 = True
    else:
        print("")