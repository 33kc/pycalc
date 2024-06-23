from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PyCalc")
root.configure(bg="#2f3640")

entry = Entry(root, width=35, borderwidth=5, font=("Helvetica", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        if float(second_number) != 0:
            entry.insert(0, f_num / float(second_number))
        else:
            entry.insert(0, "Error")


buttons = []
for i in range(10):
    button = Button(root, text=str(i), padx=35, pady=20, font=("Helvetica", 18), command=lambda i=i: button_click(i), bg="#57606f", fg="white", activebackground="#8395a7", activeforeground="white", borderwidth=0)
    buttons.append(button)


buttons[1].grid(row=3, column=0)
buttons[2].grid(row=3, column=1)
buttons[3].grid(row=3, column=2)

buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)

buttons[7].grid(row=1, column=0)
buttons[8].grid(row=1, column=1)
buttons[9].grid(row=1, column=2)

buttons[0].grid(row=4, column=0)

button_clear = Button(root, text="Clear", padx=70, pady=20, font=("Helvetica", 18), command=button_clear, bg="#c0392b", fg="white", activebackground="#e74c3c", activeforeground="white", borderwidth=0)
button_decimal = Button(root, text=".", padx=39, pady=20, font=("Helvetica", 18), command=lambda: button_click('.'), bg="#57606f", fg="white", activebackground="#8395a7", activeforeground="white", borderwidth=0)
button_equal = Button(root, text="=", padx=85, pady=20, font=("Helvetica", 18), command=button_equal, bg="#27ae60", fg="white", activebackground="#2ecc71", activeforeground="white", borderwidth=0)

button_add = Button(root, text="+", padx=38, pady=20, font=("Helvetica", 18), command=button_add, bg="#57606f", fg="white", activebackground="#8395a7", activeforeground="white", borderwidth=0)
button_subtract = Button(root, text="-", padx=40, pady=20, font=("Helvetica", 18), command=button_subtract, bg="#57606f", fg="white", activebackground="#8395a7", activeforeground="white", borderwidth=0)
button_multiply = Button(root, text="*", padx=39, pady=20, font=("Helvetica", 18), command=button_multiply, bg="#57606f", fg="white", activebackground="#8395a7", activeforeground="white", borderwidth=0)
button_divide = Button(root, text="/", padx=40, pady=20, font=("Helvetica", 18), command=button_divide, bg="#57606f", fg="white", activebackground="#8395a7", activeforeground="white", borderwidth=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_decimal.grid(row=4, column=3)
button_equal.grid(row=5, column=0, columnspan=4)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=0)

root.mainloop()
