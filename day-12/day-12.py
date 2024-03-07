import random
art = """
 ▄▄ • ▄• ▄▌▄▄▄ ..▄▄ · .▄▄ · ▪   ▐ ▄  ▄▄ •      ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .
▐█ ▀ ▪█▪██▌▀▄.▀·▐█ ▀. ▐█ ▀. ██ •█▌▐█▐█ ▀ ▪    ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·
▄█ ▀█▄█▌▐█▌▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄▐█·▐█▐▐▌▄█ ▀█▄    ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄
▐█▄▪▐█▐█▄█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌██▐█▌▐█▄▪▐█    ▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌
·▀▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▀▀▀▀ █▪·▀▀▀▀     ·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀ 
"""
print(art)
easy_level = 10
hard_level = 5
def game(easy_level,hard_level):
    print("Welcome to guess the number")
    print("I'm thinking of a number between 1 and 100.")
    the_number = random.randint(0,99)
    choose_player = input("choose a level. Type 'easy' or 'hard': ")
    if choose_player == "easy":
        while easy_level != 0:
            print(f"you have a {easy_level} attempts remaining guess tne number.")
            guess_number = int(input("guess a number: "))
            if guess_number < the_number:
                print("Too low!")
                easy_level -= 1
            if guess_number > the_number:
                print("Too high!")
                easy_level -= 1 
            if guess_number == the_number:
                print(f"you win! the number {the_number}")
                easy_level = 0
        if guess_number != the_number:
            print(f"you lost! the number {the_number}") 
        
    if choose_player == "hard":
        while hard_level != 0:
            print(f"you have a {hard_level} attempts remaining guess tne number.")
            guess_number = int(input("guess a number: "))
            if guess_number < the_number:
                print("Too low!")
                hard_level -= 1
            if guess_number > the_number:
                print("Too high!")
                hard_level -= 1 
            if guess_number == the_number:
                print(f"you win! the number {the_number}")
                hard_level = 0
        if guess_number != the_number:
            print(f"you lost! the number {the_number}")             
game(easy_level,hard_level)        
