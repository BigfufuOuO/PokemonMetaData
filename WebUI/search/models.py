from django.db import models

# Create your models here.
class Items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    name_zhHans = models.CharField(max_length=50)
    sprites_url = models.TextField()
    flavor_text_zhHans = models.TextField()
    memo = models.TextField()
    
    def __str__(self):
        return self.name_zhHans

class Abilities(models.Model):
    ability_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    flavor_text_zhHans = models.TextField()
    memo = models.TextField()
    
    def __str__(self):
        return self.name_zhHans
    
class Stats(models.Model):
    stat_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_zhHans
    
class Natures(models.Model):
    nature_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    decrease_stat_id = models.ForeignKey(Stats, on_delete=models.CASCADE, 
                                         to_field='stat_id',
                                         related_name='decrease_stat')
    increase_stat_id = models.ForeignKey(Stats, on_delete=models.CASCADE, 
                                         to_field='stat_id',
                                         related_name='increase_stat')
    
    def __str__(self):
        return self.name_zhHans
    
class Types(models.Model):
    type_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    sprites_url = models.TextField()
    
    def __str__(self):
        return self.name_zhHans

class MovesTarget(models.Model):
    target_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_zhHans

class MovesDamageClasses(models.Model):
    damage_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_zhHans
    
class MovesEffect(models.Model):
    effect_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_zhHans

class Moves(models.Model):
    move_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length = 50)
    name_zhHans = models.CharField(max_length=50)
    type_id = models.ForeignKey(Types, on_delete=models.CASCADE, to_field='type_id')
    power = models.IntegerField()
    pp = models.IntegerField()
    accuracy = models.IntegerField()
    priority = models.IntegerField()
    target_id = models.ForeignKey(MovesTarget, on_delete=models.CASCADE, to_field='target_id')
    damage_classes_id = models.ForeignKey(MovesDamageClasses, on_delete=models.CASCADE, to_field='damage_id')
    effect_id = models.ForeignKey(MovesEffect, on_delete=models.CASCADE, to_field='effect_id')
    effect_chance = models.IntegerField()
    
class Pokemon(models.Model):
    pokemon_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    species_id = models.IntegerField()
    sprites_url = models.TextField()
    
    def __str__(self):
        return self.name_zhHans
    
class PokemonSpecies(models.Model):
    species_id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=50)
    name_zhHans = models.CharField(max_length=50)
    
class PokemonAbilities(models.Model):
    pokemon_id = models.IntegerField()
    ability_id = models.IntegerField()
    is_hidden = models.BooleanField()
    slot = models.IntegerField()
    
class PokemonTypes(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()
    
# ============= Battle =============
class PokemonBattle(models.Model):
    pokemon_id = models.IntegerField()
    collect_time = models.DateField()
    userate = models.FloatField()
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    item_userate = models.FloatField()
    nature = models.ForeignKey(Natures, on_delete=models.CASCADE)
    nature_userate = models.FloatField()
    efffort_values = models.TextField()
    effort_userates = models.TextField()
    tera_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    tera_type_userate = models.FloatField()
    ability = models.ForeignKey(Abilities, on_delete=models.CASCADE)
    ability_userate = models.FloatField()
    moves = models.ForeignKey(Moves, on_delete=models.CASCADE)
    moves_userates = models.TextField()
    
    