import random
from dataclasses import dataclass, field

@dataclass(order=True)
class Spell:
    """Information about each magic spell"""
    sort_index: int = field(init=False, repr=False)
    name: str
    cost: int 
    damage: int
    type: str = field(repr=False, default="white")

    def __post_init__(self):
        """Sorting criteria (set to cost) for a list of magic spells"""
        self.sort_index = self.cost
        
#magic objects are of the formate -> 'name': 'Fire', 'cost': 10, 'damage': 60}
    def generateSpellDamage(self):
        """Random spell damage generated around the damage power"""
        damageDeviation = 5
        damageLowerLimit = self.damage - damageDeviation
        damageUpperLimit = self.damage + damageDeviation
        return random.randrange(damageLowerLimit, damageUpperLimit)
    