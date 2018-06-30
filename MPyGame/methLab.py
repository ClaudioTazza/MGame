class MethLab():
    def __init__(self, meth=0., cooks=0):
        self.meth = meth
        self.cooks = cooks

    def addMeth(self, num):
        self.meth += float(num)

    def makeMeth(self, FPS):
        self.addMeth(5. * self.cooks / float(FPS))
