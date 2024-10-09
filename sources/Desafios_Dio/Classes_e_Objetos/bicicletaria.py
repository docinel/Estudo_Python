class Bicicleta:
    def __init__(self, cor,modelo,  ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzinar(self):
        print('Plim Plim')

    def parar(self):
        print('Parando')
        print('Parou')

    def correr(self):
        print('Vrummmmm')

    def __str__(self):
        # return f'{self.cor}, {self.modelo}, {self.ano}, {self.valor}'
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'
    


b1 = Bicicleta('azul', 'caloi', 2022, 1200)
b1.buzinar()
b1.correr()
b1.parar()
print(b1)