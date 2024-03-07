import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    lable_timer.config(text = "Timer", bg=YELLOW)
    chexk_mark.config(text="")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global  reps
    work_sec = WORK_MIN * 60
    short_brake = SHORT_BREAK_MIN * 60
    long_brake = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        lable_timer.config(text="Work", fg=RED,bg =YELLOW)
        count_down(work_sec)
        reps += 1

    elif reps == 2 or reps == 4 or reps == 6:
        lable_timer.config(text="Brake", fg=GREEN,bg =YELLOW)
        count_down(short_brake)
        reps += 1
    elif reps == 8:
        lable_timer.config(text="Long Brake", fg=GREEN ,bg =YELLOW)
        count_down(long_brake)
        reps -= 7




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global text
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        st = "0" + str(count_sec)
        count_sec = st
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count != 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    elif reps == 2 or reps == 4 or reps == 6 or reps == 8:
        text += "✓"
        chexk_mark.config(text=text)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
#window.geometry("800x600")
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("600x500")
window.columnconfigure((0, 1, 2), weight =1)
window.rowconfigure((0, 1, 2), weight =1)



lable_timer = tk.Label(font=(FONT_NAME, 50), fg=GREEN)
lable_timer.config(text = "Timer", bg=YELLOW)
lable_timer.grid(row = 0, column =1, sticky = "s")

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file = r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-28\tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="0", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row = 1, column =1, sticky = "n")

button = tk.Button(width=5, text="Start", command=start_time)
button.grid(row = 2, column =0, sticky = "ne")

button1 = tk.Button(width=5, text="Reset", command=reset_timer)
button1.grid(row = 2, column =2, sticky = "n")

chexk_mark = tk.Label(fg = GREEN, bg=YELLOW, font=(FONT_NAME, 15))
chexk_mark.grid(row = 2, column =1, sticky = "we")


window.mainloop()

