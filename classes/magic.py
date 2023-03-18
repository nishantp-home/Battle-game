import random

class Spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type
        
#magic objects are of the formate -> 'name': 'Fire', 'cost': 10, 'damage': 60}
    def generateSpellDamage(self):
        damageDeviation = 5
        damageLowerLimit = self.damage - damageDeviation
        damageUpperLimit = self.damage + damageDeviation
        return random.randrange(damageLowerLimit, damageUpperLimit)
    