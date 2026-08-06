class Animal:

    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        print(f"{self.nome} emitir som")

class cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} latido")

class gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} miauuu")

def fazer_barulhoo(animal):
    animal.emitir_som()

animais = [cachorro("Rex"), gato("Mimi")]


for animal in animais:
    fazer_barulhoo(animal)
    