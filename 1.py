class Cliente:
    def __init__(self, codigo):
        self.__codigo = codigo
    def MostrarCodigo(self):
            print(self.__codigo)
a = Cliente(10)
a.MostrarCodigo()
