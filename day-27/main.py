from tkinter import *

def action():
    new_text = entry.get()
    label.config(text=new_text)

#Creating a new widow and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text", font=(45))
#label.pack()
#label.place(x=100 , y=100)
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

#Buttons
buttons = Button(text="Click Me", command=action)
#buttons.pack()
buttons.grid(column=2, row=2)

buttons1 = Button(text="New button", command=action)
buttons1.grid(column=3, row=1)

#Entries
entry = Entry(width=30)
print(entry.get())
#entry.pack()
entry.grid(column=4, row=4)



window.mainloop()
