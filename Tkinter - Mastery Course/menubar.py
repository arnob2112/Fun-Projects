import tkinter as tk 

root = tk.Tk()      # create main window
root.title("My First App")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="lightblue")

menu = tk.Menu(root)                # Create a Menu widget (the main menu bar)
root.config(menu=menu)              # Attach the menu bar to the main window

# ============================
# 3. Create the File menu (submenu)
# ============================
file_menu = tk.Menu(menu, tearoff=0)    # Create a submenu for "File"
                                        # tearoff=0 disables the dashed line at the top
menu.add_cascade(label="File", menu=file_menu)  # Add "File" menu to the menu bar

# ============================
# 4. Add items to the File menu
# ============================
file_menu.add_command(label="Exit", command=root.quit)  
# Adds an "Exit" option in the File menu
# When clicked, root.quit() closes the application


root.mainloop()     # start event loop

