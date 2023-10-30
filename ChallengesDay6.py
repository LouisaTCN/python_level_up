##Challenge 1 - Use list, write programme which checks each item, and states if True/False
truthy_or_falsey=["0", "Hello!", "", "!!", 12, True, None, "", "0", False, "False"]
for i in truthy_or_falsey:
    if i:
        print(True)
    else:
         print(False)

##Challenge 2 - Create Guest list and a Barred list, if not on list user must wait
print("Hello, what is your name?")
name = input (" > ")
accepted_guestlist = [
    "Louisa",
    "Laura",
    "Lisa"
]
barred_guestlist = [
    "Barry",
    "Brian",
    "Betty"
]
if name in accepted_guestlist:
    print(f"Welcome {name}, please come in!")
elif name in barred_guestlist:
    print(f"Sorry {name}, I can't allow you in!")
else: # else doesn't need a statment
    print(f"Sorry {name}, you are not on the list, please wait whilst I check.")




## Chellenge 3 - Create cash machine
# User to be able to withdraw cash if pin is right

# def cash machine:
# take user prin
# see if pin correct
# if pin correct let them withdraw class
# ## this only works in above scenario
# ~~ Check balance

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




















##Challenge 4 - Add error handling to apple if user doesn't give an interger
print("Apples are 25p each. How many apples would you like to buy?")
while True:
    try:
        num1 = int(input(" > "))
        num2 = 0.25
        break
    except ValueError:
        print("Please use whole numbers") 
cost = num2*num1
print(f"The price for {num1} apples is £{cost}")