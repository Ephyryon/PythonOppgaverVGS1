active = True
total = 0
while (active):
    n = input("Skriv in et tall: ")
    try:
        n = int(n)
        for i in range(1, n + 1):
            if (i % 2 != 0):
                print(i)
    except ValueError:
        if n.lower() in ["exit", "end", "cancel", "cease", "esc"]:
            active = False
        else:
            print("Inalid input. Skriv inn et tall.")