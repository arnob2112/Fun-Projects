import tkinter as tk

root = tk.Tk()      # create main window
root.title("My First App")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="lightblue")

def greet(): 
    text = entry.get()  # taking input from user
    label.config(text=f"Hello, {text}") # used for updating the same label. not creating another one.
    button.destroy()    # removing the widget.
    entry.destroy()


frame = tk.Frame(root, bg="orange", height=300, width=400) 
frame.pack(fill="x", expand=True)
frame.pack_propagate(False)

label = tk.Label(frame, text="Hello, World!",
                font=("helvetica", 15),
                bg="orange", fg="black")
label.pack(fill="both", expand=True)                    

entry = tk.Entry(frame, bg="white") # creating entry box for taking input

button = tk.Button(frame, text="Submit", command=greet,
                    bg="purple", fg="white")

button.pack(side="bottom", pady=10)
entry.pack(side="bottom")                    






root.mainloop()     # start event loop

