class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("O veículo está ligado.")

    def desligar(self):
        print("O veículo está desligado.")


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print("Abrindo a porta do carro.")



class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        print("A moto está empinando.")


carro = Carro("Toyota", "Corolla", "Prata")
moto = Moto("Honda", "CBR600RR", 600)


carro.ligar()
carro.abrir_porta()

moto.desligar()
moto.empinar()
