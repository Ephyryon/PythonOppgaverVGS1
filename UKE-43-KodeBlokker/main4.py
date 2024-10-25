exit1 = False
question1_svar = ["Oslo", "oslo"]
question3_svar = ["Blå", "blå"]
poeng = 0

while not exit1:
    question1 = input("Hva er hovedstaden i Norge? Svar: ")
    if question1 in question1_svar:
        poeng += 1
    question2 = input("Hva er 5 * 6? Svar: ")
    if question2.isdigit():
        question2 = int(question2)
    match question2:
        case 30:
            poeng += 1
    question3 = input("Hva er fargen på himmelen på en klar dag? Svar: ")
    if question3 in question3_svar:
        poeng += 1
    print(f"Du fikk {poeng} av 3 poeng.")
    exit1 = True
