import tkinter as tk

# ---------------- APP ----------------
app = tk.Tk()
app.title("Gym Diet App - Raaone Zone")
app.geometry("350x520")
app.configure(bg="#111111")

# ---------------- TITLE ----------------
tk.Label(
    app,
    text="GYM DIET APP 💪",
    fg="red",
    bg="#111111",
    font=("Arial", 18, "bold")
).pack(pady=10)

# ---------------- WEIGHT ----------------
tk.Label(app, text="Enter Weight (kg):", fg="white", bg="#111111").pack()
weight_entry = tk.Entry(app)
weight_entry.pack(pady=5)

# ---------------- GOAL ----------------
tk.Label(app, text="Select Goal:", fg="white", bg="#111111").pack(pady=5)
goal = tk.StringVar(value="Cut")

tk.Radiobutton(app, text="Cut", variable=goal, value="Cut",
               fg="white", bg="#111111", selectcolor="#111111").pack()
tk.Radiobutton(app, text="Maintain", variable=goal, value="Maintain",
               fg="white", bg="#111111", selectcolor="#111111").pack()
tk.Radiobutton(app, text="Bulk", variable=goal, value="Bulk",
               fg="white", bg="#111111", selectcolor="#111111").pack()

# ---------------- FOOD INPUTS ----------------
def make_entry(label):
    tk.Label(app, text=label, fg="white", bg="#111111").pack()
    e = tk.Entry(app)
    e.pack(pady=3)
    return e

chicken_entry = make_entry("Chicken (grams):")
egg_entry = make_entry("Eggs (count):")
oats_entry = make_entry("Oats (grams):")
whey_entry = make_entry("Whey (scoops):")

# ---------------- RESULT LABELS ----------------
result_label = tk.Label(
    app, text="", fg="yellow", bg="#111111", font=("Arial", 11)
)
result_label.pack(pady=10)

food_label = tk.Label(
    app, text="", fg="white", bg="#111111",
    font=("Arial", 10), justify="left"
)
food_label.pack(pady=5)

# ---------------- LOGIC ----------------
def calculate():
    try:
        weight = float(weight_entry.get())

        chicken = float(chicken_entry.get() or 0)
        eggs = float(egg_entry.get() or 0)
        oats = float(oats_entry.get() or 0)
        whey = float(whey_entry.get() or 0)

        # Protein calculation
        protein = (
            (chicken * 0.31) +   # 31g per 100g chicken
            (eggs * 6) +         # 6g per egg
            (oats * 0.13) +      # 13g per 100g oats
            (whey * 24)          # 24g per scoop
        )

        # Calories by goal
        if goal.get() == "Cut":
            calories = int(weight * 22)
        elif goal.get() == "Maintain":
            calories = int(weight * 26)
        else:  # Bulk
            calories = int(weight * 30)

        food = (
            "Food Plan:\n"
            f"- Chicken: {chicken} g\n"
            f"- Eggs: {eggs}\n"
            f"- Oats: {oats} g\n"
            f"- Whey: {whey} scoop(s)"
        )

        result_label.config(
            text=f"Calories: {calories} kcal/day\nProtein: {protein:.1f} g/day"
        )
        food_label.config(text=food)

    except ValueError:
        result_label.config(text="❌ Enter numbers only")
        food_label.config(text="")

# ---------------- BUTTON ----------------
tk.Button(
    app,
    text="CALCULATE",
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    command=calculate
).pack(pady=15)

# ---------------- START ----------------
app.mainloop()
