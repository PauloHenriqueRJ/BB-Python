situacao = ["não passei...", 'não passei...', 'não passei...', "não passei...", "PASSEI CARAAAALHOOOOOO!!"]
contador = 0
#Uma diferença entre for e while é que o while precisa seguir um contador previamente definido
while situacao[contador] == "não passei...":
	print("Não vou desistir!!")
	contador = contador +1
#o código do while geralmente tem algo relacionado a modificar o contador para que o while continue lendo o que foi pedido até alcançar algo desejado
print(situacao[contador])

#neste caso, o while começa no 0 e vai adicionando +1 ao contador até não poder mais estar em while. Ao fim, o contador é +4, que fica registrado na memória. Ao printar, o 5º item é PASEICARAI