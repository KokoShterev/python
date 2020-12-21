import pandas as pd

df_pokemon_data = pd.read_csv('pokemon_data.csv')
effectiveness = {
    "Fairy": ["Poison", "Steel"],
    "Steel": ["Fire", "Fighting", "Ground"],
    "Dark": ["Fighting", "Bug", "Fairy"],
    "Dragon": ["Ice", "Dragon", "Fairy"],
    "Ghost": ["Ghost", "Dark"],
    "Rock": ["Water", "Grass", "Fighting", "Ground", "Steel"],
    "Bug": ["Fire", "Flying", "Rock"],
    "Psychic": ["Bug", "Ghost", "Dark"],
    "Flying": ["Electric", "Ice", "Rock"],
    "Ground": ["Water", "Grass", "Ice"],
    "Poison": ["Ground", "Psychic"],
    "Fighting": ["Flying", "Psychic", "Fairy"],
    "Ice": ["Fire", "Fighting", "Rock", "Steel"],
    "Grass": ["Fire", "Ice", "Poison", "Flying", "Bug"],
    "Electric": ["Ground"],
    "Water": ["Electric", "Grass"],
    "Fire": ["Water", "Ground", "Rock"],
    "Normal": ["Fighting"],
}

df_pokemon_data['DPS'] = df_pokemon_data['Attack'] * df_pokemon_data['Speed'] / 100
pokemon = str(input('Choose your enemy pokemon: '))
pokemon_data = df_pokemon_data.loc[df_pokemon_data['Name'] == pokemon]
t = []
for i in effectiveness[pokemon_data.iloc[0,2]]:
    effective_pokemons = df_pokemon_data.loc[df_pokemon_data['Type 1'] == i]
    effective_pokemons = effective_pokemons.sort_values('DPS')
    t.append(list(effective_pokemons.tail(1)['Name']) + list(effective_pokemons.tail(1)['DPS']))
t.sort(key = lambda x: x[1], reverse = True)
print(t[0][0] + ' is the best decision.')