kaldt = False
exit1 = False
lue = False
feil_teller = 0

Ja = ["Ja", "ja"]
Nei = ["Nei", "nei"]
Svar = [Ja, Nei]

def check_input(input_value, list_of_lists):
    for sublist in list_of_lists:
        if input_value in sublist:
            return True
    return False

def question3():
    global exit1
    question3 = input("Går du ut?")
    if not check_input(question3, Svar):
        feil_kode()
    elif question3 in Ja:
        print("Du går ut.")
    elif question3 in Nei:
        print("Du går ikke ut. Du blir hjemme.")
        print("End")
        exit1 = True

def question4():
    global exit1
    if kaldt == True and lue == False:
        print("Du ble syk fordi det var kaldt og du tokk ikke på deg en lue.")
        print("End")
        exit1 = True
    elif kaldt == False and lue == True:
        print("Du ble dehydrert fordi det var ikke kaldt og du tokk på deg lue.")
        print("End")
        exit1 = True
    elif kaldt == True and lue == True:
        print("Du gikk en tur uten å fryse fordi du tokk på deg lue mens det var kaldt.")
        print("End")
        exit1 = True
    elif kaldt == False and lue == False:
        print("Du gikk en tur uten å bli dehydrert fordi du tokk ikke på deg lue mens det ikke var kaldt ute.")
        print("End")
        exit1 = True

def question2():
    global lue
    question2 = input("Tar du på deg lue?")
    if not check_input(question2, Svar):
        feil_kode()
    elif question2 in Ja:
        print("Du tokk på deg lue.")
        lue = True
    elif question2 in Nei: 
        print("Du tokk ikke på deg lue.")
        lue = False

def feil_kode():
    global feil_teller
    global exit1
    if feil_teller == 0:
        print("Jeg sa bare svar Ja eller Nei.")
        feil_teller += 1
    elif feil_teller == 1:
        print("Jeg sa bare svar Ja eller Nei. Husk det.")
        feil_teller += 1
    elif feil_teller == 2:
        print("Jeg sa BARE svar Ja eller Nei.")
        feil_teller += 1
    else:
        print("Ok, hade.")
        exit1 = True

print("Du er på vei ut døra.(Svar bare Ja eller Nei)")

while not exit1:
    question1 = input("Er det kalt ute? Svar: ")
    if not check_input(question1, Svar):
        feil_kode()

    elif question1 in Ja:
        print("Det er kaldt ute")
        kaldt = True
        while not exit1:
            question2()
            while not exit1:
                question3()
                while not exit1:
                    question4()

    elif question1 in Nei: 
        print("Det er ikke kaldt ute.")
        kaldt = False
        while not exit1:
            question2()
            while not exit1:
                question3()
                while not exit1:
                    question4()