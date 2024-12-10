import csv
import pandas as pd
import numpy as np

with open('Database/game_data/items.csv', 'r') as file:
    items = pd.read_csv(file)
    
with open('Database/game_data/item_names.csv','r') as file:
    item_names = pd.read_csv(file)
    
with open('Database/game_data/item_flavor_text.csv', 'r') as file:
    flavor_text = pd.read_csv(file)
    
# 只保留item_names中，language_id为12的数据
# 当id <= 1658时，保留12；当id > 1658时，保留4
item_unique = items[['id', 'identifier']]

item_1658 = item_names[item_names['item_id'] <= 1658]
item_1658 = item_1658[item_1658['local_language_id'] == 12][['item_id', 'name']]

item_2 = item_names[item_names['item_id'] > 1658]
item_2 = item_2[item_2['local_language_id'] == 4][['item_id', 'name']]
temp = pd.concat([item_1658, item_2], axis=0)
print(temp)
result_df = pd.merge(item_unique, temp, left_on='id', right_on='item_id', how='left')[['id', 'identifier', 'name']]
print(result_df)

# 选择version_group_id为当前组数值最大的数据
print(len(flavor_text))
flavor_text = flavor_text[(flavor_text['version_group_id'] == 20) & (flavor_text['language_id'] == 12)]
# 对所有的flavor_text，去掉\n
flavor_text['flavor_text'] = flavor_text['flavor_text'].str.replace('\n', '')
flavor_text = flavor_text[['item_id', 'flavor_text']]
print(flavor_text)

result_df = pd.merge(result_df, flavor_text, left_on='id', right_on='item_id', how='left')[['id', 'identifier', 'name', 'flavor_text']]

result_df['sprites_url'] = 'https://play.pokemonshowdown.com/sprites/itemicons/' + result_df['identifier'] + '.png'
result_df['memo'] = np.nan

result_df = result_df.rename(columns={'id': 'item_id', 'name': 'name_zhHans', 'flavor_text': 'flavor_text_zhHans'})

result_df.to_csv('Database/generate/new_data/items.csv', index=False, header=False)