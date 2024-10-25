poeng_max = 100

poeng_liste = []

exit_list = ["Exit", "EXIT", "exit", "End", "END", "end"]

cheese = False

function_push = poeng_liste

while not cheese: 
    question1 = input("Skriv inn Poeng: ")
    if question1 in exit_list:
        break
        
    poeng = int(question1)
    if poeng > 100: poeng = poeng_max
    cheese = True
    if poeng >= 50:
        print("Bestått")
        cheese = False
        poeng_liste.append(poeng)
        print(poeng_liste)
    else:
        print("Ikke Bestått")
        cheese = False
        poeng_liste.append(poeng)
        print(poeng_liste)