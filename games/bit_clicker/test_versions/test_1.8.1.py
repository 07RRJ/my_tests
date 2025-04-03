import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # For displaying messages
import json  # For saving and loading data
import os   # Cleaner console

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

def upgrades_1_9(button_number):
    pass

upgrade_buttons = [
    (f"upgrade bits/click - {bits_pr_c_price}", 2, 0, 2), (f"buy auto - {auto_price}", 2, 2, 2), (f"upgrade auto - {auto_price}", 2, 4, 2), 
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
]

root = tk.Tk()
root.title("07RRJ's Clicker Game")
style = ttk.Style(root)
style.theme_use("xpnative")
width = 1000
height = 1200
root.geometry(f"{width}x{height}")
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var, font=("Helvetica", 24), justify="right")
result_entry.grid(row = 0, column = 0, columnspan = 10, sticky = "nsew")

label = ttk.Label(root, text = "Clicker Game", font=("Arial", 24))
label.grid(row=0, column=0, columnspan=6)
THE_button = ttk.Button(root, text = "Click Me!", command = on_button_click)
THE_button.grid(row=1, column=0, columnspan=6)



style.configure("TButton", font = ("Helvatica", 16), width = 10, height = 4)
for button_info in upgrade_buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text = button_text, command=lambda text = button_text: upgrades_1_9(text), style="TButton")
    button.grid(row = row, column = col, columnspan = colspan, sticky = "nsew", ipadx = 10, ipady = 4, padx = 5, pady = 5)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Save Game", command = save_game)
filemenu.add_command(label="Load Game", command = load_game)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)



load_game()
root.mainloop()