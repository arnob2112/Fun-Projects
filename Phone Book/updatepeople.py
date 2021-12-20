from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("mypeopledatabase")
cursor = connection.cursor()

class UpdatePeople(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)
        self.person_id = person_id
        self.person = cursor.execute("SELECT * FROM MyPeople WHERE ID = '{}'".format(person_id)).fetchone()
        self.geometry("650x550+350+150")
        self.title("Update Person")
        self.resizable(False, False)

        # creating top frame
        self.top_frame = Frame(self, height=150, bg='#f5f5f5')
        self.top_frame.pack(fill=X)

        self.top_image = PhotoImage(file='icons/person.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg='#f5f5f5')
        self.top_image_label.place(x=230, y=40)

        self.heading = Label(self.top_frame, text='Update Person', font='arial 15 bold', bg='#f5f5f5')
        self.heading.place(x=320, y=60)

        # creating bottom frame
        self.bottom_frame = Frame(self, height=500, bg='#f5d9ff')
        self.bottom_frame.pack(fill=X)

        # name
        self.name_label = Label(self.bottom_frame, text='Name', bg='#8b4da1', fg='white', width=8, font='arial 10 bold')
        self.name_label.place(x=150, y=40)
        self.name_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.name_entry.insert(0, self.person[1])
        self.name_entry.place(x=250, y=40)
        # email
        self.email_label = Label(self.bottom_frame, text='Email', bg='#8b4da1', fg='white', width=8,
                                 font='arial 10 bold')
        self.email_label.place(x=150, y=80)
        self.email_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.email_entry.insert(0, self.person[2])
        self.email_entry.place(x=250, y=80)

        # number
        self.number_label = Label(self.bottom_frame, text='Number', bg='#8b4da1', fg='white', width=8,
                                  font='arial 10 bold')
        self.number_label.place(x=150, y=120)
        self.number_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.number_entry.insert(0, self.person[3])
        self.number_entry.place(x=250, y=120)

        # adress
        self.address_label = Label(self.bottom_frame, text='Address', bg='#8b4da1', fg='white', width=8,
                                   font='arial 10 bold')
        self.address_label.place(x=150, y=160)
        self.address_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.address_entry.insert(0, self.person[4])
        self.address_entry.place(x=250, y=160)

        # ok button
        self.add_button = Button(self.bottom_frame, width=15, text='Update', font='arial 10 bold', bg='#8b4da1',
                                 fg='white',
                                 borderwidth=2, relief="raised", command=self.update_people)
        self.add_button.place(x=280, y=210)

    def update_people(self):
        id = self.person_id
        name = self.name_entry.get()
        email = self.email_entry.get()
        number = self.number_entry.get()
        address = self.address_entry.get()

        if name != "" and email != "" and number != "" and address != "":
            try:
                query = "UPDATE MyPeople SET Name = :name, Email = :email, Number = :number, Address = :address WHERE ID = :id"
                cursor.execute(query, {'name': name, 'email': email, 'number': number, 'address': address, 'id':id})
                connection.commit()
                messagebox.showinfo('Success', f"{name}'s contant is updated.")
            except Exception as e:
                messagebox.showerror('Error', str(e), icon='warning')
        else:
            messagebox.showerror('Error', 'Fill all the feilds', icon='warning')

        self.mainloop()

