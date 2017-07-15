class ULA():
    def somar(registrador1, registrador2):
        return (int(registrador1, 16) + int(registrador2, 16))

    def somarImmediate(registrador1, registrador2):
        return (int(registrador1, 16) + int(registrador2, 2))

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

    def verificarMenorImmediate(registrador1, registrador2):
        if (int(registrador1, 16)) < (int(registrador2, 2)):
            return 1
        else:
            return 0

    def andd(registrador1, registrador2):
        return (int(registrador1, 16) & int(registrador2, 16))

    def anddImmediate(registrador1, registrador2):
        return (int(registrador1, 16) & int(registrador2, 2))

    def orr(registrador1, registrador2):
        return (int(registrador1, 16) | int(registrador2, 16))

    def orrImmediate(registrador1, registrador2):
        return (int(registrador1, 16) | int(registrador2, 2))

    def xor(registrador1, registrador2):
        return (int(registrador1, 16) ^ int(registrador2, 16))

    def xorImmediate(registrador1, registrador2):
        return (int(registrador1, 16) ^ int(registrador2, 2))

    def nor(registrador1, registrador2):
        return ~(int(registrador1, 16) & int(registrador2, 16))

    def diferenca(registrador1, registrador2):
        return (int(registrador1, 16)) != (int(registrador2, 16))

    def shiftLeft(registrador1, registrador2):
        return (int(registrador1, 16)) << (int(registrador2, 2))

    def shiftRight(registrador1, registrador2):
        return (int(registrador1, 16)) >> (int(registrador2, 2))
