import random
from Day_word_7 import word_list
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
#word_list = ["aardvark", "baboon", "camel"]
lives = 0
word = random.choice(word_list)
len_word = len(word)
list_ = []
fill_list = []
dis = []
for _ in range(len(word)):
    dis += "_"

for fill in word:
    if fill == fill:
         fill_list.append(fill)
    else:
         fill_list.append("_")
print(logo)
while dis != fill_list:
    Ask = input("guess a letter ").lower()
    for position in range(len(word)):
        letter = word[position]
        if Ask == letter:
            if Ask in dis:
              print(f"You've already gassed {Ask}")  
            dis[position] = letter
    if Ask not in dis:
      print(f"you gassed {Ask},That is not in the word. You lost a life")
    
    print(dis)
    if Ask not in dis:
        if lives < 6:
            lives = lives + 1
            man = stages[lives]
            print(man)
            if lives == 6:
                print("you lost")
                exit()    
    if Ask in dis:
      man = stages[lives]
      print(man)
print("you win!")


