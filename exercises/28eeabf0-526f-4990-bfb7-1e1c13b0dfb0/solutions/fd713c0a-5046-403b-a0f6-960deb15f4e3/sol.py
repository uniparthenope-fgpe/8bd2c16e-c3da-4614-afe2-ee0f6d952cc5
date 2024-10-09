class MagicalCreature:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat
    
    def __str__(self):
        return self.name + ' is a ' + self.species + ' found in ' + self.habitat