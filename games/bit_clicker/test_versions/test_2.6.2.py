import os
import threading
from time import sleep
from suffixes import millify
import tkinter as tk
from tkinter import messagebox, ttk, Tk
import json

os.system("cls")

root = Tk()
root.title("07RRJ's Clicker Game")
style = ttk.Style(root)
style.theme_use("clam") #xpnative
# root.configure(bg="red")
# entry = tk.Entry(root, bg="gray", fg="black", insertbackground="red")
# width = 1000
# height = 800
# root.geometry(f"{width}x{height}")
root.minsize(700, 700)

game_data = {
    'bits': 0,
    'total_bits_click': 1,
    'total_bits_second': 0,
    'bits_click': 1,
    'bits_click_price': 50,
    'bits_second': 0,
    'auto_cost': 250,
    "bps_running": False,  # Flag to track if the thread is running
    'bits_click_multiplier': 1,
    'bits_click_multiplier_price': 2500,
    'bits_second_multiplier': 1,
    'bits_second_multiplier_price': 5000,
    'experience': 10000,
    'gold': 20000,
    'gems': 1000000,
    'stamina': 75000000,
    'power': 500000000,
    'strength': 800000000000,
    'agility': 1200000000000000,
    'intelligence': 15000000000000000,
    'defense': 100000000000000000,
    'bits_click_scaling': 0,
    'bits_click_scaling_price': 50000,
    'bits_second_scaling': 0,
    'bits_second_scaling_price': 75000,
}

DEFAULT_GAME_DATA = game_data

def save_game(quit_after_save=False, show_popup=True):
    global game_data
    global game_save

    game_save = game_data.copy()  # Save the current game data

    folder_name = "C:\\MyClickerGame"
    file_name = "game_save.json"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, file_name)

    try:
        with open(file_path, "w") as f:
            json.dump(game_save, f, indent=4)

        if show_popup:
            messagebox.showinfo("Save Game", "Game saved successfully!")

        if quit_after_save:
            root.quit()  # Quit after saving if flag is true

    except Exception as e:
        messagebox.showerror("Error", f"Could not save game: {e}")

def load_game(is_popup_enabled=True):  # Use the new flag for popup control
    global game_data

    folder_name = "C:\\MyClickerGame"
    file_name = "game_save.json"
    file_path = os.path.join(folder_name, file_name)

    try:
        with open(file_path, "r") as f:
            game_save = json.load(f)

        # Ensure all expected keys exist (filling missing ones with defaults)
        for key, default_value in DEFAULT_GAME_DATA.items():
            game_save.setdefault(key, default_value)

        game_data = game_save  # Update game_data with loaded values

        if is_popup_enabled:  # Only show popup if flag is True
            show_popup("Load Game", "Game loaded successfully!")  # Show success message

        # Now update the buttons and UI after loading game data
        root.after(100, update_ui_buttons)  # Custom function to update buttons based on loaded data
        update_label()

        # Start the bps thread only if it's not already running
        if game_data.get("bps_running", False):  
            threading.Thread(target=bits_per_second, daemon=True).start()

        # Save updated data (if new default values were added)
        save_game(show_popup=False)  # Save silently (no popup)

    except FileNotFoundError:
        game_data = DEFAULT_GAME_DATA.copy()  # Start fresh if no save file exists
        save_game(show_popup=False)  # Save silently

        if is_popup_enabled:  # Only show popup if flag is True
            show_popup("Load Game", "No save file found, starting a new game.")  # Show warning message

    except Exception as e:
        if is_popup_enabled:  # Only show popup if flag is True
            show_popup("Error", f"Could not load game: {e}")  # Show error message

def save_and_quit():
    save_game(quit_after_save=True, show_popup=False)  # Save game without changing bps_running
    root.quit()  # Quit the application after saving

def show_popup(title, message):
    messagebox.showinfo(title, message)  # Show the pop-up with the title and message
def update_ui_buttons():
    # Update the labels on the buttons with the loaded game data
    for button, (button_text, row, col, action_function, variable) in zip(buttons, buttons_info):
        formatted_text = button_text.format(**game_data)
        button.config(text=formatted_text)  # Update button text dynamically
        button.grid(row=row, column=col)  # Make sure it's placed in the correct position

def rename(button, original_text):
    button.config(text="Not enough bits!", state="disabled")  # Disable & change color
    sleep(1)
    button.config(text=original_text, state="normal")  # Restore default color

def update_label():
    if root.winfo_exists():  # Check if root is still alive
        millify_formatted = millify(game_data['bits'], precision=2)
        label.config(text=f"Your bits {millify(game_data['bits'], precision=2)}")
        game_data['total_bits_second'] = int(int(game_data['bits_second']) * int(game_data['bits_second_multiplier']) * int(((len(str(game_data['bits']))**0.3)**(game_data['bits_second_scaling']))))
        game_data['total_bits_click'] = int(int(game_data.get('bits_click')) * int(game_data.get('bits_click_multiplier')) * int(((len(str(game_data['total_bits_second'])))**0.8)**game_data['bits_click_scaling']/5))

        info_stats.config(text=f"bits/click - {int(game_data['total_bits_click'])} ({int(game_data['bits_click'])} * {int(game_data['bits_click_multiplier'])} * {int(((game_data['bits_second'] * game_data['bits_second_multiplier'])**0.015)**game_data['bits_click_scaling'])})\nbits/s - {int(game_data['total_bits_second'])} ({int(game_data['bits_second'])} * {int(game_data['bits_second_multiplier'])} * {int(((len(str(game_data['bits']))**0.3)**(game_data['bits_second_scaling'])))})")

