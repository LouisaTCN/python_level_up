# capital_cities = {
#     "England" : "London",
#     "Cheshire" : "Chester",
#     "Scotland" : "Edinburgh",
#     "Wales" : "Cardiff",
#     "Northern Ireland" : "Belfast ",
#     "Ireland" : "Dublin"
# }
# ## You have to add "" against each Key/Value
# ## Dictonary Data has 2 points = Key:Value
# print(capital_cities)
# #Dictionaries don't have index like coffee list. It goes by it's Key
# ## You can only have 1 key and if it duplicates it will only read last one
# print(capital_cities["England"])

# coffee_order = [
#    "Louisa = Coffee",
#    "Jane = Tea"
# ]


# ## This is how to change coffee order to Dictionary so that you can look up by Key not by index no
# #coffee_order = {
#     "Louisa : Coffee",
#     "Jane : Tea"
# }
# print(coffee_order["Louisa"])


# #Activity1
# animals = {
#    "Dog" : "Puppy",
#    "Cat" : "Kittens",
#    "Lion" : "Cub",
#    "Peacock" : "Peahen"
# }
# print(animals["Lion"])

# ## 'Key' cannot be changed, but a value can
# animals["Cat"] = "Kitty"
# print(animals)
# ## this changes the 'Value'

# animals = {
#    "Dog" : "Puppy",
#    "Cat" : "Kittens",
#    "Lion" : "Cub",
#    "Peacock" : "Peahen"
# }

# print(animals.keys())
# ## this just returns the list of 'Keys'
# print(animals.values())
# ## this just returns the list of 'Values'
# print(animals.items())
# ## this gives you the list of items in their groupings e.g. ('Dog', 'Puppy'), ('Cat', 'Kittens')

# print(animals.get("Lion"))
# print(animals["Lion"])

# print(animals.get("Dragon"))
# print(animals["Dragon"])
# ## Get will give us back a 'None' response rather than an error
## .get is better as doesn't give fatal error

# print(animals.get("Dragon", "We couldn't find a baby animal for that parent"))
# ## this changs the .get response from 'None' to what is above


# animals = {
#    "Dog" : "Puppy",
#    "Cat" : "Kittens",
#    "Lion" : "Cub",
#    "Peacock" : "Peahen"
# }
# print(animals.setdefault("Lion", "Baby Lion"))
# ## this won't allow you to change Lion as it already exists as a Key in the Directory with a Value
# animals.setdefault("Pig", "Piglet")
# ## this will add a new item and allows as not in the Directory
# print(animals)

# # animals.update({"Fish" : "Fry", "Cow" : "Calf"})
# # ## .updates merges 2 Dictionaries into 1
# # print(animals)

# # animals.update({"Lion" : "Baby Lion"})
# # ## will update the original Dictionary

# animals.pop("Peacock")
# print(animals)
# ## this removes that Key & it's Value from the list

# animals.popitem()
# ## this removes the last item from the list


## Challenge 1
artist_songs = {
    "Madonna" : "Papa Don't Preach",
    "Adele" : "Rolling in The Deep",
    "Amy Winehouse" : "Rehab",
    "Lady Gaga" : "Poker Face",
    "Pink Floyd" : "Another Brick in the Wall"
}
print(artist_songs)

## add 2 new items to Dictionary
artist_songs.update({"London Grammar" : "Strong", "Portishead" : "Glory Box"})
print(artist_songs)

## Challenge 1 Stretch
## Print fav song using 'for loop'
###***** STILL TO DO********** 

##Challenge 2
##Create Dictonary where country is Key and Language is Value
countries = ["England", "Spain", "Ethiopia", "Iran"]

languages = ["English", "Spanish", "Amharic", "Farsi"]
my_dict=dict(zip(countries, languages))
print(my_dict)
## Zip function combines two lists into a dictionary

##Challenge 3
## from animal Dictionary, allow user to search for an animal and see the corresponding young name. If does not exist return a suitable message
animals = {
    "Dog" : "Puppy",
    "Cat" : "Kittens",
    "Lion" : "Cub",
    "Peacock" : "Peahen"
}
animal_of_choice= input("What animal would you like to serach?")
print(animals.get(animal_of_choice, "We couldn't find a baby animal for that parent"))
## you need to only give it 1 parameter, as the below would give "None. We couldn't find a baby animal for that parent", as you are giving it 2 parameters in the below.
##print(animals.get(animal_of_choice), "We couldn't find a baby animal for that parent"))
