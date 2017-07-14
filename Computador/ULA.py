class ULA():
    def somar(registrador1, registrador2):
        return (int(registrador1, 16) + int(registrador2, 16))

    def subtrair(registrador1, registrador2):
        return (int(registrador1, 16) - int(registrador2, 16))

    def multiplicar(registrador1, registrador2):
        return (int(registrador1, 16) * int(registrador2, 16))

    def dividir(registrador1, registrador2):
        return (int(registrador1, 16) / int(registrador2, 16))

    def verificarMenor(registrador1, registrador2):
        if (int(registrador1, 16)) < (int(registrador2, 16)):
            return 1
        else:
            return 0

    def andd(registrador1, registrador2):
        return (int(registrador1, 16) & int(registrador2, 16))

    def orr(registrador1, registrador2):
        return (int(registrador1, 16) | int(registrador2, 16))

    def xor(registrador1, registrador2):
        return (int(registrador1, 16) ^ int(registrador2, 16))

    def nor(registrador1, registrador2):
        return ~(int(registrador1, 16) & int(registrador2, 16))

    def diferenca(registrador1, registrador2):
        return (int(registrador1, 16)) != (int(registrador2, 16))
