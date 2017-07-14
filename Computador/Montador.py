import re
from Enums.TipoI import TipoI
from Enums.TipoR import TipoR
from Computador.Registradores import Registradores

class Montador():
    def __init__(self, palavras, registradores):
        self.palavras = palavras
        self.registradores = Registradores()
        self.palavrasMontadas = []
        self.labels = []
        self.tokenizer()
        self.montar()

    def tokenizer(self):
        result = self.palavras.split("\n")

        self.palavras = []

        pattern = re.compile(r'''(?x)
                (?:[A-Z]\.)+        
              | \w+(?:-\w+)*        
              | \$?\d+(?:\.\d+)?%?  
              | \.\.\.              
              | [][.;"'?()_`-]''')

        for palavra in result:
            results = re.findall(pattern, palavra)
            self.palavras.append(results)

        del(self.palavras[len(self.palavras) - 1])

    def montar(self):
        endereco = 0
        for palavra in self.palavras:
            string = []

            if len(palavra) < 2:
                string.append(palavra[0])
                string.append(str(endereco - 1))
                self.labels.append(string)

            elif palavra[0] == 'li':
                string.append(str(bin(TipoI.li.value)))
                string.append('00000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[2])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'bne':
                print("OI")
                string.append(str(bin(TipoI.bne.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('0000000000000000')
                string.append(palavra[3])
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'add':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.add.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'addu':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.addu.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'sub':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.sub.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'subu':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.subu.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'mult':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('00000')
                string.append('00000')
                string.append(str(bin(TipoR.mult.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'multu':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('00000')
                string.append('00000')
                string.append(str(bin(TipoR.multu.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'div':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('00000')
                string.append('00000')
                string.append(str(bin(TipoR.div.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'divu':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('00000')
                string.append('00000')
                string.append(str(bin(TipoR.divu.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'slt':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.slt.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'sltu':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.sltu.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'mflo':
                string.append('000000')
                string.append('000000')
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.mflo.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'mtlo':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append('00000')
                string.append('00000')
                string.append(str(bin(TipoR.mtlo.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'mfhi':
                string.append('000000')
                string.append('000000')
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.mfhi.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'mthi':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append('00000')
                string.append('00000')
                string.append(str(bin(TipoR.mthi.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'and':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.andd.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'or':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.orr.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'nor':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.nor.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'xor':
                string.append('000000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append(str(bin(TipoR.xor.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

    def getPalavrasMontadas(self):
        return self.palavrasMontadas

    def getLabels(self):
        return self.labels
