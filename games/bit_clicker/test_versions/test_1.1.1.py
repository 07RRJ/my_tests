import tkinter as tk

bits = 0

def on_button_click():
    global bits
    bits += 1
    print(f"Button clicked {bits} times")

root = tk.Tk()
label = tk.Label(root, text="Welcome to my Tkinter app!")
label.pack()
button = tk.Button(root, text=f"Click Me!{bits}", command=on_button_click)
button.pack()
root.mainloop()