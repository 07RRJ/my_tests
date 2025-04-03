import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # For displaying messages
import json  # For saving and loading data
import os   # Cleaner console
from time import sleep
import threading
import json


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

def upgrade_bits_per_click():
    global bits
    global bits_pr_c
    global bits_pr_c_price
    if bits > bits_pr_c_price:
        bits -= bits_pr_c_price
        label.config(text = f"Your bits {bits}")
        bits_pr_c += 1
        bits_pr_c_price += int((bits_pr_c_price**0.5)*10)
        bits_per_click.config(text = f"upgrade bits/click - {bits_pr_c_price}")
    elif bits < bits_pr_c_price:
        action3 = threading.Thread(target = rename_bits_per_click)
        action3.start()

def rename_bits_per_click():
    bits_per_click.config(text = f"not enugh bits")
    sleep(3)
    bits_per_click.config(text = f"bits/click - {bits_pr_c_price}")

def bits_ps_buy():
    global bits
    global auto_price
    if bits > auto_price:
        bits -= auto_price
        auto_price += int((auto_price**0.5)*10)
        label.config(text = f"Your bits {bits}")
        action1 = threading.Thread(target=bits_ps)
        action1.start()
        buy_auto.destroy()
        auto_upgrade.config(text = f"upgrade auto - {auto_price}")
        auto_upgrade.pack()
    elif bits < auto_price:
        action2 = threading.Thread(target = rename_auto)
        action2.start()

def rename_auto():
    buy_auto.config(text = f"not enugh bits")
    sleep(3)
    buy_auto.config(text = f"auto buy - {auto_price}")



def bits_ps():
    global bits
    while True:
        sleep(1)
        bits += better_auto
        # bits += int((better_auto/10)**0.5) good scaling
        label.config(text = f"Your bits {bits}")

def upgrade_auto():
    global bits
    global auto_price
    global better_auto
    if bits > auto_price:
        bits -= auto_price
        auto_price += int((auto_price**0.5)*10)
        auto_upgrade.config(text = f"upgrade auto - {auto_price}")
        better_auto += 1

root = tk.Tk()
label = ttk.Label(root, text = "Clicker Game", font=("Arial", 24))
label.pack()
button = ttk.Button(root, text = "Click Me!", command = on_button_click)
button.pack()
bits_per_click = ttk.Button(root, text = f"upgrade bits/click - {bits_pr_c_price}", command = upgrade_bits_per_click)
bits_per_click.pack()
buy_auto = ttk.Button(root, text = f"buy auto - {auto_price}", command = bits_ps_buy)
buy_auto.pack()
auto_upgrade = ttk.Button(root, text = f"upgrade auto - {auto_price}", command = upgrade_auto)

root.title("07RRJ's Clicker Game")
style = ttk.Style(root)
style.theme_use("xpnative")
width = 500
height = 600
root.geometry(f"{width}x{height}")



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