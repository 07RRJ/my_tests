from tkinter import ttk, Tk

root = Tk()

# Initialize the bits variable
bits = 10

# Function to handle button click (update only the variable part of the text)
# def handle_button_click(button, action):
    # global bits  # Update the global bits variable
    
    # # Increase bits on each click (you can change this logic as needed)
    # bits += 1
    
    # # Update the button's text by formatting the string with the updated bits value
    # current_text = button.cget('text')  # Get the current text of the button
    
    # # Replace the placeholder {bits} with the current bits value
    # new_text = current_text.format(bits=bits)
    
    # # Update the button's label
    # button.config(text=new_text)
    # print(f"Updated text: {new_text}")
    # print(bits)

# Define action functions for each button
def action_1(button):
    global bits
    bits += 1
    print("Performing custom action for Button 1...")
    button.config(text=f"bits/click - {bits}")  # Update the text of the existing button
    print(bits)
    # handle_button_click(button, action_1)

def action_2(button):
    print("Performing custom action for Button 2...")
    # handle_button_click(button, action_2)

def action_3(button):
    print(button)
    print("Performing custom action for Button 3...")
    # handle_button_click(button, action_3)

# Define the button texts, grid positions, and the associated action functions
buttons_info = [
    ("bits/click - {bits}", 2, 0, action_1),
    ("auto - {bits}", 2, 1, action_2),
    ("upgrade auto - {bits}", 2, 2, action_3),
    ("7", 3, 0, action_1),
    ("8", 3, 1, action_2),
    ("9", 3, 2, action_3),
    ("4", 4, 0, action_1),
    ("5", 4, 1, action_2),
    ("6", 4, 2, action_3),
    ("1", 5, 0, action_1),
    ("2", 5, 1, action_2),
    ("3", 5, 2, action_3),
    ("0", 6, 0, action_1),
    (".", 6, 1, action_2),
    ("=", 6, 2, action_3),
]

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

root.mainloop()