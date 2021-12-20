from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("mypeopledatabase")
cursor = connection.cursor()

class DisplayPerson(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)
        self.person_id = person_id
        self.person = cursor.execute("SELECT * FROM MyPeople WHERE ID = '{}'".format(person_id)).fetchone()
        self.geometry("650x550+350+150")
        self.title("Display Person")
        self.resizable(False, False)

        # creating top frame
        self.top_frame = Frame(self, height=150, bg='#f5f5f5')
        self.top_frame.pack(fill=X)

        self.top_image = PhotoImage(file='icons/person.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg='#f5f5f5')
        self.top_image_label.place(x=210, y=40)

        self.heading = Label(self.top_frame, text='Person Details', font='arial 15 bold', bg='#f5f5f5')
        self.heading.place(x=300, y=60)

        # creating bottom frame
        self.bottom_frame = Frame(self, height=500, bg='#ebedff')
        self.bottom_frame.pack(fill=X)

        # name
        self.name_label = Label(self.bottom_frame, text='Name', bg='#6b72b3', fg='white', width=8, font='arial 10 bold')
        self.name_label.place(x=150, y=80)
        self.name_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.name_entry.insert(0, self.person[1])
        self.name_entry.config(state='disable')
        self.name_entry.place(x=250, y=80)
        # email
        self.email_label = Label(self.bottom_frame, text='Email', bg='#6b72b3', fg='white', width=8,
                                 font='arial 10 bold')
        self.email_label.place(x=150, y=120)
        self.email_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.email_entry.insert(0, self.person[2])
        self.email_entry.config(state='disable')
        self.email_entry.place(x=250, y=120)

        # number
        self.number_label = Label(self.bottom_frame, text='Number', bg='#6b72b3', fg='white', width=8,
                                  font='arial 10 bold')
        self.number_label.place(x=150, y=160)
        self.number_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.number_entry.insert(0, self.person[3])
        self.number_entry.config(state='disable')
        self.number_entry.place(x=250, y=160)

        # adress
        self.address_label = Label(self.bottom_frame, text='Address', bg='#6b72b3', fg='white', width=8,
                                   font='arial 10 bold')
        self.address_label.place(x=150, y=200)
        self.address_entry = Entry(self.bottom_frame, width=40, borderwidth=2, relief="sunken", font='arial 10')
        self.address_entry.insert(0, self.person[4])
        self.address_entry.config(state='disable')
        self.address_entry.place(x=250, y=200)

        self.mainloop()

