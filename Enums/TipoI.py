from enum import Enum

class TipoI(Enum):
    li = 0b01001
    bne = 0b00101
    sw = 0b101011
    addi = 0b001000
    addiu = 0b001001
    slti = 0b001010
    sltiu = 0b001011
    anddi = 0b001100
    ori = 0b001101
    xori = 0b001110
    beq = 0b000100