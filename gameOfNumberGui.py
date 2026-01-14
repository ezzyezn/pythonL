import random
from tkinter import *

root = Tk()

#------------BASIC STATS------------
class Stats:
    def __init__(self):
        self.attempts = 0
        self.first_number = 0
        self.last_number = 100
    def restart(self):
        self.attempts = 0
        self.first_number = 0
        self.last_number = 100
stats = Stats()

class GuiHuman:
    def __init__(self):
        self.label = Label(root, text="Think of number from 0 to 100",
                           bg="#FF7C7C", font=('Verdana',15))
gui_human = GuiHuman()
class GameButtons:
    def __init__(self):
        self.response = None

        self.btn_more = Button(root, text="More",
                             font=('Verdana', 12), bg='#6AE1A9',command=lambda: self.more())
        self.btn_less = Button(root, text="Less",
                             font=('Verdana', 12), bg='#6AE1A9',command=lambda: self.less())
        self.btn_correct = Button(root, text="Correct",
                             font=('Verdana', 12), bg='#6AE1A9',command=lambda: self.correct())
    def more(self):
        self.response = ">"
        human_step()
    def less(self):
        self.response = "<"
        human_step()
    def correct(self):
        self.response = "="
gameBtn = GameButtons()
class HumanWin:
    def __init__(self):
        self.label = Label(root, text=f"Computer guessed, your number is a {computer_number} \n Attempts were used: {attempts}",
                     bg="#FF7C7C", font=('Verdana',12))
#------------MAIN WINDOW------------
root.geometry("500x500")
root.resizable(width = False, height = False)
root['bg'] = '#D297FF'

#------------GAME GUI------------
label_choose = Label(root, text="Choose gamemode 'you' or 'computer' think of number",
                     bg="#FF7C7C", font=('Verdana',12))
btn_human_choose = Button(root, text="You", font=('Verdana', 12),
                           bg='#6AE1A9',command=lambda: game_human())
btn_computer_choose = Button(root, text="Computer",
                             font=('Verdana', 12), bg='#6AE1A9',command=lambda: game_computer())

#------------CHOSE FUNCTION------------
def choose():

    label_start.pack_forget()
    btn_start.pack_forget()
    btn_close.pack_forget()


    label_choose.pack(pady=40)
    btn_human_choose.pack(pady=70)
    btn_computer_choose.pack()

#------------GAME OF HUMAN------------

def human_step(): 
    if stats.first_number <= stats.last_number:
        stats.attempts += 1
        computer_number = (stats.first_number + stats.last_number) // 2

        gui_human.label.config(text=f"Computer thinks: {computer_number}")

        gameBtn.btn_more.pack(pady=10)
        gameBtn.btn_less.pack(pady=10)
        gameBtn.btn_correct.pack(pady=10)

        if gameBtn.response is None:
            return

        if gameBtn.response == ">":
            stats.first_number = computer_number + 1
        elif gameBtn.response == "<":
            stats.last_number = computer_number - 1
        elif gameBtn.response == "=":
            wins()
        gameBtn.response = None
        human_step()
    else:
        print("you stupid")
def game_human():

    label_choose.pack_forget()
    btn_computer_choose.pack_forget()
    btn_human_choose.pack_forget()

    gui_human.label.pack(pady=40)
    root.after(2000, human_step)


#------------MAIN MENU GUI------------
label_start = Label(root, text="Welcome to the game ‘Guess a Number’",
                    bg="#FF7C7C", font=('Verdana',15))
btn_start = Button(root, text="Start game", command=lambda: choose(),
                    font=('Verdana', 12), bg='#6AE1A9')
btn_close = Button(root,text="Close game", command=lambda: quit(),
                    font=('Verdana', 12), bg='#6AE1A9' )

label_start.pack(pady=40)
btn_start.pack(pady=70)
btn_close.pack()


root.mainloop()
