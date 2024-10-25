#	1. Oppgi temperatur
question1 = input("Hvor mange grader er det ute?")
temp = int(question1)
#	2. Hvis temperaturen er høyere enn eller lik 25 grader print("Det er varmt ute, t-skjorte og shorts kan passe i dag")
if temp >= 25 : print("Det er varmt ute, t-skjorte og shorts kan passe i dag")
elif temp >= 5 : print("Det er ikke så varmt i dag, en genser eller jakke kan passe i dag")
else : print("Det er kaldt i dag, kle på deg nok klær")
#	4. else: print("Det er kaldt i dag, kle på deg nok klær")