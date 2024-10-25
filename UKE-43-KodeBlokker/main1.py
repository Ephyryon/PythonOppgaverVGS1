#	1. Oppgi temperatur
question1 = input("Hvor mange grader er det ute?")
temp = int(question1)
#	2. Hvis temperaturen er høyere enn eller lik 25 grader print("Det er varmt ute, t-skjorte og shorts kan passe i dag")
if temp >= 30 : print("Det er veldig varmt ute, t-skjorte og shorts kan passe i dag")
elif temp >= 21 : print("Det er varmt i dag, en genser er nok.")
else : print("Det er kaldt i dag, kle på deg nok klær")
#	4. else: print("Det er kaldt i dag, kle på deg nok klær")