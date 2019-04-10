
import sys
import os


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def is_winner(theBoard):
    win_comb = [('top-L', 'top-M', 'top-R'),
                ('mid-L', 'mid-M', 'mid-R'),
                ('low-L', 'low-M', 'low-R'),
                ('top-L', 'mid-L', 'low-L'),
                ('top-M', 'mid-M', 'low-M'),
                ('top-R', 'mid-R', 'low-R'),
                ('top-L', 'mid-M', 'low-R'),  # L-cross
                ('top-R', 'mid-M', 'low-L')]  # R-cross

    # checking if any X combination in theboard
    if any(theBoard[win_comb[i][0]] == 'X' and
           theBoard[win_comb[i][1]] == 'X' and
           theBoard[win_comb[i][2]] == 'X' for i in range(len(win_comb))):
        return True

    # checking if any O combination in theboard
    elif any(theBoard[win_comb[i][0]] == 'O' and
             theBoard[win_comb[i][1]] == 'O' and
             theBoard[win_comb[i][2]] == 'O' for i in range(len(win_comb))):
        return True

    else:
        return False


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
