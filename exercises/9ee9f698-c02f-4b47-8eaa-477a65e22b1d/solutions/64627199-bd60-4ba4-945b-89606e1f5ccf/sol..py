class Wizard:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def cast_spell(self, spell):
        print(f'{self.name} casts {spell}!')

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} takes {damage} damage! Health now: {self.health}')

harry = Wizard('Harry')
harry.cast_spell('Expelliarmus')
harry.take_damage(20)