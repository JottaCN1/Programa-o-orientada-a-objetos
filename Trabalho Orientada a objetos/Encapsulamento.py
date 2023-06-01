class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self._saldo}")

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self._saldo}")
        else:
            print("Saldo insuficiente. Operação de saque cancelada.")

    def obter_saldo(self):
        print(f"Saldo atual: {self._saldo}")



conta = ContaBancaria("Caio Jotta", 1000)


print(conta._saldo) 


conta.depositar(500)
conta.sacar(200)
conta.obter_saldo()
