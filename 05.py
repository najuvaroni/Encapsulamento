class restaurante:
    def __init__(self, nome,tipo,gastoMensal):
        self.nome= nome
        self.tipo= tipo
        self.__gastoMensal = gastoMensal

    def atualizarrestaurante(self,tipo2):
        self.tipo=tipo2

p1 = restaurante("Yak","Sushi bar", 1980.00)
p1.atualizarrestaurante("Cachorro Quente")
print(p1.nome, p1.tipo)
