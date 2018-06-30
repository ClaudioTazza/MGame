from time import sleep
from wallet import *
import curses
    
class Dealers():
    def __init__(self, Dealers=0):
        self.nDealers = Dealers 

    # Aumenta di n il numero dei trafficanti
    def addDealers(self,num):
        self.nDealers += num
    
    # Ritorna il numero di trafficanti
    def getDealers():
        return nDealers
        
    # Modifica il numero dei trafficanti
    def setDealers(self, num):
        self.nDealers = num
    
    # Mette a lavorare i trafficanti
    def makeMoney(self, wallet):
        wallet.addMoney(20 * nDealers)



if __name__ == "__main__":
    stdscr = curses.initscr()
    
    wallet = wallet() 
    dealers = Dealers()
    dealers.setDealers(1)
    

    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
