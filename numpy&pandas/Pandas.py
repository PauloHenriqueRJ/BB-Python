#A biblioteca Pandas é essencial para a criação de DATA FRAMES (em resumo, tabelas)
import pandas as pd

paises = ["USA","Austrália","Japão","Índia","Rússia","Marrocos","Egito"]
mao_inglesa = [True,False,False,False,True,True,True]
cpc = [809,731,588,18,200,70,45]
#criando um dicionário (em chaves é o texto, a entrada é uma lista)
dicionario = {"paises":paises, "mao_inglesa":mao_inglesa, "cpc":cpc}
carros = pd.DataFrame(dicionario)
#apenas mudando o índice (0, 1, 2, ...) para algo mais condizente com o conteúdo:
rotulos = ["US","AUS","JP","IN","RU","MOR","EG"]
carros.index = rotulos
#print(carros)

#Utilizaremos colchetes duplos ao destacar colunas de matrizes pois assim elas sairão como objetos DataFrame. Ao utilizar colchetes únicos, elas sãem como series. Obs.: ao utilizar +1 coluna, só DataFrames serão impressos
#print(carros[["paises", "cpc"]])
#print(type(carros[["paises", "cpc"]]))

#Agora, imprimindo linhas as 3 primeiras linhas. [0:3] em Pandas, o 3 será EXCLUÍDO, sendo impressas apentas as linhas 0, 1 e 2.
#print(carros[0:3])


#Funções loc (localizar) para localizar e imprimir coisas específicas. Usaremos o índice para achar oque queremos. Lembrando que colchetes únicos imprimem objetos series ou seja, só podendo imprimir uma linha/coluna de cada vez. 
#print(carros.loc[["JP", "US"]])
#Agora, utilizaremos loc para imprimir apenas uma informação de determinada coluna. Neste caso específico, um objeto do tipo series será necessário.
#print(carros.loc["RU", "mao_inglesa"])
#Por fim, agora duas colunas sendo impressas junto do índice. Habilitamos todas as linhas mas criamos uma lista para escolher as colunas.
#print(carros.loc[:, ["mao_inglesa", "cpc"]])

#Função iloc para "fatiar" o DataFrame. Neste caso, basta imaginar um tabuleiro de xadres. Ao inserir os valores desejados para o fatiamento, conforme a função e utilizada ela irá imprimir exatamente o espaço que foi requisitado. Dentro de nossa matriz 3x7, iremos fatiar o trecho da linha 2 e 3, colunas 1 e 2. Irá retornar uma matrix 2x2 com os valores desejados.
#print(carros.iloc[[1,2], [0,1]])

#Resumão geral:
#Acessar colunas: colchetes Duplos [["A", "B"]]
#Acessar linhas: fatiamento [1:4]
#loc = baseado nos rótulos
#iloc = baseado em índice 

#------------PRÓXIMO CONTEÚDO ABAIXO: Filtros e funções lógicas em Data Frames---------------
#Iniciaremos uma filtragem simples imprimindo a coluna relacionada a mão inglesa (booleana, true e false) mas somente os valores que forem verdadeiros. Traremos uma nova variável para atribuir a essa coluna e logo a seguir imprimir essa seleção.
#print(carros[carros["mao_inglesa"]])

#Outra filtragem, imprimindo apenas os que tem em cpc valores superiores a 600. Atentar na escrita.
#print(carros[carros["cpc"]>500])

#Agora iremos misturar um pouco de NumPy para utilizar-se de funções lógicas. Iremos definir limites de CPC para serem impressos.
from numpy import logical_and
import numpy as np

cpc = carros["cpc"]
entrenumeros = np.logical_and(cpc>100, cpc<500)
#Simplificando o código, temos:
print(carros[np.logical_and(carros["cpc"]>100, carros["cpc"]<500)])

#----------------------------------EXERCÍCIOS DE FIXAÇÃO---------------------------------------

