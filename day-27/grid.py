import tkinter
window = tkinter.Tk()
window.title("Grid")
window.geometry("600x400")

label1 = tkinter.Label(text="lable1", background=("blue"))
label2 = tkinter.Label(text="lable2", background=("black"))
label3 = tkinter.Label(text="lable4", background=("red"))
button1 = tkinter.Button(text="bouuton1")
button2 = tkinter.Button(text="bouuton2")
button3 = tkinter.Button(text="bouuton3")

window.columnconfigure((0,1,2,3), weight= 1)
window.rowconfigure(0, weight= 1)

label1.grid(row= 0, column= 2, sticky = "ew")
label2.grid(row= 0, column= 3,  sticky = "ew")



window.mainloop()