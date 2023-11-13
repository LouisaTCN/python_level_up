#This file works with superhero.py file

from superhero import Superhero

spiderman = Superhero("Spiderman", "Peter Parker", "Spidey Sense", "Venom",)

print(f"{spiderman.identity} is actually {spiderman.name}, and fights the evil {spiderman.enemy} with his {spiderman.power}")

hulk = Superhero("The Incredible Hulk", "Bruce Banner", "Super Strength", "Abomination")

print(f"{hulk.identity} is actually {hulk.name}, and fights the evil {hulk.enemy} with his {hulk.power}")

dr = Superhero("Doctor Strange", "Stephen Strange", "Magic", "Dormammu")

print(f"{dr.identity} is actually {dr.name}, and fights the evil {dr.enemy} with his {dr.power}")

storm = Superhero("Storm", "Ororo Munroe", "Atmokinesis", "Magneto")

print(f"{storm.identity} is actually {storm.name}, and fights the evil {storm.enemy} with her {storm.power}")

# Adding Lairs:
spiderman.set_lair("Web")
hulk.set_lair("cave")
dr.set_lair("hell")
storm.set_lair("sky")
print(hulk.lair)

list_of_lairs = [spiderman.get_lair(), hulk.get_lair(), storm.get_lair()] # Using 'Getter' to make a list
print(list_of_lairs)