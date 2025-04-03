import tkinter as tk
from tkinter import ttk
from tkinter import Button

def button_clicked_1_9(button_number):
    if button_number == 1:
        print("You clicked button 1!")
    elif button_number == 2:
        print("You clicked button 2!")
    elif button_number == 3:
        print("You clicked button 3!")
    else:
        print(f"You clicked button {button_number}.")

# Create the main window
root = tk.Tk()
root.title("Button Grid")

# Create the label
label = ttk.Label(root, text="My Button Grid", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=3)

# Create the buttons in a 3x3 grid
for i in range(3):
    for j in range(3):
        button_number = i * 3 + j + 1
        button = ttk.Button(root, text=f"Button {button_number}", command=lambda num=button_number: button_clicked_1_9(num))
        button.grid(row=i + 1, column=j)


# Create a button
button1 = Button(root, text="Click Me", width=20, height=2)
button1.grid(row=5, column=0, sticky='nsew')

# Configure row and column to be expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
