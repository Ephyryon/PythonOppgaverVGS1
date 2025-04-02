active = True
while active:
    q = input("Skriv en settning: ")
    if q.isdigit():
        print("Skriv inn en settning. Ikke et tall.")
    else:
        q = q.split()
        print(q[:3])
        print(q[2:])
        e = q.pop()
        q = " ".join(q)
        print(q)
        active = False
