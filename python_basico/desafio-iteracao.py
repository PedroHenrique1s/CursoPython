# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum()!

valores = [5, 10, 42, 7, -2, 9]

soma = 0

for valor in valores:
    soma += valor

print(f'Soma dos {valores}: {soma} ')
media = soma/len(valores)
print(f'Media dos valores: {media}')

print('\n\n\n\n\n\n')
# Dados uma sequência de números, calcule o maior da sequência.
# ATENÇÃO: Não vale usar a função max()!

seqNum = [19, 199, 32, 20, 80]
numMaior = 0
for num in seqNum:

    if  num > numMaior  :
        numMaior = num

print(f'Maior numero: {numMaior}')

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

print("\n\n\n\n\n\n\n")

listaNome = [ "pedro", "joao", "ana", "isabelly"]

for nome in listaNome:

    if len(nome) >= 5:
        print(f"Nome da pessoa com 5 caracteres ou maior: {nome}")
