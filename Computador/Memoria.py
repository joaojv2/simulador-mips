class Memoria():
    def __init__(self):
        self.palavras = []
        self.labels = []
        self.memoria = []

    def setPalavras(self, palavras):
        self.palavras = palavras
        self.memoria.append(self.palavras)

    def setLabel(self, label):
        self.labels = label
        self.memoria.append(self.labels)


    def getPalavra(self, index):
        return self.palavras[index]

    def getLabel(self, nome):
        for label in self.labels:
            if label[0] == nome:
                return label[1]

    def getQuantPalavras(self):
        return len(self.palavras)