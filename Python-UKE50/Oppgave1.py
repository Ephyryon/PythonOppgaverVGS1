import datetime

time = str(datetime.date.today())

exit1 = True

while exit1:
    print(time)
    quest = input("Når ble du født? Oppgi som dd.mm.yyyy. Svar: ")
    try:
        if datetime.datetime.strptime(quest, "%d.%m.%Y"):
            questN = quest.split(".")
            questY = int(questN[2])
            qM = int(questN[1])
            qD = int(questN[0])
            timeN = time.split("-")
            timeY = int(timeN[0])
            tM = int(timeN[1])
            tD = int(timeN[2])
            ans = timeY - questY
            if (tM and qM) in range(1, 12):
                print(f"{tM}")
                print(f"{qM}")
                tM -= 1
                qM -= 1
                if tM >= 2:
                    tM -= 1
                    tM = ((tM//2)*30)+((tM//2)*31)+28
                    qM -= 1
                    qM = ((qM//2)*30)+((qM//2)*31)+28
                elif tM == 1:
                    tM = 31
                else:
                    tM = 0
            bD = tM + tD
            BD = 365 - bD
            BD = (365 - BD)//2
            print(bD)
            print(f"I dag er du {ans} år gammel.")
            print(f"Bursdagen din er om {BD} dager.")
    except ValueError:
        if quest in ["End", "end", "Close", "close", "Cancel", "cancel"]:
            print("Shutting down...")
            exit1 = False
        else:
            print(f"Input: '{quest}' does not follow the format. Input as: 'day.month.year'")