class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor...')
class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def esta_carregado(self):
        print('Carregando...')

class Motocicleta(Veiculo):
    pass


moto = Motocicleta('Vermelha', 'ABC1234', 2)
moto.ligar_motor()


carro = Carro('Preto', 'DEF5678', 4)
carro.ligar_motor()


caminhao = Caminhao('Branca', 'GHI9012', 8)
caminhao.ligar_motor()
caminhao.esta_carregado()