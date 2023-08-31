class Conta:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.titular = titular
        print(self.__saldo)

    def sacar(self, saque):
        self.__saldo -= saque

    def depositar(self, deposito):
        self.__saldo += deposito

    def Exibir(self):
        print(self.__saldo)

a = Conta(109.00, "Bruno")
a.sacar(20)
a.Exibir()
