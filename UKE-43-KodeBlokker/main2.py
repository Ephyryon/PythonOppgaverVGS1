alder = input("Hvor gammel er du? : ")
alder = int(alder)
exit1 = False
while not exit1:
    if alder < 5:
        print("Billeten er gratis.")
    elif alder >= 5 and alder <= 12:
        print("Billeten koster 50kr.")
    elif alder >= 13 and alder <= 17:
        print("Billeten koster 75kr.")
    else:
        print("Billeten koster 100kr.")
    exit1 = True