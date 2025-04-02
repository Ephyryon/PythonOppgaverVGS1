def summer_tallx2(q = list):
    a = 0
    q1 = q.pop()
    q2 = q.pop()
    a = q1 + q2
    return a,q1,q2
active = True
while active:
    q = input("Skriv in tall 1 og 2 med mellomrom: ")
    if q == "end":
        active = False
    else:
        q = q.split(" ")
        try:
            q = [int(item) for item in q]
        except ValueError:
            print("ValueError")
        a,q1,q2 = summer_tallx2(q)
        print(f"Sum av {q1} og {q2} er {a}.")