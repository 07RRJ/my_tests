from tkinter import Tk, ttk
import tkinter as tk
from tkinter import messagebox  # For displaying messages
import json  # For saving and loading data
import os   # Cleaner console
from time import sleep
import threading
import json

os.system("cls")

# game variables
bits = 0
bits_pr_c = 1
bits_pr_c_price = 10
auto_price = 500
better_auto = 1

game_data = {"bits": bits, "bits_pr_c": bits_pr_c}



def save_game():    # save game
    global bits
    global bits_pr_c

    game_data = {"bits": bits, "bits_pr_c": bits_pr_c}  # Replace with your game's data

    folder_name = "C:\\MyClickerGame"  # Change this to your desired folder
    file_name = "game_save.json"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Full path to the save file
    file_path = os.path.join(folder_name, file_name)

    try:
        with open(file_path, "w") as f:
            json.dump(game_data, f, indent=4)
        messagebox.showinfo("Save Game", "Game saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save game: {e}")

def load_game():    # load game
    global bits
    global bits_pr_c

    folder_name = "C:\\MyClickerGame"  # Change this to your desired folder
    file_name = "game_save.json"
    file_path = os.path.join(folder_name, file_name)

    try:
        with open(file_path, "r") as f:
            game_data = json.load(f)
        # Update your game variables with the loaded data
        bits = game_data["bits"]
        bits_pr_c = game_data["bits_pr_c"]
        # ... other game variables ...
        messagebox.showinfo("Load Game", "Game loaded successfully!")
        label.config(text = f"Your bits {bits}")
    except FileNotFoundError:
        messagebox.showwarning("Load Game", "No save file found.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load game: {e}")

def on_button_click():  # on THE button click
    global bits
    bits += bits_pr_c
    label.config(text = f"Your bits {bits}")

button_states = {}

button_states = {}



# Function to handle button click (without tracking the state)
def handle_button_click(button):
    current_text = button.cget('text')  # Get the current text of the button
    new_text = f"{current_text} - Clicked"  # Append '- Clicked' to the current text
    button.config(text=new_text)  # Update the button text
    print(f"Updated text: {new_text}")

def action_1(button):
    global bits
    bits += 1
    print("Performing custom action for Button 1...")

def action_2(button):
    print("Performing custom action for Button 2...")

def action_3(button):
    print("Performing custom action for Button 3...")

def action_4(button):
    print("Performing custom action for Button 4...")

def action_5(button):
    print("Performing custom action for Button 5...")

def action_6(button):
    print("Performing custom action for Button 6...")
    
def action_7(button):
    print("Performing custom action for Button 7...")

def action_8(button):
    print("Performing custom action for Button 8...")

def action_9(button):
    print("Performing custom action for Button 9...")

def action_10(button):
    print("Performing custom action for Button 10...")

def action_11(button):
    print("Performing custom action for Button 11...")

def action_12(button):
    print("Performing custom action for Button 12...")

def action_13(button):
    print("Performing custom action for Button 13...")

def action_14(button):
    print("Performing custom action for Button 14...")

def action_15(button):
    print("Performing custom action for Button 15...")

buttons_info = [
    ("bits/click - 10", 2, 0, action_1),
    ("auto - 20", 2, 1, action_2),
    ("upgrade auto - 30", 2, 2, action_3),
    ("7", 3, 0, action_4),
    ("8", 3, 1, action_5),
    ("9", 3, 2, action_6),
    ("4", 4, 0, action_7),
    ("5", 4, 1, action_8),
    ("6", 4, 2, action_9),
    ("1", 5, 0, action_10),
    ("2", 5, 1, action_11),
    ("3", 5, 2, action_12),
    ("0", 6, 0, action_13),
    (".", 6, 1, action_14),
    ("=", 6, 2, action_15),
]

buttons = []  # Store button instances

root = Tk()

root.title("07RRJ's Clicker Game")
style = ttk.Style(root)
style.theme_use("xpnative")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Save Game", command = save_game)
filemenu.add_command(label="Load Game", command = load_game)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="Manage Save", menu=filemenu)
root.config(menu=menubar)

label = ttk.Label(root, text = "Clicker Game", font=("Arial", 32))
label.grid(row=0, column=0, columnspan = 3)

style.configure("TButton", font=("Arial", 16))  # Set the font for the button style

# Create a button with the defined style
THE_button = ttk.Button(root, text="Click Me", command=on_button_click, style="TButton")
THE_button.grid(
    row = 1,
    column = 0,
    columnspan = 3,
    sticky="nsew",
    ipadx=10,  # Increase internal padding for larger buttons
    ipady=4,   # Increase internal padding for larger buttons
    padx=5,    # Adjust external padding as needed
    pady=5,    # Adjust external padding as needed
)

buttons = []  # Store button instances

# Create buttons dynamically
for button_text, row, col, action_function in buttons_info:
    # Create button instance
    button = ttk.Button(root, text=button_text.format(bits=bits))  # Format the initial text with bits value
    
    # Assign the action function for the button
    button.config(command=lambda b=button, act=action_function: act(b))

    # Place the button in the grid
    button.grid(
        row=row,
        column=col,
        sticky="nsew",
        ipadx=10,  # Internal padding for larger buttons
        ipady=4,
        padx=5,  # External padding
        pady=5
    )
    
    buttons.append(button)  # Store the button instance

# Configure rows and columns to be expandable
for i in range(7):
    root.grid_rowconfigure(i, weight=1)  # Allow rows to expand
for i in range(3):
    root.grid_columnconfigure(i, weight=1)  # Allow columns to expand

width = 1000
height = 800
root.geometry(f"{width}x{height}")

# Make the window non-resizable
root.resizable(False, False)

load_game()
root.mainloop()