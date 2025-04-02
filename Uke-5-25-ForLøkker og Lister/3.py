active = True
navn = ["Ola", "Kari", "Per", "Nora", "Lise"]
num = 0
for i in navn:
    print(f"Hei, {navn[num]}!")
    num += 1
while active:
    num = 0
    q = input("Skriv inn et navn: ")
    if q.isdigit() or q.isnumeric():
        print("Skriv inn et navn, ikke et tall.")
    elif q.lower() in ["exit", "cancel", "stop", "end", "slutt"]:
        active = False
    else:
        for i in navn:
            if q.lower() == navn[num].lower():
                print(f"{q.capitalize()} finnes i listen!")
                break
            else:
                print(f"{q.capitalize()} finnes ikke i listen.")
                num += 1