def on_THE_button_click():  # on THE button click
    global game_data
    game_data['total_bits_second'] = int(int(game_data['bits_second']) * int(game_data['bits_second_multiplier']) * int(((len(str(game_data['bits']))**0.8)**(game_data['bits_second_scaling']/5))))
    game_data['total_bits_click'] = int(int(game_data.get('bits_click')) * int(game_data.get('bits_click_multiplier')) * int(((game_data['total_bits_second'])**0.015)**game_data['bits_click_scaling']))
    game_data['bits'] += game_data['total_bits_click']
    root.after(0, update_label)

def bits_per_second():
    while game_data.get("bps_running", False):
        game_data['total_bits_second'] = int(game_data['bits_second'] * game_data['bits_second_multiplier'] * ((len(str(game_data['bits']))**0.3)**(game_data['bits_second_scaling'])))

        if game_data['total_bits_second'] >= 10:
            sleep(0.1)
            game_data['bits'] += int(game_data['total_bits_second'] / 10)
        
        else:
            sleep(1)

        if root.winfo_exists():  # Only update if the window is still open
            root.after(0, update_label)
        else:
            break  # Exit loop if root is closed

def action_1(button):
    print(button)
    if game_data['bits'] >= game_data['bits_click_price']:
        game_data['bits'] -= game_data['bits_click_price']
        game_data['bits_click_price'] += int((game_data['bits_click_price']**0.5)*10)
        game_data['bits_click'] += 1
        button.config(text=f"bits/click - {millify(game_data['bits_click_price'], precision=2)}")
        root.after(0, update_label)
    elif game_data['bits'] < game_data['bits_click_price']:
        original_text = button.cget("text")
        threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

def action_2(button):
    if game_data['bits'] >= game_data['auto_cost']:
        game_data['bits'] -= game_data['auto_cost']
        game_data['auto_cost'] += int((game_data['auto_cost'] ** 0.5) * 10)
        game_data['bits_second'] += 1  # Increase bits per second

        button.config(text=f"bits/s - {millify(game_data['auto_cost'], precision=2)}")
        root.after(0, update_label)

        # Restart bits_per_second thread if not running
        if not game_data.get("bps_running", False):  
            game_data["bps_running"] = True
            threading.Thread(target=bits_per_second, daemon=True).start()

    else:
        original_text = button.cget("text")
        threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

def action_3(button):
    if game_data['bits'] >= game_data['bits_click_multiplier_price']:
        game_data['bits'] -= game_data['bits_click_multiplier_price']
        game_data['bits_click_multiplier_price'] += int((game_data['bits_click_multiplier_price'] ** 0.5) * 50)
        game_data['bits_click_multiplier'] += 1
        button.config(text=f"bits/click multiplier - {millify(game_data['bits_click_multiplier_price'], precision=2)}")
        root.after(0, update_label)
    
    else:
        original_text = button.cget("text")
        threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

def action_4(button):
    if game_data['bits'] >= game_data['bits_second_multiplier_price']:
        game_data['bits'] -= game_data['bits_second_multiplier_price']
        game_data['bits_second_multiplier_price'] += int((game_data['bits_second_multiplier_price'] ** 0.5) * 60)
        game_data['bits_second_multiplier'] += 1
        button.config(text=f"bits/s multiplier - {millify(game_data['bits_second_multiplier_price'], precision=2)}")
        root.after(0, update_label)
    
    else:
        original_text = button.cget("text")
        threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

def action_5(button):
    game_data['intelligence'] += 2
    button.config(text=f" - {millify(game_data['intelligence'], precision=2)}")

def action_6(button):
    game_data['defense'] += 4
    button.config(text=f" - {millify(game_data['defense'], precision=2)}")

def action_7(button):
    game_data['experience'] += 20
    button.config(text=f" - {millify(game_data['experience'], precision=2)}")
def action_8(button):
    game_data['gold'] += 50
    button.config(text=f" - {millify(game_data['gold'], precision=2)}")

def action_9(button):
    game_data['gems'] += 1
    button.config(text=f" - {millify(game_data['gems'], precision=2)}")

def action_10(button):
    game_data['stamina'] += 10
    button.config(text=f" - {millify(game_data['stamina'], precision=2)}")

def action_11(button):
    game_data['power'] += 2
    button.config(text=f" - {millify(game_data['power'], precision=2)}")

def action_12(button):
    game_data['strength'] += 1
    button.config(text=f" - {millify(game_data['strength'], precision=2)}")

def action_13(button):
    game_data['agility'] += 3
    button.config(text=f" - {millify(game_data['agility'], precision=2)}")

