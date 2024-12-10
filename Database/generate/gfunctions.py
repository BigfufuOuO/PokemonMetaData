import json
import sqlite3

class GenerateData:
    def __init__(
            self, 
            file_path: str
        ):
        self.file_path = file_path
        pass
    
    def parse_all(self):
        with open(self.file_path) as f:
            data = json.load(f)
            
        cutoff = data['info']['cutoff']
        meta_name = data['info']['metaname']
        num_battles = data['info']['number of battles']
        for pokemon in data['data']:
            self.parse_single_pokemon(data['data'][pokemon])
    
    def parse_single_pokemon(self, pokemon: dict):
        self.parse_single_items(pokemon['Items'])

    def parse_single_items(self, items: dict):
        total_scaled = 0
        for item in items:
            total_scaled += items[item]
        for item in items: 
            items[item] = round(items[item] / total_scaled * 100, 2) # 保留2位小数
        pass