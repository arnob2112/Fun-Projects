from tkinter import *
from tkinter import font

root = Tk()
root.title("Calculator")
root.geometry("350x350+600+100")
root.resizable(FALSE,FALSE)

def number_entry(x):
    if x == '.' and entrybox.get()[-1] == '.':
        pass
    elif entrybox.get() == "0":
        if x == '.':
            entrybox.insert(1, '.')
        else:
            entrybox.delete(0, END)
            entrybox.insert(0, str(x))
    else:
        length = len(entrybox.get())
        entrybox.insert(length, str(x))

def operator_entry(x):
    if entrybox.get() != "0":
        last_char = entrybox.get()[-1]
        if last_char in ['+', '-', '/'] or entrybox.get()[-2:] == '**':
            pass
        else:
            length = len(entrybox.get())
            entrybox.insert(length, button_operator[x]['text'])

def clear_it():
    entrybox.delete(0, END)
    entrybox.insert(0, 0)

def delete_it():
    length = len(entrybox.get()) - 1
    entrybox.delete(length, END)
    if length == 0:
        entrybox.insert(0, 0)

history = []
def calculate():
    expresion = entrybox.get()
    result = eval(expresion)
    entrybox.delete(0, END)
    entrybox.insert(0, result)
    history.append(f"{expresion} = {result}")
    history.reverse()
    history_bar.configure(text='History: ' + ' | '.join(history[:4]), font='verdana 8 bold')


# creating entrybox
entrybox = Entry(font='verdana 14 bold', width=20, bd=6, justify=RIGHT)
entrybox.insert(0, "0")
entrybox.place(x=35, y=10)

# creating number buttons
button_num = []
for a in range(10):
    button_num.append(Button(width=4, text=str(a), bd=6, command= lambda x = a: number_entry(x)))

zero_button = Button(width=4, text='0', bd=6, command=lambda x=0: number_entry(x))
zero_button.place(x=230, y=70)

dot_button = Button(width=4, text='.', font='Axiata 9 bold', bd=6, command=lambda x = '.': number_entry(x))
dot_button.place(x=230, y=117)


button_text = 1
for a in range(3):
    for b in range(3):
        button_num[button_text].place(x=30 + b*70, y=70 + a*70)
        button_text +=  1

# creating operator buttons
button_operator = []
for a in range(4):
    button_operator.append(Button(width=3, font='times 11 bold', bd=4, command= lambda x = a: operator_entry(x)))

button_operator[0]['text'] = "+"
button_operator[1]['text'] = "-"
button_operator[2]['text'] = "*"
button_operator[3]['text'] = "/"

for a in range(4):
    button_operator[a].place(x=290, y=70 + a*47)

clear_button = Button(width=4, text='C',font='times 9 bold', bd=6, command=clear_it)
clear_button.place(x=230, y=164)

equal_button = Button(width=12, text='=',font='times 9 bold', bd=6, command=calculate)
equal_button.place(x=230, y=258)

delete_button = Button(width=4, text='Del', font='times 9 bold',bd=6, command=delete_it)
delete_button.place(x=230, y=211)

history_bar = Label(root, text='History: ', relief=SUNKEN, height=2, anchor=W, font='Verdana 8 bold')
history_bar.pack(side=BOTTOM, fill=X)

root.mainloop()