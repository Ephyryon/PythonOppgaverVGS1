alder = 0

Ja = ["Yes", "yes", "Ja", "ja"]
Nei = ["No", "no", "Nei", "nei"]
answers = [Ja, Nei]
answered = False

def check_input(input_value, list_of_lists):
    for sublist in list_of_lists:
        if input_value in sublist:
            return True
    return False

while not answered: 
    question = input("Er du over 18 eller 18 år gammel? Ja/Nei")
    if not check_input(question, answers):
        print("Invalid Input")
    elif question in Ja:
        alder = 18
        answered = True
    elif question in Nei:
        alder = 17
        answered = True

if alder >= 18 and answered:
    print("Du er myndig!")
elif answered:
    print("Du er et barn siden du er yngre enn 18.")
