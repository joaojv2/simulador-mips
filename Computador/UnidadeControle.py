from Computador.ULA import ULA
from Enums.TipoR import TipoR
from Enums.TipoI import TipoI

class UnidadeControle():
    def __init__(self):
        self.palavra = []

    def recebePalavra(self, palavra, processador):
        self.palavra = palavra
        self.processador = processador
        self.fazendoLogica()

    def fazendoLogica(self):
        #li
        if self.palavra[0] == '0b1001':
            self.processador.setRegistrador(self.palavra[2], int(self.palavra[3], 2))
        #bne
        elif self.palavra[0] == '0b101':
            if ULA.diferenca(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])):
                self.processador.setPC(self.processador.getLabel(self.palavra[4]))
        #beq
        elif self.palavra[0] == '0b100':
            if ULA.diferenca(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])) == False:
                self.processador.setPC(self.processador.getLabel(self.palavra[4]))
        #sw terminar
        elif self.palavra[0] == '0b101011':
            print("Oi")
        #addi
        elif self.palavra[0] == '0b1000':
            self.processador.setRegistrador(self.palavra[2], ULA.somarImmediate(self.processador.getValorRegistrador(self.palavra[1]), self.palavra[3]))
        #addiu
        elif self.palavra[0] == '0b1001':
            self.processador.setRegistrador(self.palavra[2], ULA.somarImmediate(self.processador.getValorRegistrador(self.palavra[1]), self.palavra[3]))
        #slti
        elif self.palavra[0] == '0b1010':
            self.processador.setRegistrador(self.palavra[2], ULA.verificarMenorImmediate(self.processador.getValorRegistrador(self.palavra[1]), self.palavra[3]))
        #sltiu
        elif self.palavra[0] == '0b1011':
            self.processador.setRegistrador(self.palavra[2], ULA.verificarMenorImmediate(self.processador.getValorRegistrador(self.palavra[1]), self.palavra[3]))
        #andi
        elif self.palavra[0] == '0b1100':
            self.processador.setRegistrador(self.palavra[2], ULA.anddImmediate(self.processador.getValorRegistrador(self.palavra[1]), self.palavra[3]))
        #ori
        elif self.palavra[0] == '0b1101':
            self.processador.setRegistrador(self.palavra[2], ULA.orrImmediate(self.processador.getValorRegistrador(self.palavra[1]), self.palavra[3]))
        #xori
        elif self.palavra[0] == '0b1110':
            self.processador.setRegistrador(self.palavra[2], ULA.xorImmediate(self.processador.getValorRegistrador(self.palavra[1]), self.palavra[3]))
        #add#
        elif self.palavra[5] == '0b100000':
            self.processador.setRegistrador(self.palavra[3], ULA.somar(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #addu
        elif self.palavra[5] == '0b100001':
            self.processador.setRegistrador(self.palavra[3], ULA.somar(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #sub
        elif self.palavra[5] == '0b100010':
            self.processador.setRegistrador(self.palavra[3], ULA.subtrair(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #subu
        elif self.palavra[5] == '0b100011':
            self.processador.setRegistrador(self.palavra[3], ULA.subtrair(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #mult
        elif self.palavra[5] == '0b11000':
            self.processador.setRegistradorPorNome("lo", ULA.multiplicar(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #multu
        elif self.palavra[5] == '0b11001':
            self.processador.setRegistradorPorNome("lo", ULA.multiplicar(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #div
        elif self.palavra[5] == '0b11010':
            self.processador.setRegistradorPorNome("lo", ULA.dividir(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #divu
        elif self.palavra[5] == '0b11011':
            self.processador.setRegistradorPorNome("lo", ULA.dividir(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #slt
        elif self.palavra[5] == '0b101010':
            self.processador.setRegistrador(self.palavra[3], ULA.verificarMenor(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #sltu
        elif self.palavra[5] == '0b101011':
            self.processador.setRegistrador(self.palavra[3], ULA.verificarMenor(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #mflo
        elif self.palavra[5] == '0b10010':
            self.processador.setRegistrador(self.palavra[3], int(self.processador.getValorRegistradorPorNome("lo"), 16))
        #mtlo
        elif self.palavra[5] == '0b10011':
            self.processador.setRegistradorPorNome("lo", int(self.processador.getValorRegistrador(self.palavra[1]), 16))
        #mfhi
        elif self.palavra[5] == '0b10010':
            self.processador.setRegistrador(self.palavra[3], int(self.processador.getValorRegistradorPorNome("hi"), 16))
        #mthi
        elif self.palavra[5] == '0b10001':
            self.processador.setRegistradorPorNome("hi", int(self.processador.getValorRegistrador(self.palavra[1]), 16))
        #and
        elif self.palavra[5] == '0b100100':
            self.processador.setRegistrador(self.palavra[3], ULA.andd(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #or
        elif self.palavra[5] == '0b100101':
            self.processador.setRegistrador(self.palavra[3], ULA.orr(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #nor
        elif self.palavra[5] == '0b100111':
            self.processador.setRegistrador(self.palavra[3], ULA.nor(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #xor
        elif self.palavra[5] == '0b100110':
            self.processador.setRegistrador(self.palavra[3], ULA.xor(self.processador.getValorRegistrador(self.palavra[1]), self.processador.getValorRegistrador(self.palavra[2])))
        #sll
        elif self.palavra[5] == '0b0':
            self.processador.setRegistrador(self.palavra[3], ULA.shiftLeft(self.processador.getValorRegistrador(self.palavra[2]), self.palavra[4]))
        #srl
        elif self.palavra[5] == '0b10':
            self.processador.setRegistrador(self.palavra[3], ULA.shiftRight(self.processador.getValorRegistrador(self.palavra[2]), self.palavra[4]))

        #syscall
        elif self.palavra[5] == '001100':
            if int(self.processador.getValorRegistradorPorNome("$v0"), 16) == 1:
                print(int(self.processador.getValorRegistradorPorNome("$a0"),16))
                self.processador.ttk.setInput(int(self.processador.getValorRegistradorPorNome("$a0"),16))
