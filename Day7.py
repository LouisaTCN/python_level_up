#Activity 1 - Create lottery number generator (Genrate 6 numbers between 1-50).Ensure number doesn't appear twice
# create list to hold numbers
# import random library .int to 1
# Check if numbers on list - generate till not on list

import random
random_list=[] # random number list
for i in range(6): # telling it to repeat the loop 6 times - generates 6 numbers
  r=random.randint(1,50) # checks if number generated is not in list
  if r not in random_list:
    random_list.append(r) # if number is not on list to add it to list
print(f"Hello the lottery numbers for today are:")
print(random_list)



# # Activity 2
# # Create number guessing game, where user has to say if next number will be higher/lower
# # User can only guess wrong 3 times
# Get random nmber generate rand.int
# Say between 1 - 12 for numbers
# Variable that holds current number, variable to hold new numbers
# Variable that looks how many times gets it wrong
# Counter of how many times gets it right - but def wrong


# import random
# random_list=[] # random number list
# for i in range(1): # telling it to repeat the loop 1 times - generates 1 number
#   r=random.randint(1,50) # checks if number generated is not in list
#   if r not in random_list:
#     random_list.append(r) # if number is not on list to add it to list
# print(f"Do you think the next number is higher or lower than{random_list}")
# user_reponse=input
# if user_reponse=higher:
# random_list = !> print("Correct!")

# lowest_guess=1
# highest_guess=13
# counter=0
# while counter <3: # this is telling it whilst counter is below 3 carry on the 'While loop'
#     print(counter)
#     random_number=random.randint(lowest_guess,highest_guess)
#     print(random_number)
#     user_guess=(input("Do you think the next number will be Lower or Higher?"))
#     random_number2=random.randint(lowest_guess,highest_guess)
#     print(random_number2)
#     if user_guess=="Higher" and random_number2>random_number:
#         print("Correct! The number is higher")
#     elif user_guess=="Lower" and random_number2<random_number:
#         print("Correct! The number is lower")
#     else: 
#         print("Wrong!")
#         counter=counter # adds 1 to couter when wrong
#         print(counter)





# Activity 3
# Create a quiz of 5 questions
# User gets 5 points for each right & lose 2 points for a wrong answer
# Let user answer all 5 questions and display their total at end
# Do as multiple choice (a,b, c etc)

# questions=["Question 1. What is On a standard UK Monopoly board, which is the most expensive location?",
#             "Question 2. Which 'C' is a place where people are buried after death?",
#             "Question 3. Which city is the capital city of Spain?",
#             "Question 4. Who is the oldest son of Queen Elizabeth II?",
#             "Question 5 In the traditional rhyme, how many mice were blind?"]
# print(len(questions))
# answers_choices=["Fleet Street, Oxford Road, Mayfair",
#                  "Cement, Cemetary, Chest",
#                  "Malaga, Marbella, Madrid",
#                  "Charles, Andrew, Eddie",
#                  "None, Eleven, Three"]
# correct_choices=[{"Mayfair"},
#                  {"Cemetary"},
#                  {"Madrid"},
#                  {"Charles"},
#                  {"Three"}]

# score = 0
# for question, answers_choices, correct_choices in zip(questions, answers_choices,correct_choices):
#         print(question)
#         print(answers_choices)
#         user_answer=input()
#         if user_answer in correct_choices:
#             print("Correct")
#             score += 5
#         else:
#             print("Incorrect, the correct answer is correct_choices")
#             score -=2
# print(score, "out of", len(questions)*5)
      

# Activity 4
# Create function that checks if specific film is in the list
# If it is print a successful messge
# If not, update the list at index position 0 (not append as puts it at the end)
# list
# for loop
# possibly look to have 2 seperate lists

# movie_list=["Interview with a Vampire", "Dark Skys", "Dumbo"]
# print("What movie would you like to check if already on the list?")
# user_check=input()

# if user_check in movie_list:
#     print("Yes, that movie is already on the list")
# else:
#     print("That movie is not on the list, I shall add it!")
#     movie_list.insert(0,user_check)
#     print(movie_list)


    

# Activity 5
# Create a programe which takes the users input and if number turns it into a number turn into a interger
# If is String then make the string uppercase
# # check if input is number or string
while True:
  age=input("How old are you?")
  try:
  val = int(input) #Convert it into integer
  print("Input is an integer number. Number = ", val)
  except ValueError:
  print("No.. input is not a number. It's a string").upper





# Acitivity 6
# Create Hide & Seek Programme - see slide
# User should be able enter their name and pick hiding place form a list
# Program should then count out 10 seconds and try to find user
# Programe shoud be allowed 5 attempts
# put pause between each attempt 

# import time
# hiding_places=["wardrobe", "cupboard", "under stairs", "behind shower curtain", "under bed"]
# user_name = input("What is your name?")
# print(f"Hello {user_name}, lets play hide and seek!")
# print("Where would you like to hide?")  
# for i in hiding_places:
#   print (i)
# hidden_place = input("Please type your hiding place: ")
# print(f"You have 10 seconds to hide")

# start_time = time.time()
# for i in range(1,11): # counts to 10
#   print(i)
#   time.sleep(1) # counts down by 1 second
# print("Ready or not here I come!")
# for x in range (1,6): # Loop added to allow 5 tries
    
#   hiding_places_hidden=random.choice(hiding_places)
#   print(f"Is {hiding_places_hidden} your hiding place")
#   user_hiding_place = input("Please say Yes or No: ")

#   if user_hiding_place=="Yes":
#     print("I found you!")
#     break
# print("Game over")
        

