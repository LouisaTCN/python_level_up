#This file works with person.py file

from person import Person

liam = Person("Liam",30,"Tall")
katy = Person("Katy","32", 1.62, 11) # no brackets around height & weight as intergers!

print(katy.name)
print(katy.age)
print(katy.height) 

#katy.name = "Katherine" #this updates the name Katy to Katherine
#shouldn't do this by changing name as should use 'Setter'!


dave = Person("Dave", 50, "6 ft 6")
alex = Person("Alex",45, "5ft 5")

print(f"Hello my name is {katy.name}, I am {katy.age}, and I am {katy.height}")
print(f"Hello my name is {dave.name}, I am {dave.age}, and I am {dave.height}")

#ERROR: alex.introduce() #** need to do something at top to make this work
#ERROR: dave.introduce()

#The below is a setter and re-assigns the persons name
def set_new_name(self, person_name):
    self.name = person_name # update property with new name self
katy.set_new_name("Katherine")
print(katy.name)


print(katy.age)
print(katy.get_age()) # does same thing as above but easier for user to undertand this one

print(katy.get_bmi())