from customtkinter import CTk, CTkCanvas, CTkImage, CTkButton
from PIL import Image, ImageTk
import pandas
import random

BACKGROUND_COLOR = '#B1DDC6'

app = CTk()
app.title("Flashy")
app.config(background=BACKGROUND_COLOR, padx=50, pady=50)

data = pandas.read_csv(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-31\data\french_words.csv")
to_learn = data.to_dict(orient="records")

do_random = True

def word(language, card):
    global french_word, random_word, current_card
    if do_random:
        random_word = random.choice(to_learn)
    current_card = random_word[language]
    canvas.create_image(400, 252, image=card)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=1, padx=10, pady=10)
    canvas.create_text(400, 150, text=language, font=("Arial", 20, "bold"))
    french_word = canvas.create_text(400, 252, text=current_card, font=("Arial", 40, "bold"))
def flip():
    global do_random
    canvas.delete("all")
    do_random = False
    word("English", card_back_tk)

def update_word():
    global data, french_word, do_random, flip_timer
    app.after_cancel(flip_timer)
    canvas.delete(french_word)
    do_random = True
    word("French", card_front_tk)

    flip_timer = app.after(3000, func=flip)


flip_timer = app.after(3000, func=flip)

def delete_word():
    global current_card
    print(current_card)
    to_learn.remove(current_card)
    update_word()
#-----------------------------------------GUI-------------------------------------------------------------#
card_front = Image.open(
        r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-31\images\card_front.png")
card_back = Image.open(
    r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-31\images\card_back.png")

card_front_tk = ImageTk.PhotoImage(card_front)
card_back_tk = ImageTk.PhotoImage(card_back)

canvas = CTkCanvas(app, width=800, height=524)
word("French", card_front_tk)

right = Image.open(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-31\images\right.png")
right_tk = CTkImage(right, size=(100, 100))
button_right = CTkButton(master=app , hover_color=BACKGROUND_COLOR ,fg_color=BACKGROUND_COLOR ,
                         image=right_tk, command=delete_word)
button_right.grid(row=1, column= 0, sticky = "w")

wrong = Image.open(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-31\images\wrong.png")
wrong_tk = CTkImage(wrong, size=(100, 100))
button_wrong = CTkButton(master=app , hover_color=BACKGROUND_COLOR ,fg_color=BACKGROUND_COLOR ,
                         image=wrong_tk, command=update_word)
button_wrong.grid(row=1, column=2, sticky = "e")

app.mainloop()
