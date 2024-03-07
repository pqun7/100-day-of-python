import random


def heads_tails():
    Heads_and_Tails = input("Heads or Tails? ").title()
    random_heads = random.randint(0, 1)
    if random_heads == 0 and Heads_and_Tails == 'Heads':
        print("Heads You W")

    elif random_heads == 1 and Heads_and_Tails == 'Heads':
        print("Tails You L")

    if random_heads == 1 and Heads_and_Tails == 'Tails':
        print("Tails You W")

    elif random_heads == 0 and Heads_and_Tails == 'Tails':
        print("Heads You L")
heads_tails()

# def second_challenge():
#     names_string = input("Give me everybody's names, separated by a comma. ")
#     names = names_string.split(", ")
#     random_names = len(names)
#     random = random.randint(0, random_names - 1)
#     new_list = names[random]
#     print(f"{new_list}, the porson who gina pay ")
#
# # الطريقه السهله لاختيار اسم عشؤائي من لست
#
#
# def random_name():
#     my_list = ["ali", "ahmed", "pay", "today"]
#     ra = random.choice(my_list)
#     print(ra)
#
#
# def map():
#     # 🚨 Don't change the code below 👇
#     row1 = ["⬜️", "⬜️", "⬜️"]
#     row2 = ["⬜️", "⬜️", "⬜️"]
#     row3 = ["⬜️", "⬜️", "⬜️"]
#     map = [row1, row2, row3]
#     print(f"{row1}\n{row2}\n{row3}")
#     position = input("Where do you want to put the treasure? ")
#     # 🚨 Don't change the code above 👆
#
#     # Write your code below this row 👇
#     width = int(position[0])
#     length = int(position[1])
#     row_sel = map[width - 1][length - 1] = 'X'
#     # Write your code above this row 👆
#
#     # 🚨 Don't change the code below 👇
#     print(f"{row1}\n{row2}\n{row3}")
#
#
# ask = int(
#     input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# if ask == 0:
#     print(rock)
# if ask == 1:
#     print(paper)
# if ask == 2:
#     print(scissors)
# print('compare: ')
# rock_paper_scissors = [rock, paper, scissors]
# compare = random.choice(rock_paper_scissors)
# print(compare)
# if compare == paper and ask == 0:
#     print('You lost')
# if compare == scissors and ask == 1:
#     print('You lost')
# if compare == rock and ask == 2:
#     print('You lost')
#
# if ask == 0 and compare == scissors:
#     print('You Win!')
# if ask == 1 and compare == rock:
#     print('You Win!')
# if ask == 2 and compare == paper:
#     print('You Win!')
#
# if ask == 0 and compare == rock:
#     print("Draw!")
# if ask == 1 and compare == paper:
#     print("Draw!")
# if ask == 2 and compare == scissors:
#     print("Draw!")
