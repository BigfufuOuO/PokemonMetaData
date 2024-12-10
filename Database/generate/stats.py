import pandas as pd
import numpy as np

with open('Database/game_data/stats.csv', 'r') as f:
    stats = pd.read_csv(f)

with open('Database/game_data/stat_names.csv', 'r') as f:
    stat_names = pd.read_csv(f)
    
result_df = stats[['id', 'identifier']]
stat_names = stat_names[stat_names['local_language_id'] == 12][['stat_id', 'name']]
result_df = pd.merge(result_df, stat_names, left_on='id', right_on='stat_id', how='left')[['id', 'identifier', 'name']]

print(result_df)
result_df.to_csv('Database/generate/new_data/stats.csv', index=False, header=False)