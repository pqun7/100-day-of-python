# first challenge
def first_challenge():
    number = int(input("Which number do you want to check "))
    if number % 2 == 1:
        print("This is an odd number")
    else:
        print("This is an even number")


# the second challenge
def second_challenge():
    print('Body mass')
    height = input('enter your height in m: ')
    weight = input('enter your weight in k: ')
    rezolt = int(weight) / (float(height) / 100) ** 2
    rezolt_at_int = float(rezolt)
    if rezolt_at_int <= 18.5:
        print(f"Your BMI is {round(rezolt_at_int,2)}, you are underweight")
    elif rezolt_at_int <= 25:
        print(f"Your BMI is {round(rezolt_at_int,2)}, you are normal weight")
    elif rezolt_at_int <= 30:
        print(f"Your BMI is {round(rezolt_at_int,2)}, you are overweight")
    elif rezolt_at_int <= 35:
        print(f"Your BMI is {round(rezolt_at_int,2)}, you are obese")
    else:
        print(
            f"Your BMI is {round(rezolt_at_int,2)}, you are clinically obese")
# the third challenge


def third_challenge():
    year = int(input("Which year do you want to check: "))
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 != 0:
                print("leap year")
    else:
        print("not leap year")


def fourth_challenge():
    height = int(input("How your height: "))
    if height > 120:
        print("you cant ride")
    else:
        print("you can't")
        exit()
    age = int(input("how old are you: "))
    if age < 12:
        print("you bill is $5")
        bill = 5
    elif age < 18:
        print("you bill is $7")
        bill = 7
    elif age >= 45 and age <= 50:
        print("you pay is $0")
        bill = 0
    else:
        print("you pay is $12")
        bill = 12
    photo = (input("do you want a photos "))
    if photo == 'yes':
        print("+$3")
        new_bill = bill + 3
    if photo == "no":
        print(f"you totel bill is {bill}")
    print(f"you totel bill is {new_bill}")

# Fifth challenge


def Fifth_challenge():
    print("Welcome To python pizza")
    size = input("What size do you want? S, M, L ")
    add_pepperoni = input("Do you want pepperoni? Y, N ")
    extra_cheese = input("Do you want extra cheese? Y, N ")
    bill = 0
    if size == "s":
        bill += 15
        if add_pepperoni == "y":
            bill += 2
        elif add_pepperoni == "n":
            bill += 0
    if size == "m":
        bill += 20
        if add_pepperoni == "y":
            bill += 3
        elif add_pepperoni == "n":
            bill += 0
    if size == "l":
        bill += 25
        if add_pepperoni == "y":
            bill += 3
        elif add_pepperoni == "y":
            bill += 0
    if extra_cheese == "y":
        bill += 1
    elif extra_cheese == "n":
        bill += 0
    print(f"You Total bill is {bill}")

    # IF
    # A and B
    # لن يتحقق الا اذا كان الاشرطين صحيحين
    # A or B
    # سوف يتحقق اذا كان واحد منهم صحيح او الاثنين
    # not E
    # لو الشرط صحيح بيجي فولس اما اذا الشرط خطا بيجي ترو


# 6 challenge
#def sex_challenge():
name1 = input("What is your name: \n")
name2 = input("What is their name: \n")
name_compile = name1 + name2
name_lower = name_compile.lower()
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
true = t + r + u + e
print(f'T occues {t}',end = '\n')
print(f'r occues {r}',end = '\n')
print(f'u occues {u}',end = '\n')
print(f'e occues {e}',end = '\n')
print(f"Total = {true}\n")
l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
love = l + o + v + e
print(f'l occues {l}',end = '\n')
print(f'o occues {o}',end = '\n')
print(f'v occues {v}',end = '\n')
print(f'e occues {e}',end = '\n')
print(f"Total = {love}\n")
str_total = str(true) + str(love)
total = int(str_total)
if total >= 0 and total <= 10 and total >= 90 and total <= 100:
    print(f'Your score is {total},you go together like coke and mentos.')
if total >= 40 and total <= 50:
    print(f"Your score is {total},you alright together")
else:
     print(f"Your score is {total}")

def sev_challenge():
    print('''*******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/______/
    *******************************************************************************
    ''')
    print('Welcome to Treasure Island.')
    print('Your mission is to find the treasure.')
    first_ask = input("where do you want to go, left ,right ")
    lower_first_ask = first_ask.lower()
    if lower_first_ask == 'right':
        sik_ask = input("There are three boats in front of you what are you going to choose, red ,blue,black: ")
        lower_sik_ask = sik_ask.lower()
        if lower_sik_ask == "blue":
            print("There's a hole in the boat. you lost")
            exit()
        if lower_sik_ask == "red":
            print("The boat is weak and it's broken, you lost")
            exit()   
        if lower_sik_ask == 'black':
                print("The boat is intact and working great. Now, where are you going? ")
                thr_ask = input("There are two islands in front of you, right or left: ")
                lower_thr_ask = thr_ask.lower()
                if lower_thr_ask == "left":
                    print("You are on Treasure Island, you won")
                if lower_thr_ask == "right":
                    print("The island is deserted and there is nothing on it, you lost")
                    exit()
    if lower_first_ask == 'left':
        one_ask = input("There are three planes in front of you, red, blue, black: ") 
        lower_one_ask = one_ask.lower()
        if lower_one_ask == "black":
            print("The engine is broken, you will fall into the sea you lost")
            exit()
        if lower_one_ask == "red":
            print("An animal was hit by a propeller and fell into the sea you lost")
            exit()   
        if lower_one_ask == 'blue':
            print("The plane is working great.")
            two_ask = input("There are two islands in front of you. Which market should you choose, right or left? ")
            lower_two_ask = two_ask.lower()
            if lower_two_ask == "right":
                print("You are on Treasure Island, you won")
            if lower_two_ask == "left":
                print("The island is deserted and there is nothing on it, you lost")
                exit()
             

second_challenge()             