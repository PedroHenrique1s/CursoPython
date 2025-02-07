# Funções built-in

# isinstance

#Forma apropriada
valor = 2
if isinstance(valor, int):
    print('Valor é do tipo int!')
else:
    print('Valor não é do tipo int')

#Forma não apropriada 
# if type(valor) == int: 
#     True


# any e all

booleanos = [True, False, True]
all(booleanos)

any(booleanos)

valores = [1,2,2.5,3]

if all(isinstance(valor,int) for valor in valores):
    print('Todos os valores são int')
else:
    print('Nem todos os valores são int')

if any(isinstance(valor,int) for valor in valores):
    print('Pelo menos um valor é int')
else:
    print('Nenhum valor é int')

# map

def somar_dois(n):
    return n +2

numeros = [3,6,10]

#Primeira forma 
numeros_mais_dois = [somar_dois(n) for n in numeros]
print(numeros_mais_dois)

#Segunda Forma 
mapa = map(somar_dois,numeros)
mapa = list(mapa)
print(mapa)

# filter

#Primeira forma 
def meu_filtro(n):
    return n > 5

numeros = [3,6,10]
filtro = filter(meu_filtro, numeros)
filtro = list(filtro)
print(filtro)

#Segunda Forma 
maiores_que_cinco = [n for n in numeros if meu_filtro(n)]