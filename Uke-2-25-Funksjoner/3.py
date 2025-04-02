import random
def kast_terning(rull = int):
    nim = 0
    num = 0
    r = []
    while rull > 0:
        nim += 1
        a = random.randint(1,6)
        num += a
        a = f"Rull {nim}: {a}\n"
        rull -= 1
        r.append(a)
    return r,num


active = True
while active:
    q = input("Hvor mange ganger ruller du terningen?\n : ")
    if q == "end":
        active = False
    else:
        try:
            q = int(q)
        except ValueError:
            print("Feil. Skriv in et tall.")
            break
        r,num = kast_terning(q)
        try:
            float(num)
        except ValueError:
            print("ValueError")
        num = num/q
        r = "".join(r)
        print(r)
        print(f"Average: {num}")