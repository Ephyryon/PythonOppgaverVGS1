name = input("Name? : ")
exit1 = False
tries = 0
while not exit1:
    if name == "Mary": 
        print("Hello Mary.")
        while not exit1:
            password = input("Password? : ")
            if password == "swordfish":
                print("Access granted.")
            elif tries < 3:
                print("Wrong password.")
                tries += 1
            else:
                print("Too many tries.")
                exit1 = True
    else:
        print("Unknown username.")