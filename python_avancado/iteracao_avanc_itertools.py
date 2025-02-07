# itertools 

import itertools

# itertools.chain
seq1 = (1,2,3)
seq2 = ['a','b','c']

for elemento in itertools.chain(seq1,seq2):
    print(elemento)


#itertools.zip_longest

nomes =  ['Juliando', 'José', 'Lucas', 'Luiza']
idades = [30,24,19,47]
cpfs = ['xxx', 'yyy', 'zzz']
email = ['teste@teste.com' , 'teste123@123.com']

for elemento in itertools.zip_longest(nomes, idades,cpfs,email,fillvalue='???'):
    print(elemento)


#itertools.product 

comidas = ['churrasco', 'pizza', 'sushi']
bebidas  = ('Refrigerante', 'Água')

for prato in itertools.product(comidas,bebidas):
    print(prato)


#itertools.combination forma duplas de combinações
nomes =  ['Juliando', 'José', 'Lucas', 'Luiza']

for comb in itertools.permutations(nomes,2):
    print(comb)

for comb in itertools.combinations(nomes,2):
    print(comb)


#itertools.cycle infinito

for cor in itertools.cycle(['azul','amarelo']):
    print(cor)
    input()


nomes =  ['Juliando', 'José', 'Lucas', 'Luiza']
equipes = ['E1','E2']

for nome, equipe in zip(nomes,itertools.cycle(equipes)):
    print(nome,equipe)