from game_data import data
from art import logo
from art import vs
import random
from os import system
# random_person1 = random.randint(0, 49)
# random_person2 = random.randint(0, 49)
loop = True
score = 0


def clear():
    return system('cls')
random_person1 = random.randint(0, 49)
first_person = data[random_person1]["name"], data[random_person1]["description"], data[random_person1]["country"]
A = data[random_person1]['follower_count']
while loop == True:
    print(logo)
    random_person2 = random.randint(0, 49)
    second_person = data[random_person2]["name"], data[random_person2]["description"], data[random_person2]["country"]
    B = data[random_person2]['follower_count']
    print(f"your score is {score}")
    print(f"Compare A: {first_person}")
    #print(A)
    print(vs)
    print(f"Compare B: {second_person}")
    #print(B)
    ask = input("Who was more follower? 'A', 'B' ")
    if first_person == second_person and A == B:
        random_person2 - 1
    if ask == "a":
        if A > B:
            score += 1
            first_person = second_person
            A = B
            clear()
        else:
            loop = False
    if ask == "b":
        if A < B:
            score += 1
            first_person = second_person
            A = B
            clear()
        else:
            loop = False
clear()
print(f"Sorry that's not wrong. Final score {score}")
