import tkinter as tk

def update_label():
    # Get the text from the entry widget and update the label
    new_text = entry.get()
    label.configure(text=new_text)

# Create the main window
root = tk.Tk()
root.title("Dynamic Label Example")

# Create an Entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a Button to trigger the label update
update_button = tk.Button(root, text="Update Label", command=update_label)
update_button.pack(pady=5)

# Create a Label widget
label = tk.Label(root, text="This label will change!")
label.pack(pady=10)

width = 100
height = 100

# Start the Tkinter event loop
root.mainloop()