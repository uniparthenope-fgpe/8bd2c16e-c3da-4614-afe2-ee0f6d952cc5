class MagicalCreature:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return self.name + ' is a ' + self.species