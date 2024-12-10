import pandas as pd
import numpy as np

with open('Database/game_data/types.csv', 'r') as f:
    types = pd.read_csv(f)

with open('Database/game_data/type_names.csv', 'r') as f:
    type_names = pd.read_csv(f)
    
result_df = types[['id', 'identifier']]
name = type_names[type_names['local_language_id'] == 12][['type_id', 'name']]
result_df = pd.merge(result_df, name, left_on='id', right_on='type_id', how='left')[['id', 'identifier', 'name']]

result_df['sprites_url'] = 'https://play.pokemonshowdown.com/sprites/types/' + result_df['identifier'].str.capitalize() + '.png'

print(result_df)
result_df.to_csv('Database/generate/new_data/types.csv', index=False, header=False)