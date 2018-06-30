import curses
from wallet import *
from dealers import *
from methLab import *

stdscr = curses.initscr()   #Restituisce lo standard screen

curses.curs_set(0)          
curses.noecho()

#Setta quante righe e quante colonne ha il terminale in uso
(ROWS, COLS) = stdscr.getmaxyx()

wallet = wallet()
dealers = Dealers()
methLab = methLab(0, 0)

c = ' '
while c != ord('0'):
    stdscr.addstr(4, 1, "Soldi : " + str( wallet.getMoney() ))
    stdscr.addstr(4, 1, "Soldi : " + str( wallet.getMoney() ))
    stdscr.addstr(4, 1, "Soldi : " + str( wallet.getMoney() ))
    stdscr.addstr(4, 1, "Soldi : " + str( wallet.getMoney() ))
  
    stdscr.refresh()
    c = stdscr.getch()

curses.endwin()

