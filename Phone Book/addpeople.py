from tkinter import *
import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("mypeopledatabase")
cursor = connection.cursor()

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+350+150")
        self.title("Add New People")
        self.resizable(False, False)

        # creating top frame
        self.top_frame = Frame(self, height=150, bg='#f5f5f5')
        self.top_frame.pack(fill=X)

        self.top_image = PhotoImage(file='icons/person.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg='#f5f5f5')
        self.top_image_label.place(x=230, y=40)

        self.heading = Label(self.top_frame, text='My People', font='arial 15 bold', bg='#f5f5f5')
        self.heading.place(x=320, y=60)

        # creating bottom frame #f5d9ff #ebedff
        self.bottom_frame = Frame(self, height=500, bg='#f5d9ff')
        self.bottom_frame.pack(fill=X)

        # name
        self.name_label = Label(self.bottom_frame, text='Name', bg='#8b4da1', fg='white', width=8, font='arial 10 bold')
        self.name_label.place(x=150, y=40)
        self.name_entry = Entry(self.bottom_frame, width=40, borderwidth= 2, relief="sunken", font='arial 10')
        self.name_entry.insert(0, ' Enter your name')
        self.name_entry.place(x=250, y=40)
        # email
        self.email_label = Label(self.bottom_frame, text='Email', bg='#8b4da1', fg='white', width=8, font='arial 10 bold')
        self.email_label.place(x=150, y=80)
        self.email_entry = Entry(self.bottom_frame, width=40, borderwidth= 2, relief="sunken", font='arial 10')
        self.email_entry.insert(0, ' Enter your email')
        self.email_entry.place(x=250, y=80)

        # number
        self.number_label = Label(self.bottom_frame, text='Number', bg='#8b4da1', fg='white', width=8, font='arial 10 bold')
        self.number_label.place(x=150, y=120)
        self.number_entry = Entry(self.bottom_frame, width=40, borderwidth= 2, relief="sunken", font='arial 10')
        self.number_entry.insert(0, ' Enter your number')
        self.number_entry.place(x=250, y=120)

        # adress
        self.address_label = Label(self.bottom_frame, text='Address', bg='#8b4da1', fg='white', width=8, font='arial 10 bold')
        self.address_label.place(x=150, y=160)
        self.address_entry = Entry(self.bottom_frame, width=40, borderwidth= 2, relief="sunken", font='arial 10')
        self.address_entry.insert(0, ' Enter your address')
        self.address_entry.place(x=250, y=160)

        # ok button
        self.add_button = Button(self.bottom_frame, width=15, text='Add', font='arial 10 bold', bg='#8b4da1', fg='white',
                                  borderwidth= 2, relief="raised", command=self.add_person)
        self.add_button.place(x=280, y=210)

    def add_person(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        number = self.number_entry.get()
        address = self.address_entry.get()

        if name != "" and email != "" and number != "" and address !="":
            try:
                query = "INSERT INTO MyPeople (Name, Email, Number, Address) VALUES (?,?,?,?)"
                cursor.execute(query, (name, email, number, address))
                connection.commit()
                messagebox.showinfo('Success', f"{name}'s contact is added.")
            except Exception as e:
                messagebox.showerror('Error', str(e), icon='warning')
        else:
            messagebox.showerror('Error', 'Fill all the feilds', icon='warning')

        self.mainloop()
if __name__ == '__main__':
    AddPeople()