import pandas as pd
data = pd.read_csv("ssbmedier.csv", index_col = 0, skiprows = (0, 1), \
    sep =";", na_values=[".", ".."], encoding = "latin-1")
K = []   # lager ei tom liste K 
startVerdi = 2010   # lager variabel for det første årstallet
for i in range(0, 10):
    K.append(startVerdi + i)
data.columns = K  # setter radoverskriftene i variabelen data lik innholdet av lista K 
print(data.describe())
data.plot()