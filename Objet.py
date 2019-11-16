
class Objet:
    
    def __init__(self):
        self.name = name
        self.power = power
        self.kind = kind

class equipment (Objet):
    def __init__(self):
        self.damage = damage
        self.kind = kind # s'il s'agit d'une arme, jewel, or armor
        self.raise_armor = raise_armor

class consumable(Objet):
    def __init__(self):
        self.nb_uses = nb_uses

