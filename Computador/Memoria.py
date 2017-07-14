class Memoria():
    def __init__(self):
        self.palavras = []
        self.labels = []

    def setPalavras(self, palavras):
        self.palavras = palavras

    def setLabel(self, label):
        self.labels = label
        for label in self.labels:
            print(label[0])

    def getPalavra(self, index):
        return self.palavras[index]

    def getLabel(self, nome):
        for label in self.labels:
            if label[0] == nome:
                return label[1]

    def getQuantPalavras(self):
        return len(self.palavras)