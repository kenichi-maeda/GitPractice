from tkinter import *


def press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("arithmetic error detected")
        equation_text = ""
    except SyntaxError:
        equation_label.set("syntax error detected")
        equation_text = ""
    


def allClear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Calculator")
window.geometry("500x600")
window.resizable(False, False)
window.config(background="black")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(1), bg="white")
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(2), bg="white")
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(3), bg="white")
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(4), bg="white")
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(5), bg="white")
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(6), bg="white")
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(7), bg="white")
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(8), bg="white")
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(9), bg="white")
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=("Comic Sans", 17),
                 command=lambda: press(0), bg="white")
button0.grid(row=3, column=0)

plus_button = Button(frame, text='+', height=4, width=9, font=("Comic Sans", 17),
                     command=lambda: press('+'), bg="white")
plus_button.grid(row=0, column=3)

minus_button = Button(frame, text='-', height=4, width=9, font=("Comic Sans", 17),
                      command=lambda: press('-'), bg="white")
minus_button.grid(row=1, column=3)

mul_button = Button(frame, text='*', height=4, width=9, font=("Comic Sans", 17),
                    command=lambda: press('*'), bg="white")
mul_button.grid(row=2, column=3)

div_button = Button(frame, text='/', height=4, width=9, font=("Comic Sans", 17),
                    command=lambda: press('/'), bg="white")
div_button.grid(row=3, column=2)

decimal_button = Button(frame, text='.', height=4, width=9, font=("Comic Sans", 17),
                        command=lambda: press('.'), bg="white")
decimal_button.grid(row=3, column=1)

equal_button = Button(frame, text='=', height=4, width=9, font=("Comic Sans", 17),
                      command=lambda: equals(), bg="#f5c15b")
equal_button.grid(row=3, column=3)

clear_button = Button(window, text='AC', height=3, width=12, font=("Comic Sans", 17),
                      command=lambda: allClear(), bg="#5bb2f5")
clear_button.pack()

window.mainloop()
