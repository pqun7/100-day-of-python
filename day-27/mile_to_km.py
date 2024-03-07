import tkinter
window = tkinter.Tk()
#window.geometry("240x200")
def botton():
    mile = entry_m.get()
    int_mile = int(mile)
    r = round(int_mile * 1.60934)
    label_km.config(text=r)


label_m = tkinter.Label(text="Miles", font=("Arial", 10))
entry_m = tkinter.Entry(width=14)

km = tkinter.Label(text="Km", font=("Arial", 10))
label_km = tkinter.Label(text="0", font=("Arial", 12))

calculate = tkinter.Button(text="Calculate", command=botton)
label_text = tkinter.Label(text="is equal to", font=("Arial", 10))


window.columnconfigure((0, 1, 2, 3), weight =1)
window.rowconfigure((0, 1, 2, 3, 4), weight =1)
label_m.grid(row = 1, column = 2, sticky = "w")
entry_m.grid(row = 1, column = 1, sticky = "e")
km.grid(row = 2, column = 2, sticky = "wn")
label_km.grid(row = 2, column = 1, sticky = "wen")
label_text.grid(row = 2, column = 0, sticky = "ne")
calculate.grid(row = 3, column = 1, sticky = "wen")





window.mainloop()
