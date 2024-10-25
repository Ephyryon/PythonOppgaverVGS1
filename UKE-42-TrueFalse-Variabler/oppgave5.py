exit1 = False
def can_divide(dividend, divisor):
    return dividend % divisor == 0

while not exit1:
    question1 = input("Skriv inn årstal: ")
    if question1.isdigit():
        år = int(question1)
        if can_divide(år, 4) and not can_divide(år, 100):
            print("Innskrevet år er et skudår.")
            break
        elif can_divide(år, 400):
            print("Innskrevet år er et skudår.")
            break
        else:
            print("Innskrevet år er ikke et skudår.")
            break
    else:
        print("Ikke gyldig. Skriv inn et helt tall.")
