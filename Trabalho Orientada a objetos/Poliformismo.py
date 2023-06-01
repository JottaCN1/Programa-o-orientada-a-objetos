class Animal:
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        return "O cachorro faz 'Au Au!'"


class Gato(Animal):
    def falar(self):
        return "O gato faz 'Miau Miau!'"


class Vaca(Animal):
    def falar(self):
        return "A vaca faz 'Moo Moo!'"


def fazer_animal_falar(animal):
    print(animal.falar())


cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

fazer_animal_falar(cachorro)
fazer_animal_falar(gato)
fazer_animal_falar(vaca)