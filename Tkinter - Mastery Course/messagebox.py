from tkinter import messagebox

messagebox.showinfo("Title", "Message")
messagebox.showerror("Error", "Something wrong")
messagebox.askyesno("Confirm", "Are you sure?") # it can return True or False to handle critical confirmations like exiting, deleting
