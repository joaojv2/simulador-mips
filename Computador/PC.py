class PC():
    def __init__(self):
        self.pc = 0

    def setPC(self, index):
        self.pc = int(index)

    def getPC(self):
        return self.pc

    def acrescentarPC(self):
        self.pc += 1