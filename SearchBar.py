from tkinter import *
import wikipedia


def search_it():
    value = search_entry.get()
    result.delete(1.0, END)
    try:
        answer = wikipedia.summary(value)
        result.insert(INSERT, answer)
    except:
        result.insert(INSERT, "Please check your input or internet connection and try again.")


root = Tk()
# creating top frame
top_frame = Frame(root)

search_entry = Entry(top_frame)
search_entry.pack()

search_button = Button(top_frame, text="Search", command=search_it)
search_button.pack()

top_frame.pack(side=TOP)

# creating bottom frame
bottom_frame = Frame(root)

# creating scrollbar
scroll = Scrollbar(bottom_frame)
scroll.pack(side=RIGHT, fill=Y)

result = Text(bottom_frame, width=30, height=10, yscrollcommand=scroll.set, wrap=WORD)
result.pack()
scroll.config(command=result.yview)
bottom_frame.pack(side=BOTTOM)
root.mainloop()