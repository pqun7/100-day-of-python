# #FileNotFoundError
# try:
#     file = open("error.txt")
# except FileNotFoundError as error_masseg:
#     print(f"There was an error {error_masseg}")
#     file = open("error.txt", "w")
# else:
#     print("There was no error")
# finally:
#     raise TypeError("Error I Made up")
#     #print("file has been created")


#2
# height = int(input("Enter your height: "))
# weight = int(input("Enter your weight: "))
# if height > 300:
#     raise ValueError("Human Height is small than 300")
# bmi = weight / (height ** 2)
# print("Your bmi is {:.2f}".format(bmi))

#3
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")
#
# make_pie(8)

#4
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         #total_likes += 0
#         pass
#print(total_likes)


#NATO
import pandas as pd
dict_csv = pd.read_csv(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-26\nato_phonetic_alphabet.csv")

csv_to_dict = {code.letter: code.code for (index, code) in dict_csv.iterrows()}

while True:
    try:
        ask = input("Enter a word: ").upper()
        output_list = [csv_to_dict[letter] for letter in ask]
    except KeyError:
        print("Sorry, only letters in the alphabet")
    else:
        print(output_list)
        break





