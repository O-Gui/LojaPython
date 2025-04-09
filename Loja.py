from Carrinho import Carrinho
from Produto import Produto

class Loja:
    def __init__(self):
        self.carrinho = Carrinho()
        self.produtos = [
            Produto("celular", 1000.0, 10),
            Produto("notebook", 1500.0, 5),
            Produto("PC gamer", 2000.0, 11),
            Produto("teclado", 150.0, 8),     
            Produto("mouse", 100.0, 10)
        ]