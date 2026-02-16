import tkinter as tk

# =====================
# Window create
# =====================
app = tk.Tk()
app.title("Raaone Zone Calculator")
app.geometry("300x420")
app.configure(bg="#111111")

# =====================
# Title
# =====================
title_label = tk.Label(
    app,
    text="RAAONE ZONE 🔥",
    font=("Arial", 16, "bold"),
    fg="red",
    bg="#111111"
)
title_label.pack(pady=5)

# =====================
# Entry box
# =====================
entry = tk.Entry(
    app,
    font=("Arial", 20),
    justify="right",
    bg="black",
    fg="white",
    insertbackground="white"
)
entry.pack(fill="both", padx=10, pady=10)

# =====================
# Functions
# =====================
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# =====================
# Buttons frame
# =====================
frame = tk.Frame(app, bg="#111111")
frame.pack()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

for i, btn in enumerate(buttons):
    if btn == "=":
        action = calculate
    else:
        action = lambda x=btn: click(x)

    tk.Button(
        frame,
        text=btn,
        width=5,
        height=2,
        font=("Arial", 14, "bold"),
        bg="#1f1f1f",
        fg="white",
        activebackground="red",
        activeforeground="white",
        command=action
    ).grid(row=i//4, column=i%4, padx=5, pady=5)

# =====================
# Clear button
# =====================
tk.Button(
    app,
    text="CLEAR",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    command=clear
).pack(fill="both", padx=10, pady=10)

# =====================
# Run app
# =====================
app.mainloop()