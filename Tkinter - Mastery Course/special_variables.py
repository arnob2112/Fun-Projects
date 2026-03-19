import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Special Variables Demo")

# =====================
# 1. StringVar Example
# =====================
# Create a StringVar to store user's name
name_var = tk.StringVar()

# Label prompting the user to enter name
tk.Label(root, text="Enter your name:").pack()

# Entry widget linked to name_var
# Typing in the Entry updates name_var automatically
tk.Entry(root, textvariable=name_var).pack()


# =====================
# 2. IntVar Example
# =====================
# Create an IntVar to store favorite color selection
color_var = tk.IntVar()

# Label for color selection
tk.Label(root, text="Choose your favorite color:").pack()

# Radiobuttons linked to color_var
# Each button assigns a specific integer value to color_var when selected
tk.Radiobutton(root, text="Red", variable=color_var, value=1).pack()
tk.Radiobutton(root, text="Green", variable=color_var, value=2).pack()
tk.Radiobutton(root, text="Blue", variable=color_var, value=3).pack()


# =====================
# 3. DoubleVar Example
# =====================
# Create a DoubleVar to store user's age (as a float)
age_var = tk.DoubleVar()

# Label for age selection
tk.Label(root, text="Select your age:").pack()

# Scale widget (slider) linked to age_var
# Moving the slider updates age_var automatically
# 'resolution=0.5' allows half-step increments
tk.Scale(root, variable=age_var, from_=0, to=100, orient='horizontal', resolution=0.5).pack()


# =====================
# 4. BooleanVar Example
# =====================
# Create a BooleanVar to track newsletter subscription
subscribe_var = tk.BooleanVar()

# Checkbutton linked to subscribe_var
# Checking it sets subscribe_var to True, unchecking sets it to False
tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe_var).pack()


# =====================
# Function to Display All Values
# =====================
def show_values():
    # Map integer values to color names
    colors = {1: "Red", 2: "Green", 3: "Blue"}
    
    # Use .get() to retrieve current values from special variables
    print("Name:", name_var.get())  # StringVar
    print("Favorite Color:", colors.get(color_var.get(), "None"))  # IntVar
    print("Age:", age_var.get())  # DoubleVar
    print("Subscribed:", subscribe_var.get())  # BooleanVar

# Button to trigger value display
tk.Button(root, text="Show Values", command=show_values).pack()

# Start the Tkinter event loop
root.mainloop()