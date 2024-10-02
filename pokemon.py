import numpy as np
import pandas as pd

pokemon = pd.read_csv('pokemon_data.csv') #prints the first 5 and the last 5 

print(pokemon)
print(pokemon.columns)

#access one column (series of data)
print(pokemon['Type 1'])
print(pokemon.HP)

#create new column for attack/sp. atk ratio 
pokemon['Attack Ratio'] = pokemon['Attack'] / pokemon['Sp. Atk']
print(pokemon['Attack Ratio'])

poke = pokemon.set_index('Name')

#Access a specific 'cell' (row, col)
#Error
print(poke.loc['Pikachu', 'Type 1'])

#access a range of rows 
print(poke.loc[['Bulbasaur','Squirtle','Charmander']])

for index, row in poke.iterrows():
    print(index, '-', row['Type 1'])