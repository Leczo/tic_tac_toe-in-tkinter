from tkinter import *
from winner_check import is_winner, restart
import sys
import os

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

winner = False
moves = 0


def callback(index, position):
    global moves
    global winner
    global buttons

    if winner == True:
        return None
    else:
        if buttons[index]['text'] == ' ' and moves % 2 == 0:

            moves += 1
            theBoard[position] = 'X'
            buttons[index].config(text=theBoard[position])
            label['text'] = 'Player O move'

        elif buttons[index]['text'] == ' ':
            moves += 1
            theBoard[position] = 'O'
            buttons[index].config(text=theBoard[position])
            label['text'] = 'Player X move'

        if is_winner(theBoard):
            winner = True
            if moves % 2 != 0:
                label['text'] = 'Player X is winner'
            else:
                label['text'] = 'Player O is winner'
            # disabling all game buttons
            for i in buttons:
                i.config(state='disabled')
        # Draw
        if moves == 9:
            for i in buttons:
                i.config(state='disabled')
                label['text'] = 'Draw'


#
    label_moves['text'] = 'Number of moves: ' + str(moves)


root = Tk()
frame = Frame(root)
frame.grid()


labeltext = 'Player X move'
label = Label(frame, text=labeltext)
label.grid(row=0, column=3)

# label with number of moves
label_tmoves = 'Number of moves: ' + str(moves)
label_moves = Label(frame, text=label_tmoves)
label_moves.grid(row=1, column=3)

# restarting game
restart_button = Button(root, text="Restart", command=restart)
restart_button.grid(row=9, column=2)

# Setting 9 buttons, Text in the button is taken from board
pos = ['top-L', 'top-M', 'top-R',
       'mid-L', 'mid-M', 'mid-R',
       'low-L', 'low-M', 'low-R']
buttons = []
for index in range(9):

    # text in button is taken from the board
    button = Button(root, text=theBoard[pos[index]], width=15, height=5,
                    command=lambda index=index: callback(index, pos[index]))

    if index in [0, 3, 6]:
        direction = 'W'
    if index in [1, 4, 7]:
        direction = 'N'
    else:
        direction = 'E'

    # adding button to frame
    button.grid(padx=1, pady=1, row=int(index % 3),
                column=int(index/3)+1, sticky=direction)

    # appending button to list
    buttons.append(button)

root.mainloop()
