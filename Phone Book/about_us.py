from tkinter import *

class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+150")
        self.title("About Us")
        self.resizable(False, False)

        # creating top frame
        self.top_frame = Frame(self, height=550, bg='#d1ffc9')
        self.top_frame.pack(fill=BOTH)

        self.heading = Label(self.top_frame, text='About Us', font='arial 17 bold', bg='#d1ffc9')
        self.heading.place(x=280, y=130)

        self.text = Label(self.top_frame, text="This application is made for all who don't want to remember contact information"
                                               "\nlike Albert Einstein. This application will be your daily partner and make"
                                               "\nyour life easier if you value it properly.I am always here to help you for any"
                                               "\nkind of problem which you are facing while using this. Also eagerly waiting for"
                                               "\nyour valuable feedback and I will update that upcoming version."
                                               "\n\n\n"
                                               "\nContact with me: "
                                               "\n\nFacebook: Md Ehshanul Haque"
                                               "\nInstagram: _arnob_12"
                                               "\nWhatsapp: 01769936762"
                                               "\n\n"
                                               "STAY TUNED.", font='arial 10 bold', bg='#d1ffc9')
        self.text.place(x=72, y=200)

        self.mainloop()

