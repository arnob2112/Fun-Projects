import tkinter as tk  

# Create a class that inherits from tk.Tk (the main window class)
class App(tk.Tk):
    def __init__(self):
        # Call the constructor of the parent class (tk.Tk)
        # This initializes the main window
        super().__init__()

        # Set the window title
        self.title("OOP App")

        # Call a separate method to create widgets
        # This keeps the code organized (OOP style)
        self.create_widgets()

    def create_widgets(self):
        # Create a Label widget
        # "self" means the widget belongs to this window
        self.label = tk.Label(self, text="Hello")

        # Add the label to the window using the pack layout manager
        # pack() automatically places the widget inside the window
        self.label.pack()

if __name__ == "__main__":
    
    # Create an instance of the App class (create the window)
    app = App()
    app.mainloop()