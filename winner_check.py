
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
