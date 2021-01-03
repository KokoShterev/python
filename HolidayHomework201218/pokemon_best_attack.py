import pandas as pd
import json

df_pokemon_data = pd.read_csv('pokemon_data.csv')

with open('effectiveness.json') as f:
    effectiveness = json.load(f)

df_pokemon_data['DPS'] = df_pokemon_data['Attack'] * df_pokemon_data['Speed'] / 100
pokemon = input('Choose your enemy pokemon: ')
pokemon_data = df_pokemon_data.loc[df_pokemon_data['Name'] == pokemon]

t = []
for i in effectiveness[pokemon_data.iloc[0,2]]:
    effective_pokemons = df_pokemon_data.loc[df_pokemon_data['Type 1'] == i]
    t.append(effective_pokemons.loc[effective_pokemons['DPS'].idxmax()][['Name', 'DPS']])

t = pd.DataFrame(t) #NEVER grow a DataFrame!
print(t.loc[t['DPS'].idxmax()]['Name'] + ' is the best decision.')