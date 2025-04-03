from tkinter import ttk, Tk

root = Tk()

# Initialize multiple variables for different button actions
variables = {
    'bits': 10,
    'coins': 5,
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

# Define action functions for each button
def action_1(button):
    variables['bits'] += 1
    print("Action 1 (bits) executed.")
    button.config(text=f"bits/click - {variables['bits']}")
    print(variables['bits'])

def action_2(button):
    variables['coins'] += 2
    print("Action 2 (coins) executed.")
    button.config(text=f"coins - {variables['coins']}")
    print(variables['coins'])

def action_3(button):
    variables['score'] += 10
    print("Action 3 (score) executed.")
    button.config(text=f"score - {variables['score']}")
    print(variables['score'])

def action_4(button):
    variables['level'] += 1
    print("Action 4 (level) executed.")
    button.config(text=f"level - {variables['level']}")
    print(variables['level'])

def action_5(button):
    variables['health'] += 5
    print("Action 5 (health) executed.")
    button.config(text=f"health - {variables['health']}")
    print(variables['health'])

def action_6(button):
    variables['mana'] += 3
    print("Action 6 (mana) executed.")
    button.config(text=f"mana - {variables['mana']}")
    print(variables['mana'])

def action_7(button):
    variables['experience'] += 20
    print("Action 7 (experience) executed.")
    button.config(text=f"experience - {variables['experience']}")
    print(variables['experience'])

def action_8(button):
    variables['gold'] += 50
    print("Action 8 (gold) executed.")
    button.config(text=f"gold - {variables['gold']}")
    print(variables['gold'])

def action_9(button):
    variables['gems'] += 1
    print("Action 9 (gems) executed.")
    button.config(text=f"gems - {variables['gems']}")
    print(variables['gems'])

def action_10(button):
    variables['stamina'] += 10
    print("Action 10 (stamina) executed.")
    button.config(text=f"stamina - {variables['stamina']}")
    print(variables['stamina'])

def action_11(button):
    variables['power'] += 2
    print("Action 11 (power) executed.")
    button.config(text=f"power - {variables['power']}")
    print(variables['power'])

def action_12(button):
    variables['strength'] += 1
    print("Action 12 (strength) executed.")
    button.config(text=f"strength - {variables['strength']}")
    print(variables['strength'])

def action_13(button):
    variables['agility'] += 3
    print("Action 13 (agility) executed.")
    button.config(text=f"agility - {variables['agility']}")
    print(variables['agility'])

def action_14(button):
    variables['intelligence'] += 2
    print("Action 14 (intelligence) executed.")
    button.config(text=f"intelligence - {variables['intelligence']}")
    print(variables['intelligence'])

def action_15(button):
    variables['defense'] += 4
    print("Action 15 (defense) executed.")
    button.config(text=f"defense - {variables['defense']}")
    print(variables['defense'])
    print(variables)

# Define the button texts, grid positions, and the associated action functions
buttons_info = [
    ("bits/click - {bits}", 2, 0, action_1, 'bits'),
    ("coins - {coins}", 2, 1, action_2, 'coins'),
    ("score - {score}", 2, 2, action_3, 'score'),
    ("level - {level}", 3, 0, action_4, 'level'),
    ("health - {health}", 3, 1, action_5, 'health'),
    ("mana - {mana}", 3, 2, action_6, 'mana'),
    ("experience - {experience}", 4, 0, action_7, 'experience'),
    ("gold - {gold}", 4, 1, action_8, 'gold'),
    ("gems - {gems}", 4, 2, action_9, 'gems'),
    ("stamina - {stamina}", 5, 0, action_10, 'stamina'),
    ("power - {power}", 5, 1, action_11, 'power'),
    ("strength - {strength}", 5, 2, action_12, 'strength'),
    ("agility - {agility}", 6, 0, action_13, 'agility'),
    ("intelligence - {intelligence}", 6, 1, action_14, 'intelligence'),
    ("defense - {defense}", 6, 2, action_15, 'defense'),
]

buttons = []  # Store button instances

# Create buttons dynamically
for button_text, row, col, action_function, variable in buttons_info:
    # Format the button text dynamically using the variables dictionary
    formatted_text = button_text.format(**variables)

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
