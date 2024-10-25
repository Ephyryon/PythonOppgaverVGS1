er_helg = True

words = "It's weekend right now."
words2 = "Ok, thats fair."
words3 = "That's a bad exscuse. Go to school."

question = input("Is it weekend right now?")
question2 = input("Then why aren't you at school?")

if question == "Yes": er_helg = True
if not er_helg : question2 
else : print(words)
if question2 == "" : print(words2)
else : print(words3)