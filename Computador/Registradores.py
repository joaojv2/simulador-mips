class Registradores():
    def __init__(self):
        self.registradores = [[]]
        self.value = 0
        self.criarRegistradores()

    def criarRegistradores(self):
        self.registradores = [['$zero', '0' ,self.value],
                        ["$zero","0",self.value],
                        ["$at","1",self.value],
                        ["$v0","2",self.value],
                        ["$v1","3",self.value],
                        ["$a0","4",self.value],
                        ["$a1","5",self.value],
                        ["$a2","6",self.value],
                        ["$a3","7",self.value],
                        ["$t0","8",self.value],
                        ["$t1","9",self.value],
                        ["$t2","10",self.value],
                        ["$t3","11",self.value],
                        ["$t4","12",self.value],
                        ["$t5","13",self.value],
                        ["$t6","14",self.value],
                        ["$t7","15",self.value],
                        ["$s0","16",self.value],
                        ["$s1","17",self.value],
                        ["$s2","18",self.value],
                        ["$s3","19",self.value],
                        ["$s4","20",self.value],
                        ["$s5","21",self.value],
                        ["$s6","22",self.value],
                        ["$s7","23",self.value],
                        ["$t8","24",self.value],
                        ["$t9","25",self.value],
                        ["$k0","26",self.value],
                        ["$k1","27",self.value],
                        ["$gp","28",self.value],
                        ["$sp","29",self.value],
                        ["$fp","30",self.value],
                        ["$ra","31",self.value],
                        ["pc","",self.value],
                        ["hi","",self.value],
                        ["lo","",self.value]]

    def getRegistradores(self):
        return self.registradores

    def getRegistrador(self, nome):
        for registador in self.registradores:
            if registador[0] == "$" + nome:
                return registador[1]

    def getValorRegistrador(self, nome):
        for registador in self.registradores:
            if registador[1] == str(int(nome,2)):
                return registador[2]

    def getValorRegistradorPorNome(self, nome):
        for registador in self.registradores:
            if registador[0] == nome:
                return registador[2]

    def setRegistrador(self, registradorr, value):
        for registador in self.registradores:
            if registador[1] == str(int(registradorr,2)):
                registador[2] = hex(value)

    def setRegistradorPorNome(self, registradorr, value):
        for registador in self.registradores:
            if registador[0] == registradorr:
                registador[2] = hex(value)