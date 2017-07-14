from Computador.Memoria import Memoria
from Computador.Registradores import Registradores
from Computador.UnidadeControle import UnidadeControle
from Computador.PC import PC

class Processador():
    def __init__(self):
        self.registradores = Registradores()
        self.memoria = Memoria()
        self.unidadeControle = UnidadeControle()
        self.PC = PC()

    def setRegistrador(self, nome, value):
        self.registradores.setRegistrador(nome , value)

    def setRegistradorPorNome(self, nome, value):
        self.registradores.setRegistradorPorNome(nome , value)

    def getRegistradores(self):
        return self.registradores.getRegistradores()

    def getValorRegistrador(self, nome):
        return self.registradores.getValorRegistrador(nome)

    def getValorRegistradorPorNome(self, nome):
        return self.registradores.getValorRegistradorPorNome(nome)

    def setPalavra(self, palavras):
        self.memoria.setPalavras(palavras)

    def setLabel(self, label):
        self.memoria.setLabel(label)

    def getLabel(self, nome):
        return self.memoria.getLabel(nome)

    def setPC(self, index):
        self.PC.setPC(index)


    def nextStep(self):
        i = 0
        while self.PC.getPC() < self.memoria.getQuantPalavras():
            self.unidadeControle.recebePalavra(self.memoria.getPalavra(self.PC.getPC()), self)
            i = i = self.PC.getPC() + 1
            self.PC.setPC(i)