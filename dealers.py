from time import sleep
from wallet import *
import curses
    
class Dealers():
    def __init__(self):
        self.nDealers= 0

    def addDealers(self,num):
        self.nDealers += num
    
    def getDealers():
        return nDealers
        
    def setDealers(self, num):
        self.nDealers = num

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
