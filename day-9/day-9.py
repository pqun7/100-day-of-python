# from replit import clear
# Python Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
# print(programming_dictionary["Function"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]
# exercise 1
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for students in student_scores:
    scoer = student_scores[students]
    if scoer <= 100 and scoer >= 91:
        student_grades[students] = "Outstanding"
    if scoer <= 90 and scoer >= 81:
        student_grades[students] = "Exceeds Expectations"
    if scoer <= 80 and scoer >= 71:
        student_grades[students] = "Acceptable"
    if scoer <= 70 and scoer >= 0:
        student_grades[students] = "Fail"

# 🚨 Don't change the code below 👇
# print(student_grades)
# exercise 2
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(counrty, visits, cities):
    new_dic = {}
    new_dic["country"] = counrty
    new_dic["visits"] = visits
    new_dic["cities"] = cities
    travel_log.append(new_dic)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# exercise 3

# HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
dic_pepole = {}
def bit(dic_pepole):
    ask = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    dic_pepole[ask] = bid

bit(dic_pepole)
yes_no = input("Are there ant other biders? Type Yes, No ")
lower_yes_no = yes_no.lower()
if lower_yes_no == "yes":
    clear()
while lower_yes_no == "yes":
    bit(dic_pepole)
    yes_no = input("Are there ant other biders? Type Yes, No ")
    lower_yes_no = yes_no.lower()
if lower_yes_no == "no":
    names = ""
    bigist_dit = []
    highest_bid = 0
    for kay in dic_pepole:
        bid_amount = dic_pepole[kay]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = kay
        
print(f"The winner is {winner}, with a bid of {highest_bid}")