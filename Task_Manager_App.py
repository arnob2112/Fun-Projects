from tkinter import Tk, ttk, Frame, Label, Entry, Listbox, Button, StringVar, END, messagebox

class TaskManager(Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("400x300")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        top_frame = Frame(self)
        top_frame.config(bg="lightblue")
        top_frame.grid(row=0, column=0, padx=5, sticky="ew")

        # making main window expandable
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        
        # creating four columns inside top frame
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=0)
        top_frame.columnconfigure(2, weight=0)
        top_frame.columnconfigure(3, weight=1)
        

        self.task_var = StringVar()
        self.app_title = Label(top_frame, text="TASK MANAGER APP",
                                bg="lightblue", font=("Arial", 16, "bold"))
        self.entry = Entry(top_frame, textvariable=self.task_var)
        self.listbox = Listbox(top_frame)
        self.add_button = Button(top_frame, text="Add", command=self.add_task)
        

        self.app_title.grid(row=0, column=1, columnspan=2, pady=(10, 0))
        self.entry.bind("<Return>", self.add_task)
        self.entry.grid(row=1, column=1, pady=10)
        self.add_button.grid(row=1, column=2, padx=10, pady=10)
        self.listbox.grid(row=2, column=1, pady=5, columnspan=2, sticky="snew")


        bottom_frame = Frame(self)
        bottom_frame.config(bg="lightblue")
        bottom_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 5), sticky="snew")

        # creating four columns inside botton frame
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=0)
        bottom_frame.columnconfigure(2, weight=0)
        bottom_frame.columnconfigure(3, weight=1)

        Button(bottom_frame, text="Delete", command=self.delete_task).grid(row=0, column=1, padx=5)
        Button(bottom_frame, text="Clear All", command=self.clear_all).grid(row=0, column=2, padx=5)


    
    def add_task(self, event=None): # for using this func in both command= and when enter pressed event=None is used.
        task  = self.task_var.get().title()
        if task:
            self.listbox.insert(END, task)
            self.task_var.set("")

    def delete_task(self):
         selected = self.listbox.curselection()
         if selected:
            self.listbox.delete(selected)

    def clear_all(self):
        message = messagebox.askyesno("Confirm", "Clear all tasks?")
        if message:
            self.listbox.delete(0, END)



app = TaskManager()
app.mainloop()