def action_14(button):
    if game_data['bits'] > game_data['bits_click_scaling_price']:
        game_data['bits'] -= game_data['bits_click_scaling_price']
        game_data['bits_click_scaling'] += 1
        game_data['bits_click_scaling_price'] += int((game_data['bits_click_scaling_price'] ** 0.5) * 500)
        button.config(text=f"bits/click scaling - {millify(game_data['bits_click_scaling_price'], precision=2)}")
        root.after(0, update_label)

    else:
        original_text = button.cget("text")
        threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

def action_15(button):
    if game_data['bits'] > game_data['bits_second_scaling_price']:
        game_data['bits'] -= game_data['bits_second_scaling_price']
        game_data['bits_second_scaling'] += 1
        game_data['bits_second_scaling_price'] += int(game_data['bits_second_scaling_price'] * 2.7)
        button.config(text=f"bits/s scaling - {millify(game_data['bits_second_scaling_price'], precision=2)}")
        root.after(0, update_label)


    else:
        original_text = button.cget("text")
        threading.Thread(target=rename, args=(button, original_text), daemon=True).start()

label = ttk.Label(root, text = "Clicker Game", font=("Arial", 32))
label.grid(row=0, column=0, columnspan = 3)

info_stats = ttk.Label(root, text = f"bits/click - {millify(game_data['bits'], precision=2)}\nbits/s - {game_data['bits_second']}", anchor="ne", justify="right")
info_stats.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

# Configure the grid to expand and fill the space
root.grid_columnconfigure(1, weight=1)  # Allow the second column to expand

style.configure("TButton", font=("Arial", 16))  # Set the font for the button style

# Create a button with the defined style
THE_button = ttk.Button(root, text="Click Me", command=on_THE_button_click, style="TButton")
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

# Custom Menu Bar (Non-Stretching)
menu_frame = tk.Frame(root, bg="lightgray", relief="raised", bd=2)
menu_frame.place(x=0, y=0)  # Place it at the top-left corner

# Add Buttons to Menu
save_button = tk.Button(menu_frame, text="Save Game", command=save_game)
save_button.pack(side="left", padx=5, pady=2)

load_button = tk.Button(menu_frame, text="Load Game", command=load_game)
load_button.pack(side="left", padx=5, pady=2)

save_quit_button = tk.Button(menu_frame, text="Save & Quit", command=save_and_quit)
save_quit_button.pack(side="left", padx=5, pady=2)

quit_button = tk.Button(menu_frame, text="Quit", command=root.quit)
quit_button.pack(side="left", padx=5, pady=2)

# Define the button texts, grid positions, and the associated action functions
buttons_info = [
    (f"bits/click - {game_data['bits_click_price']}", 2, 0, action_1, 'bits'),
    (f"bits/s - {millify(game_data['auto_cost'], precision=2)}", 2, 1, action_2, 'auto_cost'),
    (f"bits/click multiplier - {millify(game_data['bits_click_multiplier_price'], precision=2)}", 2, 2, action_3, 'bits_click_multiplier_price'),
    (f"bits/s multiplier - {millify(game_data['bits_second_multiplier_price'], precision=2)}", 3, 0, action_4, 'bits_second_multiplier_price'),
    (f" - {millify(game_data['intelligence'], precision=2)}", 3, 1, action_5, 'intelligence'),
    (f" - {millify(game_data['defense'], precision = 2)}", 3, 2, action_6, 'defense'),
    (f" - {millify(game_data['experience'], precision = 2)}", 4, 0, action_7, 'experience'),
    (f" - {millify(game_data['gold'], precision = 2)}", 4, 1, action_8, 'gold'),
    (f" - {millify(game_data['gems'], precision = 2)}", 4, 2, action_9, 'gems'),
    (f" - {millify(game_data['stamina'], precision = 2)}", 5, 0, action_10, 'stamina'),
    (f" - {millify(game_data['power'], precision = 2)}", 5, 1, action_11, 'power'),
    (f" - {millify(game_data['strength'], precision = 2)}", 5, 2, action_12, 'strength'),
    (f" - {millify(game_data['agility'], precision = 2)}", 6, 0, action_13, 'agility'),
    (f"bits/click scaling - {millify(game_data['bits_click_scaling_price'], precision=2)}", 6, 1, action_14, 'bits_click_scaling_price'),
    (f"bits/s scaling - {millify(game_data['bits_second_scaling_price'], precision=2)}", 6, 2, action_15, 'bits_second_scaling_price'),
]

buttons = []  # Store button instances

for i in range(7):
    root.grid_rowconfigure(i, weight=1, uniform="equal")  # Add uniformity to rows

for i in range(3):
    root.grid_columnconfigure(i, weight=1, uniform="equal")  # Add uniformity to columns

# Dynamically create buttons
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
        sticky="nsew",  # This will make the button expand in all directions (north, south, east, west)
        ipadx=10,       # Internal padding for larger buttons
        ipady=4,        # Internal padding for larger buttons
        padx=5,         # External padding
        pady=5          # External padding
    )
    
    buttons.append(button)  # Store the button instance

root.after(1, load_game)  # Load game after 100ms
root.mainloop()