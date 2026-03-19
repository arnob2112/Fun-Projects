import tkinter as tk

root = tk.Tk()  # creating main window.
root.title("LOGIN")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="lightblue")

frame1 = tk.Frame(root, bg="#D3D3D3", height=300, width=250)
frame1.pack_propagate(False)
frame1.pack(pady=40)

frame2= tk.Frame(frame1, bg="#D3D3D3")
frame2.pack(expand=True)


username = tk.Label(frame2, text="Username:")
username.grid(row=0, column=0)
username_entry = tk.Entry(frame2)
username_entry.grid(row=0, column=1)

password = tk.Label(frame2, text="Password:")
password.grid(row=1, column=0)
password_entry = tk.Entry(frame2, show="*")
password_entry.grid(row=1, column=1)

button = tk.Button(frame2, text="Login")
button.grid(row=2, column=1)

root.mainloop()
