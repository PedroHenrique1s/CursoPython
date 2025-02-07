# Desempacotando sequências

seq = (10,20,30)
a,b,c = seq

dic = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3'
}

for chave, valor in dic.keys():
    print(chave, valor)

nomes =  ['Juliando', 'José', 'Lucas', 'Luiza']
idades = [30,24,19,27]

for i, (nomes,idades) in enumerate(zip(nomes,idades)):
    print(i, nomes, idades)


minha_lista = [1,2,3,4,5]
primeiro, *meio, ultimo = minha_lista

print(primeiro)
print(meio)
print(ultimo)

#Sempre vai retornar uma lista 
primeiro, *resto = (1,2,3,4)

#variavel que nn quer usar *_ representa um variavel que não vai ser usada
primeiro, *_, ultimo = (1,2,3,4)
