from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class TextEditor:

    current_open_file = "no file"

    def __init__(self, master):
        self.master = master
        master.title("Text Editor")

        # creating text box to write anything
        self.text_area = Text(self.master, undo=True, wrap=WORD)
        self.text_area.pack(fill=BOTH, expand=1)

        # creating menu bar
        self.main_menu = Menu(master)
        self.master.config(menu=self.main_menu)

        # adding items in main menu
        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="new", command=self.new_file)
        self.file_menu.add_command(label="open     -Ctrl + o", command=self.open_files)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="save     -Ctrl + s", command=self.save_file)
        self.file_menu.add_command(label="save as", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="exit", command=self.quit_it)

        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="redo", command=self.text_area.edit_redo)
        self.edit_menu.add_command(label="cut     -Ctrl + x", command=self.cut_text)
        self.edit_menu.add_command(label="copy     -Ctrl + c", command=self.copy_text)
        self.edit_menu.add_command(label="paste     -Ctrl + v", command=self.paste_text)

        # creating shortcut keys
        self.master.bind("<Control - o>", self.open_files)
        self.master.bind("<Control - s>", self.save_file)

    def new_file(self):
        self.current_open_file = "no file"
        self.text_area.delete(1.0, END)

    def open_files(self, event=""):
        file = filedialog.askopenfile(initialdir="/", filetypes=(("text file", ".txt"), ("all files", "*.*")))
        if file is not None:
            self.text_area.delete(1.0, END)
            for line in file:
                self.text_area.insert(END, line)
            self.current_open_file = file.name
            file.close()

    def save_file(self, event=""):
        if self.current_open_file == "no file":
            self.save_as_file()
        else:
            file = open(self.current_open_file, "w+")
            file.write(self.text_area.get(1.0, END))
            file.close()

    def save_as_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if file is not None:
            self.current_open_file = file.name
            file.write(self.text_area.get(1.0, END))
            file.close()

    def cut_text(self, event=""):
        self.copy_text()
        self.text_area.delete("sel.first", "sel.last")

    def copy_text(self, event=""):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste_text(self, event=""):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())

    def quit_it(self):
        answer = messagebox.askyesno("Exit", "Are you sure?")
        if answer == 1:
            self.master.quit()


root = Tk()
root.geometry("300x300+625+275")

text = TextEditor(root)

root.mainloop()
