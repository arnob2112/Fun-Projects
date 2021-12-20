from tkinter import *
import sqlite3
from addpeople import AddPeople
from updatepeople import UpdatePeople
from displayperson import DisplayPerson
from tkinter import messagebox

connection = sqlite3.connect("mypeopledatabase")
cursor = connection.cursor()
class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+350+150")
        self.title("My People")
        self.resizable(False, False)

        # creating top frame
        self.top_frame = Frame(self, height=150, bg='#f5f5f5')
        self.top_frame.pack(fill=X)

        self.top_image = PhotoImage(file='icons/people.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image)
        self.top_image_label.place(x=230, y=40)

        self.heading = Label(self.top_frame, text='My People', font='arial 15 bold', bg='#f5f5f5')
        self.heading.place(x=320, y=60)

        # creating bottom frame
        self.bottom_frame = Frame(self, height=500, bg='#99f2f1')
        self.bottom_frame.pack(fill=X)

        # creating scroll bar
        self.ver_scrollbar = Scrollbar(self.bottom_frame, orient=VERTICAL)

        # creating listbox
        self.list_box = Listbox(self.bottom_frame, width=70, height=25, bg='white')
        self.list_box.grid(row=0, column=0, padx=(40,0))
        self.list_box.config(yscrollcommand=self.ver_scrollbar.set)

        persons = cursor.execute("SELECT * FROM MyPeople").fetchall()
        count = 0
        for person in persons:
            self.list_box.insert(count, f" {person[0]}.   {person[1]}    {person[3]}")
            count += 1

        self.ver_scrollbar.config(command=self.list_box.yview)
        self.ver_scrollbar.grid(row=0, column=1, sticky= N+S)

        # creating buttons
        add_button = Button(self.bottom_frame, width=15, text='Add', font='arial 10 bold', bg='#99f2f1',
                                  borderwidth= 2, relief="ridge", command=self.add_people)
        add_button.grid(row=0, column=2, padx=20, pady=15, sticky=N)

        update_button = Button(self.bottom_frame, width=15, text='Update', font='arial 10 bold', bg='#99f2f1',
                                  borderwidth= 2, relief="ridge", command=self.update_person)
        update_button.grid(row=0, column=2, padx=20, pady=55, sticky=N)

        display_button = Button(self.bottom_frame, width=15, text='Display', font='arial 10 bold', bg='#99f2f1',
                                  borderwidth= 2, relief="ridge", command=self.display_person)
        display_button.grid(row=0, column=2, padx=20, pady=95, sticky=N)

        delete_button = Button(self.bottom_frame, width=15, text='Delete', font='arial 10 bold', bg='#99f2f1',
                                  borderwidth= 2, relief="ridge", command=self.delete_person)
        delete_button.grid(row=0, column=2, padx=20, pady=135, sticky=N)

        self.mainloop()

    def add_people(self):
        add_people = AddPeople()
        self.destroy()

    def update_person(self):
        try:
            person = self.list_box.get(self.list_box.curselection())
            person_id = person.split(". ")[0]

            update_window = UpdatePeople(person_id)
        except:
            messagebox.showerror('Error', 'Please select a contact first!')

    def display_person(self):
        try:
            person = self.list_box.get(self.list_box.curselection())
            person_id = person.split(". ")[0]

            display_window = DisplayPerson(person_id)
        except:
            messagebox.showerror('Error', 'Please select a contact first!')

    def delete_person(self):
        try:
            person = self.list_box.get(self.list_box.curselection())
            person_id = person.split(". ")[0]
            person_name = cursor.execute("SELECT Name FROM MyPeople WHERE ID = :id", {'id': person_id}).fetchone()

            query = "DELETE FROM MyPeople WHERE ID = :id"
            answer = messagebox.askquestion('Warning', f"Are you sure to delete {person_name[0]}?")
            if answer == 'yes':
                try:
                    cursor.execute(query, {'id': person_id})
                    connection.commit()
                    messagebox.showinfo('Success', f"{person_name[0]}'s contact has deleted.")
                    self.destroy()
                except Exception as e:
                    messagebox.showerror('Error', str(e), icon='warning')
        except:
            messagebox.showerror('Error', 'Please select a contact first!')

if __name__ == '__main__':
    MyPeople()