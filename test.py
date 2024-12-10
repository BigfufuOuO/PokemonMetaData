# sigmoid 
import json

with open('Database/battle_data/gen9vgc2024regh-1630.json') as f:
    data = json.load(f)
    
total = 0
for item in data['data']['Sneasler']['Items']:
    total += data['data']['Sneasler']['Items'][item]

print(total)