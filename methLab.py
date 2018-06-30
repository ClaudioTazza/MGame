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
       self.meth = addMeth(5 * self.cooks)
