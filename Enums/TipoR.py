from enum import Enum

class TipoR(Enum):
    add = 0b100000
    addu = 0b100001
    sub = 0b100010
    subu = 0b100011
    mult = 0b11000
    multu = 0b11001
    div = 0b11010
    divu = 0b11011
    slt = 0b101010
    sltu = 0b101011
    mflo = 0b10010
    mtlo = 0b10011
    mfhi = 0b10010
    mthi = 0b10001
    andd = 0b100100
    orr = 0b100101
    nor = 0b100111
    xor = 0b100110
    sll = 0b000000
    srl = 0b000010
