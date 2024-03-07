#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
in_names = open(r"\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-24\Mail Merge Project Start\Input\Names/invited_names.txt")
str_let = open(r"\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-24\Mail Merge Project Start\Input\Letters/starting_letter.txt")
for i in str_let:
    names = str(in_names)
    i.replace("name", names)
print(i)

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp