# this file is just the instructions to run the file in Main!



class Superhero():
    def __init__(self, name, identity, power, enemy):
        self.name = name
        self.identity = identity
        self.power = power
        self.enemy = enemy

    def set_lair(self, lair):# 'Setter ' for Adding a lair to above class & objects
         self.lair = lair

    def get_lair(self):
        return self.lair

