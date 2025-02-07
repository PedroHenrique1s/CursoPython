# Utilidades do módulo functools

import functools

#functools.cache

@functools.cache
def fatorial(n):
    print(f'Valor de n: {n}')
    if n == 1:
        return n
    return n * fatorial(n-1)


fatorial(4)
fatorial(4)
#functools.partial

def somar(a,b):
    return a + b

somar_dois = functools.partial(somar,2)
somar_dois(3)