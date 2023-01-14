string = 'Eu sou o Paulo'
string = "Me chamo Paulo"
string = """Como eu disse anteriormente
 meu nome é paulo"""
#àspas triplas permitem 'enter' no meio da string.

nome = 'Paulo Henrique'
sobrenome = """do Nascimento 
Souza"""
nomecompleto = nome + sobrenome
print(nomecompleto)
repetido = nome*2 + sobrenome*2
print(repetido)
#somando e multiplicando strings.

frase = "Quando a educação não é libertadora, o sonho do oprimido é ser opressor."

caracteres = len(frase)
print(caracteres)
#número de caracteres na string, coeçando no 0 e terminando no 72
busca = frase.find("libertadora")
print(busca)
#número do caractere que inicia a palavra procurada. caso repita só o 1º é mostrado.

quebra = frase.split(",")
print(quebra)
#transforma a string numa lista, quebrando no termo indicado.

frasealta = frase.swapcase()
print(frasealta)
#muda as maiúsculas/minúsculas da string.

semespaco = frase.strip()
print(semespaco)
#apaga os espaços em branco no início e no fim da string.

troca = frase.replace("libertadora,", "purgativa")
print(troca)
#troca palavras de uma string
#OBS.: strings são imutáveis, diferindo de valores numéricos