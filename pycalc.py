import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("PyCalc")
root.geometry("400x500")
root.configure(padx=10, pady=10)

entry = ctk.CTkEntry(root, width=370, height=40, font=("Helvetica", 18), corner_radius=10)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, ctk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, ctk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, ctk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, ctk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, ctk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, ctk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, ctk.END)
    
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
    button = ctk.CTkButton(root, text=str(i), width=80, height=60, font=("Helvetica", 18), command=lambda i=i: button_click(i), corner_radius=10)
    buttons.append(button)

buttons[1].grid(row=3, column=0, padx=5, pady=5)
buttons[2].grid(row=3, column=1, padx=5, pady=5)
buttons[3].grid(row=3, column=2, padx=5, pady=5)

buttons[4].grid(row=2, column=0, padx=5, pady=5)
buttons[5].grid(row=2, column=1, padx=5, pady=5)
buttons[6].grid(row=2, column=2, padx=5, pady=5)

buttons[7].grid(row=1, column=0, padx=5, pady=5)
buttons[8].grid(row=1, column=1, padx=5, pady=5)
buttons[9].grid(row=1, column=2, padx=5, pady=5)

buttons[0].grid(row=4, column=1, padx=5, pady=5)

button_clear = ctk.CTkButton(root, text="Clear", width=170, height=60, font=("Helvetica", 18), command=button_clear, corner_radius=10)
button_decimal = ctk.CTkButton(root, text=".", width=80, height=60, font=("Helvetica", 18), command=lambda: button_click('.'), corner_radius=10)
button_equal = ctk.CTkButton(root, text="=", width=350, height=60, font=("Helvetica", 18), command=button_equal, corner_radius=10)

button_add = ctk.CTkButton(root, text="+", width=80, height=60, font=("Helvetica", 18), command=button_add, corner_radius=10)
button_subtract = ctk.CTkButton(root, text="-", width=80, height=60, font=("Helvetica", 18), command=button_subtract, corner_radius=10)
button_multiply = ctk.CTkButton(root, text="*", width=80, height=60, font=("Helvetica", 18), command=button_multiply, corner_radius=10)
button_divide = ctk.CTkButton(root, text="/", width=80, height=60, font=("Helvetica", 18), command=button_divide, corner_radius=10)

button_clear.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
button_decimal.grid(row=4, column=0, padx=5, pady=5)
button_equal.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()
