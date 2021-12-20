from tkinter import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from about_us import AboutUs

date = str(datetime.datetime.now().date())

class PhoneBook(object):
    def __init__(self, window):
        self.window = window
        self.window.title('PhoneBook')

        # top frame
        self.top_frame = Frame(self.window, height=150, bg='#f5f5f5')
        self.top_frame.pack(fill=X)

        self.top_image = PhotoImage(file='phonebook.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image)
        self.top_image_label.place(x=180, y=40)

        self.heading = Label(self.top_frame, text='My Phonebook App', font='arial 15 bold', bg='#f5f5f5')
        self.heading.place(x=270, y=60)

        self.date_label = Label(self.top_frame, text="Today's date:  " + date, font='arial 10 bold', fg='#878787', bg='#f5f5f5')
        self.date_label.place(x=470, y=120)

        # bottom frame
        self.bottom_frame = Frame(self.window, height=500, bg='#b1f0e9')
        self.bottom_frame.pack(fill=X)

        # view button
        self.my_people_button = Button(self.bottom_frame,width=15, text='My People', font='arial 10 bold', bg='#b1f0e9',
                                  borderwidth= 2, relief="groove", command=self.my_people)
        self.my_people_button.place(x=250, y=70)
        # add people button
        self.add_button = Button(self.bottom_frame,width=15, text='Add People', font='arial 10 bold', bg='#b1f0e9',
                                  borderwidth= 2, relief="groove", command=self.add_people)
        self.add_button.place(x=250, y=130)

        # about us button
        self.about_button = Button(self.bottom_frame, width=15, text='About us', font='arial 10 bold', bg='#b1f0e9',
                                  borderwidth= 2, relief="groove", command=self.about_us)
        self.about_button.place(x=250, y=190)

    def my_people(self):
        people = MyPeople()

    def add_people(self):
        add_people = AddPeople()

    def about_us(self):
        about_window = AboutUs()

def main():
    root = Tk()
    phonebook = PhoneBook(root)
    root.geometry("650x550+350+150")
    root.resizable(False, False)
    mainloop()

if __name__ == '__main__':
    main()