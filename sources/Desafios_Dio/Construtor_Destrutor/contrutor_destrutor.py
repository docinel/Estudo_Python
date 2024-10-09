class Cachorro:
    def __init__(self, nome, raca, acordado=True):
        print(f'{nome} foi criado!')
        self.nome = nome
        self.raca = raca
        self.acordado = acordado

    def __del__(self):
        print(f'{self.nome} foi destruido!')

    def latir(self):
        print('au au au au')

def criar_cachorro():
    cachorro = Cachorro('Toby', 'SRD')
    cachorro.latir()
    return cachorro

cachorro = criar_cachorro()

del cachorro
