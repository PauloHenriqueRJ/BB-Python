range = range(5)
#range = range(0start,5stop,1step)
lista = list(range)
print(lista)
#por algum motivo, só um range pode funcionar ao mesmo tempo na minha máquina...

range1 = range(1,12,2)
#1 = start = início
#12 = stop = valor excluído, irá parar no antecessor.
#2 = step = passo que  ele dá
lista1 = list(range1)
print(lista1)

range2 = (100,0,-5)
#se o passo for negativo a lista será imprimida negativada até o stop.
lista2 = list(range2)
print(lista2)

range3 = range(2, 1000, 3000)
#apenas o start é imprimido, o passo ultrapassa o stop.
lista3 = list(range3)
print(lista3)

range4 = range(0.5, 75, 1)
#range só aceita números inteiros.
lista4 = list(range4)
print(lista4)