class MagicalCreature:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def fly(self):
        return f'{self.name} the {self.species} is flying!'

    def speak(self):
        return f'{self.name} says: Hello!'

creature = MagicalCreature('Fawkes', 'Phoenix')
print(creature.fly())
print(creature.speak())