import os
import tkinter as tk
from time import sleep
import threading

os.system("cls")

bits = 0
# bits = 100000000000000000000000000000000000000000000000000000
bits_pr_c = 1
bits_pr_c_price = 10
auto_price = 500
upgrade_auto_price = 750
better_auto = 1

def on_button_click():
    global bits
    global bits_pr_c
    bits += bits_pr_c
    label.config(text = f"your bits {bits}")

def upgrade_bits_p_c():
    global bits
    global bits_pr_c
    global bits_pr_c_price
    if bits > bits_pr_c_price:
        bits -= bits_pr_c_price
        label.config(text = f"your bits {bits}")
        bits_pr_c += 1
        bits_pr_c_price += int((bits_pr_c_price**0.5)*10)
        bits_per_click.config(text = f"upgrade bits/click - {bits_pr_c_price}")

def bits_ps_buy():
    print("1")
    global bits
    global auto_price
    if bits > auto_price:
        bits -= auto_price
        label.config(text = f"your bits {bits}")
        action2 = threading.Thread(target=bits_ps)
        action2.start()
        buy_auto.destroy()
        auto_upgrade.pack()
    elif bits < auto_price:
        action3 = threading.Thread(target = rename_auto)
        action3.start()

def rename_auto():
    buy_auto.config(text = f"not enugh bits")
    sleep(3)
    buy_auto.config(text = f"auto buy - {auto_price}")

# def rename():
#     rename.config(text = "")
#     sleep(3)
#     rename.config(text = "")

def bits_ps():
    global bits
    while True:
        sleep(1)
        bits += better_auto * bits_pr_c
        # bits += int((better_auto/10)**0.5) good scaling
        label.config(text = f"your bits {bits}")
        print(bits)

def upgrade_auto():
    global bits
    global upgrade_auto_price
    global better_auto
    if bits > upgrade_auto_price:
        bits -= upgrade_auto_price
        upgrade_auto_price += int((upgrade_auto_price**0.5)*10)
        auto_upgrade.config(text = f"upgrade auto - {upgrade_auto_price}")
        better_auto += 1

# multitask(=

root = tk.Tk()
label = tk.Label(root, text = "clicker game")
label.pack()
button = tk.Button(root, text = "Click Me!", command = on_button_click)
button.pack()
bits_per_click = tk.Button(root, text = f"upgrade bits/click - {bits_pr_c_price}", command = upgrade_bits_p_c)
bits_per_click.pack()
buy_auto = tk.Button(root, text = f"buy auto - {auto_price}", command = bits_ps_buy)
buy_auto.pack()
auto_upgrade = tk.Button(root, text = f"upgrade auto - {upgrade_auto_price}", command = upgrade_auto)

root.title("clicker game")
width = 500
height = 600
root.geometry(f"{width}x{height}")

root.mainloop()