import random
active = True
liste = []
i = 0
num = 0
min = 0
mak = 0
gjen = 0
while active:
    q = input("Random tall eller vil du besteme selv? Bestem/Random: ")
    if q.lower() == "bestem":
        while i < 7:
            q = input(f"Skriv inn tall {i+1}: ")
            if q.isnumeric():
                q = float(q)
                liste.append(q)
                i += 1
                min = q
            else:
                print("Skriv inn et tall.")
    elif q.lower() == "random":
        while i < 7:
            r = random.randrange(1,100)
            liste.append(r)
            i += 1
            min = r
    for i in liste:
        if liste[num] > mak:
            mak = liste[num]
            gjen += liste[num]
        elif liste[num] < min:
            min = liste[num]
            gjen += liste[num]
        num += 1
print(f"Minste tall: {min}")
gjen = gjen/7
print(f"Gjennomsnitt: {gjen}")
print(f"Største tall: {mak}")
liste.clear()