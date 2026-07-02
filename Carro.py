class Carro:
    def __init__(self, marca, modelo, ano , velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, valor):
        if valor > 0:
            self.velocidade += valor
            print(f"O carro acelerou {valor} km/h. Velocidade atual: {self.velocidade} km/h.")
        else:
            print("Valor de aceleração inválido. O valor deve ser positivo.")

    def frear(self, valor: int):
        self.velocidade -= valor
        print(f"O carro freou para {valor} km/h.")

    def exibir_info(self):
        print("="*20)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade: {self.velocidade} km/h")
        print("="*20)

c1 = Carro("chevrolet", "cruze", 2013, 30)
c1.acelerar(70)
c1.frear(60)
c1.exibir_info()
