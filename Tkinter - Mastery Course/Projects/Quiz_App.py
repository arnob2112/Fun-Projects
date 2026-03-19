import tkinter as tk
from tkinter import ttk

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x400")
        self.resizable(False, False)
        self.config(bg="#1B263B")

        self.style = ttk.Style()

        self.create_card()

    def create_card(self):
        self.style.configure("Card.TFrame", background="#F5F5F5", borderwidth=1, relief="solid")

        card_frame = ttk.Frame(self, style="Card.TFrame")
        card_frame.pack(expand=True)


app = QuizApp()
app.mainloop()