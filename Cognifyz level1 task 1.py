import tkinter as tk
from tkinter import messagebox

def reverse_string():
    text = input_entry.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    if reverse_mode.get() == "characters":
        reversed_text = text[::-1]
    elif reverse_mode.get() == "words":
        reversed_text = ' '.join(text.split()[::-1])
    
    if ignore_case.get():
        reversed_text = reversed_text.lower()

    result_label.config(text=f"Reversed Output:\n{reversed_text}")

# GUI setup
app = tk.Tk()
app.title("Advanced String Reverser")
app.geometry("400x300")
app.resizable(False, False)

tk.Label(app, text="Enter text to reverse:", font=("Arial", 12)).pack(pady=10)
input_entry = tk.Entry(app, width=40)
input_entry.pack(pady=5)

# Reversal mode
reverse_mode = tk.StringVar(value="characters")
tk.Label(app, text="Choose reversal mode:").pack(pady=5)
tk.Radiobutton(app, text="By Characters", variable=reverse_mode, value="characters").pack()
tk.Radiobutton(app, text="By Words", variable=reverse_mode, value="words").pack()

# Ignore case
ignore_case = tk.BooleanVar()
tk.Checkbutton(app, text="Ignore Case (convert to lowercase)", variable=ignore_case).pack(pady=5)

# Button
tk.Button(app, text="Reverse", command=reverse_string).pack(pady=10)

# Result
result_label = tk.Label(app, text="", font=("Arial", 11), wraplength=350, justify="center")
result_label.pack()

app.mainloop()
