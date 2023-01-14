lista = ["Paulo irá pro ", "bb", "no ano de", 2023]

elemento1 = lista[0]
elemento2 = lista[1]
elemento3 = lista[4]
-------------------------------
esportes = ["futebol", "basquete", "vôlei"]
print(esportes)
#substituir elementos de uma lista
esportes[0] = "racha"
print(esportes)
#inserir um novo elemento numa lista
esportes.append("rugby")
print(esportes)
#inserir um elemento em determinada posição
esportes.insert(1, "esgrima")
print(esportes)
esportes.insert(10, "breakdancing")
print(esportes)
#remover elementos de uma lista
del esportes[1]
print(esportes)