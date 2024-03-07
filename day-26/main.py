numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
#print(squared_numbers)
even_numbers = [num for num in numbers if num % 2 == 0]

with open("file1.txt", "r") as file1:
    readfile1 = file1.readlines()

with open("file2.txt", "r") as file2:
    readfile2 = file2.readlines()

result = [int(num) for num in readfile1 if num in readfile2]
#print(result)


sentence = "What is the Airspeed Velocity of on Unladen Swallow?"
new_dict = {new_word: len(new_word) for new_word in sentence.split(" ")}
#print(new_dict)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15,
             "Thursday": 14, "Friday": 21,
             "saturday": 22, "sunday":24}
weather_f = {day: (weathe * 9/5) + 32 for day, weathe in weather_c.items() }
#print(weather_f)

#NATO
import pandas as pd
dict_csv = pd.read_csv(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-26\nato_phonetic_alphabet.csv")

csv_to_dict = {code.letter: code.code for (index, code) in dict_csv.iterrows()}
ask = input("Enter a word: ").upper()
output_list = [csv_to_dict[letter] for letter in ask]
print(output_list)
