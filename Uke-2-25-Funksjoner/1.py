active = True
def billet_type(alder = list):
    billeter = []
    nim = 0
    for num in alder:
        if num <= 12:
            nim += 1
            billet = f"Person {nim} må kjøpe en: Barnebillet\n"
            billeter.append(billet)
        elif num <= 16:
            nim += 1
            billet = f"Person {nim} må kjøpe en: Ungdomsbillet\n"
            billeter.append(billet)
        else:
            nim += 1
            billet = f"Person {nim} må kjøpe en: Voksenbillet\n"
            billeter.append(billet)
    return billeter    

while active:
    q = input("Skriv in alder. Du kan skrive inn flere aldre ved å skrive et komme mellom tallene.\nSkriv in [end] for å avslutte programmet. : ")
    if q == "end":
        active = False
    else:
        q = q.replace(","," ")
        q = q.split(" ")
        try:
            q = [int(item) for item in q]
        except ValueError:
            print("ValueError")
        billeter = billet_type(q)
        billeter = "".join(billeter)
        print(billeter)

