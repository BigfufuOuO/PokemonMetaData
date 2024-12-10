import pandas as pd
import numpy as np

with open('Database/game_data/abilities.csv', 'r') as f:
    abilities = pd.read_csv(f)
    
with open('Database/game_data/ability_names.csv', 'r') as f:
    ability_names = pd.read_csv(f)
    
with open('Database/game_data/ability_flavor_text.csv', 'r') as f:
    ability_flavor_text = pd.read_csv(f)
    
result_df = abilities[['id', 'identifier']]
name = ability_names[ability_names['local_language_id'] == 12][['ability_id', 'name']]
result_df = pd.merge(result_df, name, left_on='id', right_on='ability_id', how='left')[['id', 'identifier', 'name']]
flavor_text = ability_flavor_text[(ability_flavor_text['language_id'] == 12) & (ability_flavor_text['version_group_id'] == 20)][['ability_id', 'flavor_text']]
flavor_text['flavor_text'] = flavor_text['flavor_text'].str.replace('\n', '')
result_df = pd.merge(result_df, flavor_text, left_on='id', right_on='ability_id', how='left')[['id', 'identifier', 'name', 'flavor_text']]


result_df['memo'] = np.nan
result_df = result_df.rename(columns={'id': 'ability_id', 'name': 'name_zhHans', 'flavor_text': 'flavor_text_zhHans'})
result_df.to_csv('Database/generate/new_data/abilities.csv', index=False, header=False)
print(result_df)