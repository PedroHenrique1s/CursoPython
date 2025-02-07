# Crie uma função chamada multiplicador_por. O que está 
# função faz é retornar uma nova função f 
# capaz de multiplicar um número qualquer 
# pelo fator n passado à função multiplicar_por.

# Exemplo de uso:

import functools


def mult(a, b):
    return a*b



def multiplicar_por(n):
    return functools.partial(lambda x, y: x * y, b=n)


dobrar = multiplicar_por(2)
print(dobrar(3))

vezes_cinco = multiplicar_por(5)
print(vezes_cinco(10))