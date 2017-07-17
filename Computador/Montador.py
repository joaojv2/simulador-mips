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
        self.vetores = []
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
              | [][.;"'?_`-]''')

        for palavra in result:
            results = re.findall(pattern, palavra)
            self.palavras.append(results)

        del(self.palavras[len(self.palavras) - 1])

    def montar(self):
        endereco = 0
        for palavra in self.palavras:
            string = []
            if palavra == None:
                continue
            if palavra[0] == 'syscall':
                string.append('000000')
                string.append('00000')
                string.append('00000')
                string.append('00000')
                string.append('00000')
                string.append('001100')
                self.palavrasMontadas.append(string)
                endereco += 1

            elif len(palavra) < 2:
                string.append(palavra[0])
                string.append(str(endereco - 1))
                self.labels.append(string)

            elif palavra[1] == '.' and palavra[2] == 'space':
                vetor = [x for x in range(int(int(palavra[3]) / 4))]
                self.vetores.append(vetor)

            elif palavra[0] == 'la':
                string.append(str(bin(TipoI.addi.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('0000000000000000')
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'sw':
                string.append(str(bin(TipoI.sw.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('0000000000000000')
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'addi':
                string.append(str(bin(TipoI.addi.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'addiu':
                string.append(str(bin(TipoI.addiu.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'slti':
                string.append(str(bin(TipoI.slti.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'sltiu':
                string.append(str(bin(TipoI.sltiu.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'andi':
                string.append(str(bin(TipoI.anddi.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'ori':
                string.append(str(bin(TipoI.ori.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'xori':
                string.append(str(bin(TipoI.xori.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'li':
                string.append(str(bin(TipoI.li.value)))
                string.append('00000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[2])))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'bne':
                string.append(str(bin(TipoI.bne.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('0000000000000000')
                string.append(palavra[3])
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'beq':
                string.append(str(bin(TipoI.beq.value)))
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

            elif palavra[0] == 'sll':
                string.append('000000')
                string.append('00000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                string.append(str(bin(TipoR.sll.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'srl':
                string.append('000000')
                string.append('00000')
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('{0:b}'.format(int(palavra[3])))
                string.append(str(bin(TipoR.srl.value)))
                self.palavrasMontadas.append(string)
                endereco += 1

            elif palavra[0] == 'mul':
                string.append(str(bin(TipoR.mul.value)))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[2]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[3]))))
                string.append('{0:b}'.format(int(self.registradores.getRegistrador(palavra[1]))))
                string.append('00000')
                string.append('000010')
                self.palavrasMontadas.append(string)
                endereco += 1

            else:
                print(palavra)

    def getPalavrasMontadas(self):
        return self.palavrasMontadas

    def getLabels(self):
        return self.labels

    def getVetor(self):
        return self.vetores
