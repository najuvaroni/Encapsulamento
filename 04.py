class livros:
    def __init__(self, titulo, autor,ano, precoDeProducao):
        self.titulo= titulo
        self.autor= autor
        self.ano = ano
        self.__precoDeProducao = precoDeProducao
    def atualizarano(self,atual):
        self.ano=atual

p1 = livros("O lado feio do amor ","Collen Houver",2015, 50.00)
p1.atualizarano(2014)
print(p1.titulo, p1.autor, p1.ano)
