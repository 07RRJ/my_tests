import os
import threading
from time import sleep
import tkinter as tk
from tkinter import messagebox, ttk, Tk
import json

os.system("cls")

root = Tk()
root.title("07RRJ's Clicker Game")
style = ttk.Style(root)
style.theme_use("clam") #xpnative
width = 1000
height = 800
root.geometry(f"{width}x{height}")

# Make the window non-resizable
# root.resizable(False, False)

# Initialize multiple game_data for different button actions
game_data = {
    'bits': 0,
    'bits_click': 1,
    'bits_click_price': 50,
    'bits_second': 0,
    "bps_running": False,  # Flag to track if the thread is running
    'auto_cost': 500,
    'score': 100,
    'level': 1,
    'health': 50,
    'mana': 30,
    'experience': 0,
    'gold': 200,
    'gems': 10,
    'stamina': 75,
    'power': 5,
    'strength': 8,
    'agility': 12,
    'intelligence': 15,
    'defense': 10,
}

DEFAULT_GAME_DATA = game_data

def save_game():    # save game
    global game_data
    global game_save

    game_save = game_data

    folder_name = "C:\\MyClickerGame"  # Change this to your desired folder
    file_name = "game_save.json"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Full path to the save file
    file_path = os.path.join(folder_name, file_name)

    try:
        with open(file_path, "w") as f:
            json.dump(game_save, f, indent=4)
        messagebox.showinfo("Save Game", "Game saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save game: {e}")

def load_game():  # Load game with missing key handling
    global game_data
    global game_save

    folder_name = "C:\\MyClickerGame"
    file_name = "game_save.json"
    file_path = os.path.join(folder_name, file_name)

    try:
        with open(file_path, "r") as f:
            game_save = json.load(f)

        # Ensure all expected keys exist (fills missing ones with default values)
        for key, default_value in DEFAULT_GAME_DATA.items():
            game_save.setdefault(key, default_value)

        game_data = game_save  # Update global game_data first!

        # Now check if bps_running is True **after** updating game_data
        if game_data.get("bps_running"):  
            game_data["bps_running"] = True
            threading.Thread(target=bits_per_second, daemon=True).start()

        messagebox.showinfo("Load Game", "Game loaded successfully!")
        label.config(text=f"Your bits {game_data['bits']}")

        # Save updated file in case new defaults were added
        save_game()

    except FileNotFoundError:
        messagebox.showwarning("Load Game", "No save file found, starting a new game.")
        game_data = DEFAULT_GAME_DATA.copy()  # Use default values
        save_game()  # Save a new default file

    except Exception as e:
        messagebox.showerror("Error", f"Could not load game: {e}")

def on_button_click():  # on THE button click
    global game_data
    game_data['bits'] += 1 * int(game_data.get('bits_click', 1))
    label.config(text = f"Your bits {game_data['bits']}")

def bits_per_second():
    while True:
        sleep(1)
        game_data['bits'] += game_data['bits_second']
        label.config(text = f"Your bits {game_data['bits']}")

def rename(button, original_text):
    button.config(text="Not enough bits!", state="disabled")  # Disable & change color
    sleep(1)
    button.config(text=original_text, state="normal")  # Restore default color

while True:
    def action_1(button):
        if game_data['bits'] > game_data['bits_click_price']:
            game_data['bits'] -= game_data['bits_click_price']
            game_data['bits_click_price'] += int((game_data['bits_click_price']**0.5)*10)
            game_data['bits_click'] += 1
            button.config(text=f"bits/click - {game_data['bits_click_price']}")
            label.config(text = f"Your bits {game_data['bits']}")
        elif game_data['bits'] < game_data['bits_click_price']:
            original_text = button.cget("text")
            threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

    while True:
        def action_2(button):
            if game_data['bits'] >= game_data['auto_cost']:
                game_data['bits'] -= game_data['auto_cost']
                game_data['auto_cost'] += int((game_data['auto_cost']**0.4) * 10)
                game_data['bits_second'] += 1  # Increase bits per second

                button.config(text=f"bits/s - {game_data['auto_cost']}")
                label.config(text = f"Your bits {game_data['bits']}")

                # Start bits_per_second thread ONLY if it's not already running
                if not game_data["bps_running"]:
                    game_data["bps_running"] = True  # Set flag
                    threading.Thread(target=bits_per_second, daemon=True).start()
                elif game_data['bits'] < game_data['auto_cost']:
                    original_text = button.cget("text")
                    threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

        while True:
            def action_3(button):
                game_data['score'] += 10
                button.config(text=f" - {game_data['score']}")

            def action_4(button):
                game_data['level'] += 1
                button.config(text=f" - {game_data['level']}")

            def action_5(button):
                game_data['health'] += 5
                button.config(text=f" - {game_data['health']}")

            def action_6(button):
                game_data['mana'] += 3
                button.config(text=f" - {game_data['mana']}")

            def action_7(button):
                game_data['experience'] += 20
                button.config(text=f" - {game_data['experience']}")

            def action_8(button):
                game_data['gold'] += 50
                button.config(text=f" - {game_data['gold']}")

            def action_9(button):
                game_data['gems'] += 1
                button.config(text=f" - {game_data['gems']}")

            def action_10(button):
                game_data['stamina'] += 10
                button.config(text=f" - {game_data['stamina']}")

            def action_11(button):
                game_data['power'] += 2
                button.config(text=f" - {game_data['power']}")

            def action_12(button):
                game_data['strength'] += 1
                button.config(text=f" - {game_data['strength']}")

            def action_13(button):
                game_data['agility'] += 3
                button.config(text=f" - {game_data['agility']}")

            def action_14(button):
                game_data['intelligence'] += 2
                button.config(text=f" - {game_data['intelligence']}")

            def action_15(button):
                game_data['defense'] += 4
                button.config(text=f" - {game_data['defense']}")
            break
        break
    break

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

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Save Game", command = save_game)
filemenu.add_command(label="Load Game", command = load_game)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="Manage Save", menu=filemenu)
root.config(menu=menubar)

# Define the button texts, grid positions, and the associated action functions
buttons_info = [
    ("bits/click - {bits_click_price}", 2, 0, action_1, 'bits'),
    ("bits/s - {auto_cost}", 2, 1, action_2, 'auto_cost'),
    ("bits/click multiplier - {score}", 2, 2, action_3, 'score'),
    ("bits/s multiplier - {level}", 3, 0, action_4, 'level'),
    ("bits/click scaling - {health}", 3, 1, action_5, 'health'),
    ("bits/s scaling - {mana}", 3, 2, action_6, 'mana'),
    (" - {experience}", 4, 0, action_7, 'experience'),
    (" - {gold}", 4, 1, action_8, 'gold'),
    (" - {gems}", 4, 2, action_9, 'gems'),
    (" - {stamina}", 5, 0, action_10, 'stamina'),
    (" - {power}", 5, 1, action_11, 'power'),
    (" - {strength}", 5, 2, action_12, 'strength'),
    (" - {agility}", 6, 0, action_13, 'agility'),
    (" - {intelligence}", 6, 1, action_14, 'intelligence'),
    (" - {defense}", 6, 2, action_15, 'defense'),
]

buttons = []  # Store button instances

load_game()
# Create buttons dynamically
for button_text, row, col, action_function, variable in buttons_info:
    # Format the button text dynamically using the game_data dictionary
    formatted_text = button_text.format(**game_data)

    # Create button instance with the formatted text
    button = ttk.Button(root, text=formatted_text)

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

root.mainloop()