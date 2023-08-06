from tkinter import *

root = Tk()
root.geometry("304x460")
root.minsize(304, 460)
root.maxsize(304, 460)
root.iconbitmap("Calculator.ico")
root.title("Calculator")
eq = ""


def click(event):
    global eq
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(exp.get())
        except:
            value = "error"
        exp.set(value)
        ex.update()
    elif text == "C":
        exp.set("")
        ex.update()
    else:
        exp.set(exp.get() + str(text))
        ex.update()


exp = StringVar()
exp.set("")
ex = Entry(root, textvariable=exp, font="Rubik 20 bold", justify=RIGHT, highlightthickness=1)
ex.grid(row=0, column=0, ipady=17)
ex.config(highlightbackground="black", highlightcolor="black")
frame1 = Frame(root, borderwidth=6, bg="grey")
frame1.grid(row=2, padx=12)
buttons = []
for i in range(3):
    for n in range(3):
        buttons.append(Button(frame1, fg="black", text=n + 1 + 3 * i, font="Rubik 15 bold"))
        buttons[-1].grid(ipadx=13, ipady=10, padx=5, pady=5, row=i, column=n + 1)
        buttons[-1].bind("<Button-1>", click)
x = []
x.append(Button(frame1, fg="black", text="C", font="Rubik 15 bold"))
x[-1].grid(ipadx=13, ipady=10, padx=5, pady=5, row=0, column=4)
x.append(Button(frame1, fg="black", text="+", font="Rubik 15 bold"))
x[-1].grid(ipadx=14, ipady=10, padx=5, pady=5, row=1, column=4)
x.append(Button(frame1, fg="black", text="-", font="Rubik 15 bold"))
x[-1].grid(ipadx=16, ipady=10, padx=5, pady=5, row=2, column=4)
x.append(Button(frame1, fg="black", text="/", font="Rubik 15 bold"))
x[-1].grid(ipadx=16, ipady=10, padx=5, pady=5, row=3, column=4)
x.append(Button(frame1, fg="black", text="*", font="Rubik 15 bold"))
x[-1].grid(ipadx=14, ipady=10, padx=5, pady=5, row=3, column=3)
x.append(Button(frame1, fg="black", text=0, font="Rubik 15 bold"))
x[-1].grid(ipadx=13, ipady=10, padx=5, pady=5, row=3, column=1)
x.append(Button(frame1, fg="black", text=".", font="Rubik 15 bold"))
x[-1].grid(ipadx=15, ipady=10, padx=5, pady=5, row=4, column=1)
x.append(Button(frame1, fg="black", text="%", font="Rubik 15 bold"))
x[-1].grid(ipadx=10, ipady=10, padx=5, pady=5, row=3, column=2)
x.append(Button(frame1, fg="black", text="=", font="Rubik 15 bold"))
x[-1].grid(ipadx=80, ipady=10, padx=5, pady=5, row=4, column=2, columnspan=3)
for i in x:
    i.bind("<Button-1>", click)
root.mainloop()
