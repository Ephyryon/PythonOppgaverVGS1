actions = ["end", "sjekk saldo", "ta ut", "sett inn"]
balance = 0
exit1 = False
def check_input(input_value, list_of_lists):
    for sublist in list_of_lists:
        if input_value in sublist:
            return True
    return False
while not exit1:
    exit2 = False
    action = input("Hva vil du gjøre?(sett inn/ta ut/sjekk saldo): ")
    if check_input(action, actions):
        while not exit2:
            match action:
                case "sett inn":
                    deposit = input("Hvor mye vil du sette inn? : ")
                    deposit = int(deposit)
                    balance += deposit
                    print(f"Du har satt inn {deposit} NOK. Din nye saldo er {balance} NOK.")
                    exit2 = True
                case "ta ut":
                    deposit = input("Hvor mye vil du ta ut? : ")
                    deposit = int(deposit)
                    if deposit < balance:
                        balance -= deposit
                        print(f"Du har tatt ut {deposit} NOK. Din nye saldo er {balance} NOK.")
                        exit2 = True
                    else:
                        print(f"Du har ikke nokk i kontoen. Du har {balance} NOK i kontoen.")
                        exit2 = True
                case "sjekk saldo":
                    print(f"Din saldo er {balance} NOK.")
                    exit2 = True
                case "end":
                    exit1 = True
                    exit2 = True
    else:
        print("Invalid Input")