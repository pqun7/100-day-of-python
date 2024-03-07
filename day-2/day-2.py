#first challenge
def First_Challenge():
    two_digit_number = input('type a two digit number: ')
    number_1 = two_digit_number[0]
    number_2 = two_digit_number[1] 
    print(int(number_1)+int(number_2))
#the second challenge
def Second_Challenge():
    print(3 * (3 + 3) / 3- 3)

#the third challenge
def Third_Challenge():
    print('Body mass')
    height = input('enter your height in m: ')
    weight = input('enter your weight in k: ')
    rezolt = int(weight) / (float(height) / 100) ** 2
    rezolt_at_int = float(rezolt)
    print(round(rezolt_at_int,2))

#the fourth challenge
def Fourth_Challenge():
    age = int(input('What is your current age: ')) 
    year = 90 - age
    months = year * 12
    weeks = year * 52
    days = year * 365
    print(f'you have {days} days, {weeks} weeks, and {months} months left.')

#First_Challenge()
#Second_Challenge()
#Third_Challenge()
#Fourth_Challenge()
