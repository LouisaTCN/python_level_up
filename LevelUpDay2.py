# print(bool("classical"))
# ## values are Truth or False, not exact boolen true/false
# ## empty string will come back as False - anything empty! True will be with a value entered!

# music = "classical"
# shopping_list = []
# num = 0
# name = ""
# my_name = "Dave"
## empty string will come( back as False - anything empty! True will be with a value entered!
## True/False lets us know if there is data there to work on

## print("What is your name?")
## name = input (" > ")
## if name==True:
##    print(f"Hello {name}, how are you?")
# #else: 
# #    print("You did not give me a name!")
# ## Won't work as string & boolen don't match each other!!!

# print("What is your name?")
# if name:
#     print(f"Hello {name}, how are you?")
# else:
#     print("You did not give me a name!")
# ### ***amend to work - you don't care what name you are given


# ## IN OPERATOR
# ## Use 'IF' if you want just a word to appear as accepted e.g. paint, if gives it will give you the response
# answer = input("What coat is always wet when you put it on?")
# if "paint" in answer:
#     print("Correct!")
# else:
#     print("Incorrect")
# ## so long as give paint in answer will come back as Corect

### HOW TO UPDATE LIST FROM USER IF ITEM NOT ALREADY IN LIST:
##list of shopping items
## programme to allow user to add to shopping list
## if item already in list don't add

# shopping_list=[
#     "Eggs",
#     "Ham",
#     "Spinach",
# ]


# print(shopping_list)
# print(input("What would you like to add to shopping list?"))

# shopping_list.update({input})
# print(shopping_list)


# ##CORRECT WAY TO UPDATE SHOPPING LIST AS ABOVE FROM USER, IF NOT IN LIST
# shopping_list=["eggs", "ham", "spinach"]
# print(shopping_list)

# addional_items = input("Is there anything else you would like to add?")

# if addional_items in shopping_list: ##this is comparing lit to see if already in list   
#     print("This item is already on your list")
# else:
#     shopping_list.append(addional_items)
# print(shopping_list)


# ## NOT OPERATOR
# shopping_list=["eggs", "ham", "spinach"]
# print(shopping_list)

# addional_items = input("Is there anything else you would like to add?")

# if addional_items not in shopping_list: ##this is comparing lit to see if already in list   
#     print("This item is already on your list")
# else:
#     shopping_list.append(addional_items)
# print(shopping_list)




# allowed_answers = ["Yes", "No", "Nope", "Okay"]
# answer = input("what is your answer?")
# while answer not in allowed_answers:
#     print("that is not an acceptalbe answer!")
#     answer = input("what is your answer?")
# else:
#     print("thank you for the response")



# ## RETURN OPERATOR
# def add_up(num1, num2):
#     print(num1+num2)
# add_up(4,7) # Will show 11 as function doing it's job
# print(add_up(4,7)) # Thing told fucntion on this line will print the function so gives 'none' - Function will always return to it's 'Caller'

# def add_up(num1, num2):
#     return(num1+num2) # by adding 'Return' it gives you back the answer - It's telling the code to do it and return the answer, so we can carry on working with it!

# add_up(4,7) # Will show 11 as function doing it's job
# print(add_up(4,7)) # Thing told function on this line will print the function so gives 'none' - Function will always return to it's 'Caller'


# User to be able to withdraw cash if pin is right

# def cash machine:
# take user prin
# see if pin correct
# if pin correct let them withdraw class
# ## this only works in above scenario

# Pin checker:
# see if pin is correct

# Cash Function:


# def pin_checker(user_pin):
#     if user_pin == "1234":
#          return True
# else:
#     return False

# def cash_withdrawal(amount,user_pin):
#     if pin_checker(user_pin):
#         print("you can withdraw {amount}")
# else:
#     print("Your pin was incorrect")

# def change_pin(newpin, user_pin):
#     if pin_checker(user_pin):
#         let them change to the new pin


# ## LIST COMPREHENSION ** THE BELOW ADDS TO A NEW LIST BASED ON FINDING 'SAURUS' IN LIST
# dinsoaurs = [
#     "Tricepatops",
#     "Velociraptor",
#     "Anklyosaurus",
#     "Archaeopteryx",
#     "Tyrannosaurus Rex",
#     "Stegosaurus",
#     "Iguanodon"
# ]
# print(dinsoaurs)
# # if "saurus" in dinsoaurs: ## This doesn't work as looking for just that word in list
# ## So, we use I


# saurus_dinos = []
# for dino in dinsoaurs:
#     if "saurus" in dino: ## this just brings ones back with 'saurus' in it
#         saurus_dinos.append(dino)

# print(saurus_dinos)

# saurus_dinosoaurs=[dino for dino in dinsoaurs if 'saurus' in dino] ## this is same as above for loop working out, but harder to read
# ## first dino above is doing the .append job
# print(saurus_dinos)
# print(saurus_dinosoaurs)


## Lists - lists will print in the order,unless we use a different method to change it
## Tuples are lists but with () rather than[] - only the change in brackets define this
coffee_order=(
    "Louisa - Coffee",
    "Clare - Tea",
    "Paul - Mocha"
)
## You cannot amend a Tuple, so use to keep data safe; cannot be accidentally changed/deleted
## You can only use .count & .index on a Tuple
## You cannot use e.g. .pop, .append .update etc
## Tuples are index positions


# ##Casting - the below is casting as using an int, to allow interger as otherwise would be string and error
# print("type in two numbers to multiple them")
# num1 = int(input(" > "))
# num2 = int(input(" > "))
# print(num1*num2)
# ## If user types in letter,  it would give an error as needs to be interger input
# ## While loop, gives user the chance to enter again

## WHILE TRUE
# print("type in two numbers to multiple them")
# # while True:
#     try: ## try as 192 & 193 are what could go wrong
#         num1 = int(input(" > "))
#         num2 = int(input(" > "))
#         break ## if goes right break loop
#     except: # except handles every kind of error scenario
#         print("Please use intergers only") ## if the above doesn't work give this error message
# print(num1*num2)
## this says rather than break code, give them an exception note to help make it work
## however this would continue to give them try until they get right

### ** This is better as it gives the actual error specific e.g. ValueError (if they entered a letter rather than number)
print("type in two numbers to multiple them")
while True:
    try: ## try as 192 & 193 are what could go wrong
        num1 = int(input(" > "))
        num2 = int(input(" > "))
        break ## if goes right break loop
    except ValueError: #ValueError on this occasion, as trying to get numbers. If any other error it will notify so you can fix
        print("Please use whole numbers") ## if the above doesn't work give this error message
print(num1*num2)