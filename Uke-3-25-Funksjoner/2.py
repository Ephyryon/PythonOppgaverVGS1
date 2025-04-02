# Celsius til Fahrenheit og revers calculator
active = True
active2 = False
while active:
    q = input("1 = Fahrenheit til celsius. 2 = Celsius til fahrenheit. : ")
    if q.isdigit():
        try:
            q = int(q)
        except ValueError:
            print("Invalid input. Skriv in 1 eller 2.")
        if q in [1, 2]:
            active2 = True
            if q == 1:
                while active2:
                    q = input("Hvor mange grader fahrenheit er det? : ")
                    if q.isnumeric():
                        try:
                            q = float(q)
                        except ValueError:
                            print("Invalid input. Skriv in et nummer.")
                        q = (q-32)*5/9
                        print(f"Det er {q} celsius grader ute.")
                        active2 = False
                    else:
                        print("Invalid input. Skriv in et nummer.")
            elif q == 2:
                while active2:
                    q = input("Hvor mange grader celsius er det? : ")
                    if q.isnumeric():
                        try:
                            q = float(q)
                        except ValueError:
                            print("Invalid input. Skriv in et nummer.")
                        q = q*1.8+32
                        print(f"Det er {q} fahrenheit grader ute.")
                        active2 = False
                    else:
                        print("Invalid input. Skriv in et nummer.")
                    
        else:
            print("Invalid input. Skriv in 1 eller 2.")
    elif q == "exit":
        active = False
    else:
        print("Invalid input. Skriv inn 1 eller 2.")