import time
import curses

class methLab():
   def __init__(self, meth=0, cooks=0):
     self.meth = meth 
     self.cooks = cooks 
    
   # Aggiunge n grammi di meth
   def addMeth(self, num):
       self.meth += num

   # Ritorna il numero di g di Meth in laboratorio
   def getMeth(self):
       return self.meth

   # Ritorna il numero di cuochi
   def getCooks(self):
       return self.cooks

   # Reimposta il numero di cuochi
   def setCooks(self, num):
       self.cooks = num

   # Reimposta il numero di g di meth
   def setMeth(self, num):
       self.meth = num

   # Avvia la produzione di meth 
   def makeMeth(self):
       while True:
         self.meth = self.addMeth(5 * self.cooks)
         time.sleep(1)
         print ("hai " + str(self.meth) + " g di meth\n")

if __name__ == "__main__":
    methLab = methLab()
    methLab.makeMeth()
