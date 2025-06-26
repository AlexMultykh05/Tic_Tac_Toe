import random
from tkinter import *
from tkmacosx import Button


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == '' and check_winner() is False:
        if player == players[1]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=players[0] + "'s turn")

            elif check_winner() is True:
                label.config(text=players[1] + ' wins!!')
            elif check_winner() == 'Tie':
                label.config(text='Tie!')

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=players[1] + "'s turn")

            elif check_winner() is True:
                label.config(text=players[0] + ' wins!!')
            elif check_winner() == 'Tie':
                label.config(text='Tie!')


def free_place():
    places = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                places -= 1

    if places == 0:
        return False
    else:
        return True


def check_winner():
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg='lightgreen')
            buttons[1][column].config(bg='lightgreen')
            buttons[2][column].config(bg='lightgreen')
            return True

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg='lightgreen')
            buttons[row][1].config(bg='lightgreen')
            buttons[row][2].config(bg='lightgreen')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='lightgreen')
        buttons[1][1].config(bg='lightgreen')
        buttons[2][2].config(bg='lightgreen')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='lightgreen')
        buttons[1][1].config(bg='lightgreen')
        buttons[2][0].config(bg='lightgreen')
        return True

    elif free_place() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return 'Tie'

    else:
        return False


def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + "'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg='#F0F0F0')


window = Tk()
window.title('TicTacToe')
window.minsize(400, 400)
window.maxsize(400, 400)

players = ['X', 'O']

player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + "'s turn", font=('Comfortaa', 40))
label.pack(side='top')

restart_button = Button(text='Restart', font=('Comfortaa', 20), command=new_game, bg='lightblue', fg='white')
restart_button.pack(side='top')

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', font=('Comfortaa', 40), width=100, height=100,
                                      command=lambda row=row, column=column: next_turn(row, column))

        buttons[row][column].grid(row=row, column=column)

if __name__ == '__main__':
    window.mainloop()
