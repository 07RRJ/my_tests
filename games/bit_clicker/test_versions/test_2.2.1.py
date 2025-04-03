from tkinter import Tk, ttk 
import os

root = Tk()

def handle_button_click(button):
    os.system("cls")
    """Handles button click events by updating the button's text."""
    current_text = button.cget("text")  # Get the current text
    new_text = "Clicked!"  # Change to new text (you can modify this logic)
    button.config(text=new_text)

# Button data: (text, row, col[, colspan])
buttons_info = [
    (f"bits/click - 10", 2, 0), (f"auto - 20", 2, 1), (f"upgrade auto - 30", 2, 2),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), 
    ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), 
    ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), 
    ("0", 6, 0), (".", 6, 1), ("=", 6, 2),
]

buttons = []  # Store button instances

# Create buttons dynamically
for button_info in buttons_info:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1

    # Create button instance
    button = ttk.Button(root, text=button_text)
    
    # Correct way to pass the button instance
    button.config(command=lambda b=button: handle_button_click(b))
    
    # Place the button in the grid
    button.grid(
        row=row,
        column=col,
        columnspan=colspan,
        sticky="nsew",
        ipadx=10,  # Internal padding for larger buttons
        ipady=4,
        padx=5,  # External padding
        pady=5
    )
    
    buttons.append(button)  # Store the button instance

root.mainloop()
