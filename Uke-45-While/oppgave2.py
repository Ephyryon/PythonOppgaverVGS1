exit1 = False
karakterer = []

while not exit1:
    action = input("Skriv in poengsum: ")
    if action.isdigit():
        action = int(action)
        if action > 100:
            action = 100
            passed = "Bestått"
            print(passed)
            karakter = str(f"{action} : {passed}")
            karakterer.append(karakter)
        elif action >= 50:
            passed = "Bestått"
            print(passed)
            karakter = str(f"{action} : {passed}")
            karakterer.append(karakter)
        else:
            passed = "Ikke bestått"
            print(passed)
            karakter = str(f"{action} : {passed}")
            karakterer.append(karakter)
    elif action == "cmd":
        action = input("cmd/: ")
        match action:
            case "close":
                exit1 = True
            case "liste":
                print(karakterer)
    else:
        print("Ugyldig [INPUT]. Skriv in [INT] tall.")