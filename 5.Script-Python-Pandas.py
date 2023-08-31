import pandas as pd
brics = pd.read_csv("brics.txt") 
print(brics.sort_values(by=['Paises'], ascending=True))