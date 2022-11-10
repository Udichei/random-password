import random
import tkinter as tk

root = tk.Tk()
chars = ('+-/*!$@?=<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')


#the function generates a random password depending on the entered length
def get_password():
    lenght = int(myentry.get())
    password['text'] = ''

    for i in range(lenght):
        password['text'] += random.choice(chars)

#Main window settings
root.title('Randomizer')
root.geometry('500x200')
root.resizable(width=True, height=False)
root.configure(bg='#000000')

title = tk.Label(root, text='Enter password length', font=("Terminal", 20), height=2, fg='#FFBF00', bg='#000000')
title.pack()

myentry = tk.Entry(root, font=("Terminal", 20), fg='#FFBF00', bg='#000000', borderwidth=0, justify='center')
myentry.pack()

btn = tk.Button(root, text='randomize', command=get_password, font=("Terminal", 20), height=1, fg='#FFBF00', bg='#000000', highlightcolor='#FFBF00', highlightbackground='#000000', borderwidth=-1)
btn.pack()

password = tk.Label(root, text='', font=("Terminal", 20), height=1, fg='#FFBF00', bg='#000000')
password.pack()

root.mainloop()
