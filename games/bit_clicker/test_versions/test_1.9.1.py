from tkinter import Tk, ttk

def handle_button_click(text):
    if text == "C":
        print("adaf")

buttons = [
    (f"upgrade bits/click", 1, 0), (f"buy auto", 1, 1), ("upgrade upgrade bits/click", 1, 2),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), 
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), 
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), 
    ("0", 5, 0,), (".", 5, 1), ("=", 5, 2),
]

root = Tk()

for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    button.grid(
        row=row,
        column=col,
        columnspan=colspan,
        sticky="nsew",
        ipadx=10,  # Increase internal padding for larger buttons
        ipady=4,   # Increase internal padding for larger buttons
        padx=5,   # Adjust external padding as needed
        pady=5,   # Adjust external padding as needed
    )

for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

# Configure rows and columns to be expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)  # Allow rows to expand
for i in range(3):
    root.grid_columnconfigure(i, weight=1)  # Allow columns to expand

width = 1000
height = 800
root.geometry(f"{width}x{height}")

# Make the window non-resizable
root.resizable(False, False)

root.mainloop()