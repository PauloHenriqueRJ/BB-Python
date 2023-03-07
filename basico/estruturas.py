#Estruturas de Decisão

#if-else
altura = 1.80
if altura <1.70:
  print("Ah lá o anãokkk")
else:
  print("Ah lá o bambukkkk")
#A identação (recuo ou não) é obrigatória para o funcionamento do código.

#if-elif-else
saldo = 500
if saldo < 1000:
  print('Você está no caminho certo! Continue assim, ok? (Pobrekk).')
	
#Estruturas de Repetição:
	
#for
#a variável criada realiza um loop dentro da lista, assumindo os valores dela.  
times = ["Flamengo",'Wasco','Botafogo','Piracicaba']
for time in times:
  print(time)

#Imprimindo um termo específico dentro de uma string. Obs.: case sensitive.
nomecompleto = "Paulo Henrique do Nascimento Souza"
for vogais in nomecompleto:
  if vogais in ['a', 'e', 'i', 'o', 'u']:
    print(vogais)

#for percorrendo um range:
for k in range(9):
	print(k)

#palavra reservada 'break':
durags = ['azul', 'preta', 'verde', 'cinza']

for cor in durags:
	print(cor)
	if cor == "preta":
		break

#palavra reservada 'continue' e for-else:
for pares in range(21):
	if pares %2 == 0: #resto da divisão por 2 = 0 ou seja, números pares!
		continue #resumino, o for irá realizar a leitura do range e se o número for par, ele irá prosseguir e continuar olhando o restante do código. caso não seja par, ele irá seguir para a próxima linha!
	print(pares)
else:
	print('Todos os números ímpares do range (0,21,1) foram impressos!')

#While/While-else---------

situacao = ["não passei...", 'não passei...', 'não passei...', "não passei...", "PASSEI CARAAAALHOOOOOO!!"]
contador = 0
#Uma diferença entre for e while é que o while precisa seguir um contador previamente definido
while situacao[contador] == "não passei...":
	print("Não vou desistir!!")
	contador = contador + 1
#o código do while geralmente tem algo relacionado a modificar o contador para que o while continue lendo o que foi pedido até alcançar algo desejado
	print(situacao[contador])

#neste caso, o while começa no 0 e vai adicionando +1 ao contador até não poder mais estar em while. Ao fim, o contador é +4, que fica registrado na memória. Ao printar, o 5º item é PASEICARAI
else:
	print('Jogador, agora é só curtir o bem bom!!')