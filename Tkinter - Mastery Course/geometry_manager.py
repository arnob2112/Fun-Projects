import tkinter as tk 

root = tk.Tk()      # create main window
root.title("My First App")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="lightblue")


# there are three geometry managers. Only one can be used per container. 
frame1 = tk.Frame(root, bg="lightblue")
frame1.pack(pady=10) 

# label is used for displaying text or image
label1 = tk.Label(frame1, text="Hello, Pack", 
                font="helvetica", fg="white", 
                bg="black", width=20, height=2)

label1.pack()    # it packs widgets in order relative to each other.

frame2 = tk.Frame(root, bg="lightblue", width=400, height=100)
frame2.pack()
frame2.pack_propagate(False)    # Do NOT resize this frame based on its children.
label2 = tk.Label(frame2, text="Hello, Place", 
                font="helvetica", fg="white", 
                bg="black", width=20, height=2)
label2.place(relx=0.2, rely=0.3)  # places widgets using absolute coordinates (x, y).

frame3 = tk.Frame(root, bg="lightblue")
frame3.pack(pady=10)
label3 = tk.Label(frame3, text="Hello, Grid", 
                font="helvetica", fg="white", 
                bg="black", width=20, height=2)
label3.grid(row=0, column=3)    # places widgets in a table structure using row & column numbers.

root.mainloop()     # start event loop

