class Gato:
    tipo = "É um Felino."

    def __init__(self, nome):
        self.nome = nome

gatuno1 = Gato("Frajola")
gatuno2 = Gato("Tom")

print(gatuno1.tipo)
print(gatuno1.nome)

print(gatuno2.nome)
print(gatuno2.tipo)