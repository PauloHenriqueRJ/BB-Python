#O NumPy (Numeric Python) é uma biblioteca que permite operações com matrizes inteiras, característica que não está presente no python puro. Obs.: valores de um único tipo.

import numpy as np
#importando com 'as np' poderemos utilizar np para nos referir a numpy
lista = [14, 539, 28, 34, -2, 54, 18, 452]

np_lista = np.array(lista)

#print(type(np_lista)) #tipo ndarray
#print(type(lista)) #tipo primitivo list

alturas = [1.67, 1.73, 1.80, 1.96, 1.53]
np_alturas = np.array(alturas)

pesos = [65, 72.5, 110, 93, 101]
np_pesos = np.array(pesos)

IMC = np_pesos/np_alturas**2 #ao usar o array, a conta é realizada entre os valores correspondentes das listas. ex.: a 1º altura com o 1º peso.
#print(IMC)

menor25 = IMC<25
#print(menor25) #Será retornado com True ou False (booleanos).

#print(IMC[IMC<25]) #Será retornado o valor citado nos colchetes.

#print(IMC[np_alturas>1.6]) #Será retornado o IMC contendo o valor citado nos colchetes. Os verdadeiros serão impressos.

#print(IMC[1:3]) #Imprimindo uma lista com os valores citados de IMC, EXCLUINDO o último citado.
#------------------------PRÓXIMO CONTEÚDO ABAIXO: Operações com matrizes-----------------------

jogadores = np.array([[6.2, 247], [5.7, 176], [6.7, 213], [5.4, 154]])
#print(jogadores.shape) #retorna o "shape" do array. Neste caso temos uma matriz 4x2 (4 linhas e 2 colunas).
#print(jogadores)

conversor = np.array([3.281, 2.205]) 
convertido = jogadores/conversor #aqui nós dividimos a coluna 1 de jogadores com a coluna 1 de conversor. O mesmo acontece para a coluna 2 das duas matrizes, realizando a conversão de PÉ->METRO e LIBRA->QUILO, respectivamente.
print("Aqui está a matriz contendo altura e peso dos jogadores: {}".format(convertido))

#-----------------PRÓXIMO CONTEÚDO ABAIXO: Estatística Básica com Numpy-----------------------

#imprimindo a média do PESO (2ª coluna da matriz 'convertido')
#print("Aqui está a média do peso: {}" .format(np.mean(convertido[:,1])))

#impimindo a média da ALTURA (1ª coluna da matriz 'convertido')
#print("Aqui está a média da altura: {}" .format(np.mean(convertido[:,0])))

#imprimindo a mediana do peso e da altura
#print("Aqui está a mediana do peso: {}" .format(np.median(convertido[:,1])))
#print("Aqui está a média do peso: {}" .format(np.median(convertido[:,0])))

#Imprimir o desvio padrão (raiz quadrada da variança) do peso e da altura
#print("Aqui está o desvio padrão do peso: {}" .format(np.std(convertido[:,1])))
#print("Aqui está o desvio padrão da altura: {}" .format(np.std(convertido[:,0])))

#Imprimindo a correlação (o quanto uma variável é relevante para determinar a outra)
correlacao = np.corrcoef(convertido[:,0],convertido[:,1])
#Obteremos uma matriz (2x2 neste caso), onde a diagonal principal é a própria variável relaciondando-se a outra variável. Ex: a¹¹ = Peso relacionado a Peso (valor igual a 100% = 1)
#print("Aqui está a correlação: {}" .format(correlacao))

#-----------------PRÓXIMO CONTEÚDO ABAIXO: Operadores Booleanos com Numpy---------------------

#Utilizaremos das funções lógicas (ou, e, se então, etc.) em listas com o numpy

casa1 = np.array([18, 20, 10.75, 9.5])
casa2 = np.array([14, 24, 14.25, 9])
#aqui, iremos verificar quais medidas de 'minha casa' são menores que 10 OU maiores que 18.5, utilizando a lógica OR (apenas uma das duas precisa ser verdade)
#print(np.logical_or(casa1>18.5, casa1<10))

#aqui, iremos imprimir quais medidas dos dois vetores são menores do que 11, utilizando a lógica AND (as medidas de casa1 e casa2 precisam condizer com o pedido)
#print(np.logical_and(casa1<11, casa2<11))

#----------------------------------EXERCÍCIOS DE FIXAÇÃO---------------------------------------

#Exercício: o que será impresso ao rodar o programa?
np_2d = np.array([[1.5,6.4,7.8,2.2],[4.3,8.7,1.9,3.4],[5.3,7.3,9.4,2.5]])
#print(np_2d[2:,2:])
#Observando a notação de impressão temos que será impresso '[2:,2:], o que se transmite em:
#2: = da 2ªlinha em diante
#2: = da 2ªcoluna em diante
#temos que a 2ªlinha será o 3º termo do array ([5.3,7.3,9.4,2.5]) e da 2ª coluna da matriz para frente, utilizando apenas a 2ªlinha teremos o resultado como: [9.4,2.5]

#Exercício: qual dos três códigos apresenta como resultado 3.5

#Código 1
np_2d = np.array([[5,6,1,2,3,4],[4,5,3,2,1,8],[9,10,3,7,6,5]])
#print(np.sum(np_2d[0,:]))

#Código 2
np_2d = np.array([[5,6,1,2,3,4],[4,5,3,2,1,8],[9,10,3,7,6,5]])
#print(np.mean(np_2d[0,:]))

#Código 3
np_2d = np.array([[5,6,1,2,3,4],[4,5,3,2,1,8],[9,10,3,7,6,5]])
#print(np.std(np_2d[0,:]))

#Podemos observar que o único diferencial dos códigos é a conta utilizada. Soma, média e desvio padrão, respectivamente. A fração de np_2d que será impressa é [0,:], que se transmite como a 1ª linha e nenhuma coluna. Por fim, a conta será aplicada apenas ao trecho [5,6,1,2,3,4]. Dito isto, basta realizar as contas com essa lista e bater com o valor dado de 3.5

#Exercício: qual dos códigos abaixo irá retornar o valor de (3, 2)?

#Código 1
numbers = [[50, 3],[21,15],[32,80]]
np_array = np.array(numbers)
#print(np.array.len)

#Código 1
numbers = [[50, 3],[21,15],[32,80]]
np_array = np.array(numbers)
#print(np.array.dim)

#Código 1
numbers = [[50, 3],[21,15],[32,80]]
np_array = np.array(numbers)
#print(np.array.shape)

#Código 4
numbers = [[50, 3],[21,15],[32,80]]
np_array = np.array(numbers)
#print(np.array.size)