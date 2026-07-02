class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def exibir_info(self):
        print(f"Largura: {self.largura}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")

r1 = Retangulo(78, 200)
r1.exibir_info()