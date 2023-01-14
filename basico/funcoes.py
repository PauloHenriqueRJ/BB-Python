import math

def bhaskara(a, b, c=0):
    #o parâmetro c está pré-definido, isto é, quando não é exposto o valor de c, ele utiliza o valor pré-definido.
    delta = b**2 - 4*a*c
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    return raiz1, raiz2

print(bhaskara(1, -5, 6))