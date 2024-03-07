import random


def first():
    student_heights = input("Input a list of student heights ").split(" ")
    q = 0
    w = 0
    for x in student_heights:
        q = q + int(x)
    for d in student_heights:
        w = w + 1
    total = q / w
    print(total)


def hi():
    student_scores = input("Input a list of student scores ").split()
    for x in range(0, len(student_scores)):
        student_scores[x] = int(student_scores[x])
    print(student_scores)
    # 🚨 Don't change the code above 👆
    highst_score = 0
    # Write your code below this row 👇
    for score in student_scores:
        if score > highst_score:
            highst_score = score
    print(f"The highest score in the class is: {highst_score}")

    total = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total += number
    print(total)
    # The easiest way
    total2 = 0
    for number2 in range(2, 101, 2):
        total2 += number2
    print(total2)


def fizz_buzz():
    print("Fizz buzz GAME")
    for fizz in range(1, 101):
        if fizz % 3 == 0 and fizz % 5 == 0:
            print("Fizz buzz")
        elif fizz % 3 == 0:
            print("Fizz")
        elif fizz % 5 == 0:
            print("buzz")
        else:
            print(fizz)
    print(fizz)


# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# result_letters = []
# for letter in range(0, nr_letters):
#    result_letters += random.choice(letters)

# result_symbols = []
# for symbol in range(0, nr_symbols):
#    result_symbols += random.choice(symbols)

# result_numbers = []
# for number in range(0, nr_numbers):
#      result_numbers += random.choice(numbers)
# not_random = result_letters+result_symbols+result_numbers
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
result_all = []
for letter in range(0, nr_letters):
    result_all.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    result_all.append(random.choice(symbols))

for number in range(0, nr_numbers):
    result_all.append(random.choice(numbers))
#not_random = result_letters+result_symbols+result_numbers
random.shuffle(result_all)
passwords = ""
for char in result_all:
    passwords += char
print(f"your password is {passwords}")  
