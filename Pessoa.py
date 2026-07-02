class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos e moro na cidade {self.cidade}."

p1 = Pessoa("Willian", 30, "São Paulo")
p2 = Pessoa("Maria", 25, "Rio de Janeiro")
print(p1.apresentar())
print(p2.apresentar())