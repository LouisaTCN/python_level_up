# this file is just the instructions to run the file in Main!

class Person():

    def __init__(self, person_name, person_age, person_height, person_weight):
        self.name = person_name
        self.age = person_age
        self.height = person_height
        self.weight = person_weight

    def set_job(self, job_title):
        allowed_jobs = ["developer", "instructor", "finance", "HR", "admin", "compliance"]
        while job_title not in allowed_jobs:
            print("This is not a role within this company")
            print("Please enter your job title again")
            job_title=input()
        self.job = job_title    
    
    def set_new_name(self, person_name): #allows this to be updated later on
        self.name = person_name

    def set_hair_colour(self, hair_colour): # this was added in after the 1st def_init *You add it in after otherwise would break the otehrs which don't have this already input!
        self.hair_colour = hair_colour



    def introduce(self):
        print(f"Hello my name is {self.name}, I am {self.age}, and I am {self.height}")

    def get_age(self):
         return self.age
        
    def get_bmi(self):
         return self.height * self.weight