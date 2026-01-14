import random
from tkinter import *

root = Tk()

#------------MAIN WINDOW------------
root.geometry("500x500")
root.resizable(width = False, height = False)
root['bg'] = '#D297FF'


#------------MAIN FUNCTION------------
def game():
    label_start.pack_forget()
    btn_start.pack_forget()
    attempts = 0
    first_number = 0
    last_number = None
    print(attempts)

#------------MAIN MENU GUI------------
label_start = Label(root, text="Welcome to the game ‘Guess a Number’", bg="#FF7C7C", font='Verdana, 15')
btn_start = Button(root, text="Start game", command=lambda: game(), font='Verdana, 12', bg='#6AE1A9')
btn_close = Button(root,text="Close game", command=lambda: quit(), font='Verdana, 12', bg='#6AE1A9' )

label_start.pack(pady=40)
btn_start.pack(pady=70)
btn_close.pack()


root.mainloop()
