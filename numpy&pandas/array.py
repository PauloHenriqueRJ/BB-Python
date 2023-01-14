#O NumPy (Numeric Python) é uma biblioteca que permite operações com matrizes inteiras, característica que não está presente no python puro. Obs.: valores de um único tipo.


import numpy as np
#importando com 'as np' poderemos utilizar np para nos referir a numpy
lista = [14, 539, 28, 34, -2, 54, 18, 452]

np_lista = np.array(lista)

print(type(np_lista)) #tipo ndarray
print(type(lista)) #tipo primitivo list

alturas = [1.67, 1.73, 1.80, 1.96, 1.53]
np_alturas = np.array(alturas)

pesos = [65, 72.5, 110, 93, 101]
np_pesos = np.array(pesos)

IMC = np_pesos/np_alturas**2 #ao usar o array, a conta é realizada entre os valores correspondentes das listas. ex.: a 1º altura com o 1º peso.
print(IMC)

menor25 = IMC<25
print(menor25) #Será retornado com True ou False (booleanos).

print(IMC[IMC<25]) #Será retornado o valor citado nos colchetes.

print(IMC[np_alturas>1.6]) #Será retornado o IMC contendo o valor citado nos colchetes. Os verdadeiros serão impressos.

print(IMC[1:3]) #Imprimindo uma lista com os valores citados de IMC, EXCLUINDO o último citado.
