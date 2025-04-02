def finn_gjennomsnitt(num):
    a = 0
    b = 0
    d = len(num)
    b = d
    while d > 0:
        nim = num.pop()
        a += nim
        print(nim)
        print(a)
        d -= 1
    return a,b

active = True
while active:
    q = input("Skriv en liste med tall. Tallene skal ha et komma mellom hverandre.\n/: ")
    if q == "end":
        active = False
    else:
        c = q.replace(",", "+")
        q = q.split(",")
        try: q = [int(item) for item in q] 
        except ValueError: print("Error")
        a,b = finn_gjennomsnitt(q)
        try: 
            a = float(a)
            b = float(b)
        except ValueError: None
        print(b)
        print(a)
        q = a/b
        print(f"Gjennomsnittet av listen med tall du skrev inn er: {q}")
        print(c)
