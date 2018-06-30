from threading import Thread
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
methLab = methLab(0, 1)

p = Thread(target=methLab.makeMeth)
p.start()

while True: 
    stdscr.addstr(4, 1, "Soldi: " + str( wallet.getMoney() ))
    stdscr.addstr(6, 1, "Trafficanti: " + str( dealers.getDealers() ))
    stdscr.addstr(8, 1, "Meth : " + str( methLab.getMeth() ))
    stdscr.addstr(10, 1, "Cuochi : " + str( methLab.getCooks() ))
  
    stdscr.refresh()

curses.endwin()

