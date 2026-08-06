class Calculadora:
    def __init__(self):

        self.historico = []

    def somar(self, a, b):
        resultado = a + b

        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):

        if b == 0:
            print("Aviso: Erro! Não é possível dividir por zero.")
            self.historico.append(f"{a} / {b} = Falha (Divisão por zero)")
            return None

        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado

    def exibir_historico(self):
        print("\n=== HISTÓRICO DE OPERAÇÕES ===")
        # Se a lista estiver vazia (tamanho zero)
        if len(self.historico) == 0:
            print("O histórico está vazio.")
        else:
            for operacao in self.historico:
                print(f"[•] {operacao}")
        print("==============================")

calc = Calculadora()


print("Executando operações...")
calc.somar(5, 3)
calc.somar(10, 20)

calc.subtrair(10, 4)
calc.subtrair(5, 15)

calc.multiplicar(4, 2)
calc.multiplicar(7, 3)

calc.dividir(20, 4)
calc.dividir(10, 2)


calc.dividir(8, 0)


calc.exibir_historico()