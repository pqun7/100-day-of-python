# exercise 1
# Write your code below this line 👇
def paint_calc(height, width, cover):
    rezlot = (test_h * test_w) / coverage
    return rezlot


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.
# 🚨 Don't change the code below 👇
def exercise_1():
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)
    round_paint = round(paint_calc(test_h,test_w,coverage))
    print(f"You'll need {round_paint} cans of paint.")

# exercise 2
# Write your code below this line 👇
def prime_chaker(number):
    zero = 0
    not_prime = 0
    for prime in range(2,number):
        if prime != number:
            if number % prime == 0:
                zero =+ 1
                not_prime =+ 1
    if not_prime > 0:
        print("It's not a prime number!")
    if zero == 0:
        print("It's prime number!")              
  
# Write your code above this line 👆
# Define a function called prime_chaker() so that the code below works.
# 🚨 Don't change the code below 👇
def exercise_2():
    n = int(input("Chack this number: "))
    prime_chaker(number = n)

# exercise 3
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  
def loop():
    len_alphabet = len(alphabet)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "encode" and direction != "decode":
        print("The entry is incorrect, try again")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  
    text = input("Type your message:\n").lower()
    for i in text:
        if i not in alphabet:
            alphabet.append(i) 
    shift = int(input("Type the shift number:\n"))
    def caesae(start_text, shift_amount, cipher_direction):
        if cipher_direction == "encode":
            enc = ""
            for n in text:
                start_text = alphabet.index(n)
                shift_amount = start_text - shift
                if shift_amount < 0:
                    shift_amount += shift
                    encry = alphabet[-shift_amount]
                else: 
                    encry = alphabet[shift_amount]
                enc += encry   
            print(f"Here is your encode result {enc}") 
        if cipher_direction == "decode":
            dec = ""
            for n in text:
                start_text= alphabet.index(n)
                shift_amount = start_text + shift
                if shift_amount > len_alphabet:
                    shift_amount -= shift
                    decry = alphabet[-shift_amount]
                else: 
                    decry = alphabet[shift_amount]
                dec += decry     
            print(f"Here is your decode result {dec}.")   
    caesae(start_text = text,shift_amount= shift,cipher_direction = direction)
    ask = input('type "yes", if you want to go again. Otherwise type "no".')
    lower_ask = ask.lower()
    if lower_ask == "no":
        print("Goodbye")
        exit()
    while lower_ask == "yes":
        loop()                     
loop()

    