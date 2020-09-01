import random
import tkinter as tk

window = tk.Tk()
window.geometry("402x350")
window.title("Rock Paper and Scissors")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_number(choice):
    the_choice = {'rock' : 0, 'paper' : 1, 'scissors' :2}
    return the_choice[choice]

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def gameplay(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_number(human_choice)
    comp = choice_number(comp_choice)
    if(user == comp):
        print('Tie')
        answer = f"TIE !!!\nYou choosed {USER_CHOICE}\nComputer choosed {COMP_CHOICE}\nYour score {USER_SCORE}. Computer score {COMP_SCORE}"
    elif ((user - comp) % 3 == 1):
        print('You win')
        USER_SCORE += 1
        answer = f"You win !\nYou choosed {USER_CHOICE}\nComputer choosed {COMP_CHOICE}\nYour score {USER_SCORE}. Computer score {COMP_SCORE}"
    else:
        print('Computer wins')
        COMP_SCORE += 1
        answer = f"Computer wins !\nYou choosed {USER_CHOICE}\nComputer choosed {COMP_CHOICE}\nYour score {USER_SCORE}. Computer score {COMP_SCORE}"

    text_area = tk.Text(master=window, height = 5, width = 40, bg = "#FFFF99")
    text_area.grid(column = 0, row = 5)
    text_area.insert(tk.END, answer)

def Rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = computer_choice()
    gameplay(USER_CHOICE, COMP_CHOICE)

def Scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissors'
    COMP_CHOICE = computer_choice()
    gameplay(USER_CHOICE, COMP_CHOICE)

def Paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = computer_choice()
    gameplay(USER_CHOICE, COMP_CHOICE)

def Quit_game():
    window.destroy()

def Button():
    button1 = tk.Button(text="    Rock    ", bg="skyblue", command=Rock, width=20, height=2, activebackground='gray',
                        state='normal')
    button1.grid(column=0, row=1)
    button2 = tk.Button(text="    Paper   ", bg="pink", command=Paper, width=20, height=2, activebackground='gray',
                        state='normal')
    button2.grid(column=0, row=2)
    button3 = tk.Button(text="    Scissors    ", bg="lightgreen", command=Scissors, width=20, height=2,
                        activebackground='gray', state='normal')
    button3.grid(column=0, row=3)
    text_area = tk.Text(master=window, height=5, width=50, bg="#FFFF99")
    text_area.grid(column=0, row=4)
    welcome = f"Hey ! Welcome to the rock, scissors, paper game !\nthe game is easy and simple\nhope you like it !\nclick the button above to start the game\nGood Luck !"
    text_area.insert(tk.END, welcome)

    button4 = tk.Button(compound='left', text="Wanna exit? click here...", bg='wheat4', command=Quit_game, width =20, height=3,activebackground='gray')
    button4.grid(column = 0, row=6)



def start_the_game():
    start = tk.Button(text= 'Start The Game', bg = 'navajo white', command = lambda:[Button(), start.grid_forget()] , width=20, height=2, activebackground = 'gray', state='normal')
    start.grid(padx=120, pady=150)

start_the_game()




window.mainloop()
