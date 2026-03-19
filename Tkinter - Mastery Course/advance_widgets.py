# tkinter_classic_colors_commented.py
import tkinter as tk
from tkinter import messagebox

# ============================
# 1. Main Window
# ============================
root = tk.Tk()  # Create the main application window
root.title("Classic Tkinter Form")  # Set window title
root.geometry("450x550")  # Set fixed window size
root.configure(bg="#f0f0f0")  # Light gray background for the window

# ============================
# 2. Top Frame - User Info
# ============================
# Frame to group user info section with background color and border
top_frame = tk.Frame(root, bg="#d1e7dd", bd=2, relief="groove")
top_frame.pack(padx=10, pady=10, fill="x")

# Section label
tk.Label(top_frame, text="User Information", bg="#d1e7dd",
         font=("Arial", 14, "bold")).pack(pady=5)

# Name Entry
# StringVar will automatically store and update the Entry text
name_var = tk.StringVar()
tk.Label(top_frame, text="Enter your name:", bg="#d1e7dd").pack(anchor="w", padx=5)
tk.Entry(top_frame, textvariable=name_var, width=30).pack(padx=5, pady=5)

# ============================
# 3. Middle Frame - Preferences
# ============================
# Frame for color selection and hobbies with yellow background
middle_frame = tk.Frame(root, bg="#fff3cd", bd=2, relief="groove")
middle_frame.pack(padx=10, pady=10, fill="x")

# --- Favorite Color Radiobuttons ---
tk.Label(middle_frame, text="Select your favorite color:", bg="#fff3cd").pack(anchor="w", padx=5, pady=5)

# IntVar stores the integer value of the selected radiobutton
color_var = tk.IntVar()
tk.Radiobutton(middle_frame, text="Red", variable=color_var, value=1, bg="#fff3cd").pack(anchor="w", padx=20)
tk.Radiobutton(middle_frame, text="Green", variable=color_var, value=2, bg="#fff3cd").pack(anchor="w", padx=20)
tk.Radiobutton(middle_frame, text="Blue", variable=color_var, value=3, bg="#fff3cd").pack(anchor="w", padx=20)

# --- Hobbies Checkbuttons ---
tk.Label(middle_frame, text="Select your hobbies:", bg="#fff3cd").pack(anchor="w", padx=5, pady=5)

# BooleanVars store True/False depending on checkbox state
hobby_read_var = tk.BooleanVar()
hobby_music_var = tk.BooleanVar()
hobby_sport_var = tk.BooleanVar()

# Each Checkbutton updates its BooleanVar when toggled
tk.Checkbutton(middle_frame, text="Reading", variable=hobby_read_var, bg="#fff3cd").pack(anchor="w", padx=20)
tk.Checkbutton(middle_frame, text="Music", variable=hobby_music_var, bg="#fff3cd").pack(anchor="w", padx=20)
tk.Checkbutton(middle_frame, text="Sports", variable=hobby_sport_var, bg="#fff3cd").pack(anchor="w", padx=20)

# ============================
# 4. Listbox Frame - Country
# ============================
# Frame for country selection with blue background
listbox_frame = tk.Frame(root, bg="#cff4fc", bd=2, relief="groove")
listbox_frame.pack(padx=10, pady=10, fill="x")

# Label
tk.Label(listbox_frame, text="Select your country:", bg="#cff4fc").pack(anchor="w", padx=5, pady=5)

# Listbox widget allows selecting one country
country_listbox = tk.Listbox(listbox_frame, height=5, bg="white")
countries = ["USA", "Canada", "UK", "Australia", "India"]
for country in countries:
    country_listbox.insert(tk.END, country)  # Insert each country into the listbox
country_listbox.pack(padx=20, pady=5)

# ============================
# 5. Bottom Frame - Age & Submit
# ============================
# Frame for age slider and submit button with red background
bottom_frame = tk.Frame(root, bg="#f8d7da", bd=2, relief="groove")
bottom_frame.pack(padx=10, pady=10, fill="x")

# Age Scale
tk.Label(bottom_frame, text="Select your age:", bg="#f8d7da").pack(anchor="w", padx=5, pady=5)

# DoubleVar stores the slider value as a float
age_var = tk.DoubleVar()
tk.Scale(bottom_frame, variable=age_var, from_=0, to=100,
         orient="horizontal", resolution=1, bg="#f8d7da", troughcolor="#ffffff").pack(padx=20, pady=5, fill="x")

# ============================
# 6. Function to Show All Values
# ============================
def show_values():
    # --- Retrieve user name from Entry ---
    name = name_var.get()
    
    # --- Retrieve favorite color from Radiobutton ---
    colors = {1: "Red", 2: "Green", 3: "Blue"}
    color = colors.get(color_var.get(), "None")
    
    # --- Retrieve hobbies from Checkbuttons ---
    hobbies = []
    if hobby_read_var.get(): hobbies.append("Reading")
    if hobby_music_var.get(): hobbies.append("Music")
    if hobby_sport_var.get(): hobbies.append("Sports")
    
    # --- Retrieve selected country from Listbox ---
    try:
        country_index = country_listbox.curselection()[0]  # Get selected index
        country = country_listbox.get(country_index)       # Get country name
    except IndexError:
        country = "None"  # No selection made
    
    # --- Retrieve age from Scale ---
    age = age_var.get()
    
    # --- Show all information in a messagebox ---
    messagebox.showinfo("User Information",
                        f"Name: {name}\n"
                        f"Favorite Color: {color}\n"
                        f"Hobbies: {', '.join(hobbies) if hobbies else 'None'}\n"
                        f"Country: {country}\n"
                        f"Age: {age}")

# ============================
# Submit Button
# ============================
# Clicking the button triggers show_values() function
tk.Button(bottom_frame, text="Submit", command=show_values,
          bg="#0d6efd", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# ============================
# 7. Run the Tkinter Event Loop
# ============================
root.mainloop()  # Start the GUI