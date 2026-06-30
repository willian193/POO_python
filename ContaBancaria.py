class ContaBancaria:

    def __init__(self, numero_conta, titular, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")


    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido. O valor deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")

        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def exibir_extrato(self):
        print("="*20)
        print(f"conta: {self.numero_conta}")
        print(f"titular: {self.titular}")
        print(f"saldo: R${self.saldo:.2f}")
        print("="*20)

conta1 = ContaBancaria(numero_conta="001-5", titular="Willian", saldo=67.0)
conta2 = ContaBancaria(numero_conta="002-3", titular="Maria", saldo=150.0)
conta1.depositar(valor=100)
conta1.sacar(valor=100)
conta1.exibir_extrato()
conta2.depositar(valor=200)
conta2.sacar(valor=50)
conta2.exibir_extrato()