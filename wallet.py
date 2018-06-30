class wallet():
    def __init__(self):
        self.money = 0
    
    # Ritorna la quantita' di denaro in possesso
    def getMoney(self):
        return self.money

    # Aggiunge n 'soldi' al portafoglio
    def addMoney(self, num):
        self.money += num

    
