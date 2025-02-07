# Funções de iteração 

#enumerate 
nomes =  ['Juliando', 'José', 'Lucas', 'Luiza']

#Forma comum
for n in range(len(nomes)):
    nome = nomes[n]
    print(nome)

#Forma do Python
for i, nome in enumerate(nomes,1):
    print(f"Posição da lista {i} -> Nome: {nome}")

#sorted
conj = {1,10,-1,4}
ordenados = sorted(conj)
ordenados = sorted(conj, reserve=True)


lista1 = [1,10,-1,4]
lista1.sort()

#Funciona só com numeros 
lista1 = [1,10,-1,4]
lista2 = sorted(lista1)
# lista2 ficou sorteada 
# lista1 ficou ordenada

#reversed 
#De trás pra frente
#Apenas para lista, conjunto não tem ordem
for i in reversed(range(10)):
    print(i)


#zip
nomes =  ['Juliando', 'José', 'Lucas', 'Luiza']
idades = [30,24,19,47]
#formando uma tupula (juliano,30)
for elemento in zip(nomes, idades):
    print(elemento)