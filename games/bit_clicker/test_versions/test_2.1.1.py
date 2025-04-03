from tkinter import Tk, ttk 

root = Tk()

def handle_button_click(button):
    print (button)
    # Get the current text of the button
    current_text = button.cget("text")  # This is correct

    # Change the text to something else
    new_text = "Button Clicked!"  # Or use a different logic to determine the new text

    # Rename the button
    button.config(text=new_text)

# Create 9 buttons
buttons = []
for row in range(3):
    for col in range(3):
        # Use default argument to correctly capture the button instance
        button = ttk.Button(root, text=row * 3 + col + 1)
        button.config(command=lambda b=button: handle_button_click(b))  # Correct way to pass button
        button.grid(row=row, column=col, sticky="nsew")
        buttons.append(button)

root.mainloop()
