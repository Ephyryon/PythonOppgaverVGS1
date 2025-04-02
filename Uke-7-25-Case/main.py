filmer = []
active = True
rm = 0
def stage2():
        greater = 0
        lesser = 0
        q = input("Skriv inn titlen på en eller flere filmer. Ha komma mellom film titlene. : ")
        q = q.split(",")
        for item in q:
            if item not in filmer:
                filmer.append(item)
            else:
                print(f"'{item.capitalize()}' er allerede i listen.")
        q2 = input("Vil du legge til flere film titler? [Ja/Nei] : ")
        if q2.lower() == "nei":
            filmeru = filmer
            filmer.sort()
            q = input("Skriv inn hvor mange som besøkte festivalen for hver dag i uka.\nSkriv inn besøkne for dag 1 først, osv. Ha komma mellom dagene. : ")
            q = q.replace(" ","")
            q = q.split(",")
            if len(q) != 7:
                print("Skriv inn besøkne for hver dag denne uka. Dag 1 først, osv.")
            else:
                for item in q:
                    try:
                        item = int(item)
                        if item > greater:
                            greater = item
                        if item < lesser:
                            lesser = item
                        elif lesser == 0:
                            lesser = item
                    except ValueError:
                        print("Antall besøkne for hver dag må være tall.")
                qsum = sum(q)
                qsumdiv = qsum/len(q)
                while active:
                    try:
                        t = int(input("Terminal:\n1 - Vis gjennomsnitt for besøk denne uka\n2 - Vis høyest og lavest besøkstall\n3 - Legge til et nytt besøkstall\n4 - Vis filmer\n5 - Avslutt\nVelg et tall: "))
                    except ValueError:
                        print("Ugyldig input. Skriv et tall mellom 1 og 5.")
                    if t == 1:
                        print(f"Gjennomsnitt: {qsumdiv}")
                    elif t == 2:
                        print(f"Høyest besøkstall: {greater}\nLavest besøkstall: {lesser}")
                    elif t == 3:
                        t = input("Skriv inn et eller flere besøkstall. Ha komma mellom tallene. : ")
                        t = t.split(",")
                        for item in t:
                            try:
                                item = int(item)
                                if item > greater:
                                    greater = item
                                if item < lesser:
                                    lesser = item
                                elif lesser == 0:
                                    lesser = item
                            except ValueError:
                                print("Besøkstall må være et heltall.")
                        tsum = sum(t)
                        qsum += tsum
                        qsumdiv = qsum/(len(t)+len(q))
                        print("Besøkstall har blitt lagt til.")
                    elif t == 4:
                        print(filmer)
                    else:
                        print("Avslutter... ")
                        active = False
while active:
    q = input("Skriv inn titlen på en eller flere filmer. Ha komma mellom film titlene. : ")
    q = q.split(",")
    filmer.extend(q)
    q2 = input("Vil du legge til flere film titler? [Ja/Nei] : ")
    if q2.lower() == "nei":
        while active:
            print(filmer)
            q = input("Skriv inn titlen på filmer du vil fjerne. Ha komma mellom film titlene. : ")
            if q != "":
                q = q.split(",")
                for film in filmer:
                    for item in q:
                        if item.lower() == film.lower():
                            rm += 1
                            filmer.remove(film)
                if rm == 0:
                    print(f"Du har ikke skrevet inn noen filmer som er i listen.")
                else:
                    while active:
                        stage2()
            else:
                while active:
                    stage2()
