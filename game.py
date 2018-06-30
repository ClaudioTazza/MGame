import curses
from wallet import *
from dealers import *

stdscr = curses.initscr()   #Restituisce lo standard screen

curses.curs_set(0)          
curses.noecho()

#Setta quante righe e quante colonne ha il terminale in uso
(ROWS, COLS) = stdscr.getmaxyx()

wallet = wallet()
dealers = Dealers()

c = ' '
while c != ord('0'):
    stdscr.addstr(4, 1, "Soldi : " + str( wallet.getMoney() ))
    stdscr.refresh()
  
    wallet.addMoney(10)
    c = stdscr.getch()

curses.endwin()

