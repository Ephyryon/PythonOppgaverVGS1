exit1 = False


while not exit1:
    q = input("Årlig inntekt? : ")
    if q.isnumeric():
        q = float(q)
        print(q)
        while not exit1:
            q2 = input("Har du barn under 12år? Hvis ja, hvor mange. : ")
            if q2.isnumeric() or q2.lower() == "nei": 
                try:
                    q2 = float(q2)
                    if q2 > 1:
                        q2 = 25000.0 + (15000.0*(q2-1))
                    else:
                        q2 = 25000.0
                except ValueError:
                    None
                while not exit1:
                    q3 = input("Har du satt in beløp på BSU? Hvis ja, skriv in hvor mye. Hvis nei, ikke skriv in noe. : ")
                    if q3.isnumeric():
                        q3 = float(q3)
                        if q3 <= 27500.0:
                            q3 = q3/10
                            while not exit1:
                                q4 = input("Har du betalt på gjeld? Hvis ja, skriv in hvor mye. Hvis nei, ikke skriv in noe. : ")
                                if q4.isnumeric() or q4 == "":
                                    try:
                                        q4 = float(q4)
                                    except ValueError:
                                        None
                                    while not exit1:
                                        q5 = input("Har du betalt fagforeningskontingent? Hvis ja, skriv in hvor mye. Hvis nei, ikke skriv in noe. : ")
                                        if q5.isnumeric or q5 == "":
                                            try:
                                                q5 = float(q5)
                                                if q5 > 7700:
                                                    q5 = 7700
                                            except ValueError:
                                                None
                                            while not exit1:
                                                a = q*0.46
                                                if a > 109950.0:
                                                    a = 109950.0
                                                a = a+q2+q3+q4+q5
                                                a = q-a
                                                a = a*0.22
                                                b = 0.0
                                                c = 0.0
                                                d = 0.0
                                                e = 0.0
                                                f = 0.0
                                                g = 0.0
                                                # Første trinn
                                                if q > 217400.0:
                                                    b = min(q, 306050.0) - 217400.0
                                                    b = b * 0.017
                                                # Andre trinn
                                                if q > 306050.0:
                                                    c = min(q, 697150.0) - 306050.0
                                                    c = c * 0.04
                                                # Tredje trinn
                                                if q > 697150.0:
                                                    d = min(q, 942400.0) - 697150.0
                                                    d = d * 0.137
                                                # Fjerde trinn
                                                if q > 942400.0:
                                                    e = min(q, 1410750.0) - 942400.0
                                                    e = e * 0.167
                                                # Femte trinn
                                                if q > 1410750.0:
                                                    f = q - 1410750.0
                                                    f = f * 0.177
                                                #Trygde avgift
                                                g = q*0.077
                                                answer = b+c+d+e+f
                                                print(answer)
                                                print(a)
                                                print(g)
                                                answer = answer+a+g
                                                v = answer/q
                                                v = v*100.0
                                                print(f"Din årlige skatt er {answer} med en årlig inntekt på {q}. Det er {v}% av din årlige inntekt.")
                                                exit1 = True
                                        elif q5.lower() == "exit":
                                            exit1 = True
                                        else:
                                            print("Feil. Skriv in et tall eller ingenting.")
                                elif q4.lower() == "exit":
                                    exit1 = True
                                else:
                                    print("Feil. Skriv in et tall eller ingenting.")
                        else:
                            print("Feil. Kan ikke sette inn mer en 27500kr i BSU i året.")
                    elif q3.lower() == "exit":
                        exit1 = True
                    else:
                        print("Feil. Skriv in et tall eller ingenting.")
            elif q2.lower() == "exit":
                exit1 = True
            else:
                print("Feil. Skriv in Ja eller Nei.")
    elif q.lower() == "exit":
        exit1 = True
    else:
        print("Feil. Skriv in årlig inntekt uten noen tegn.")
