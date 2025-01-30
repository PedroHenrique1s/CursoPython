# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
#     "abc" com chave 1 = "bcd"
#     "ABCDE" com chave 2 = "CDEFG"
#     "Cachorro" com chave -1 = "Bzbgnqqn"
#     "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 string com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

texto= "ABCDE"
chave = 2

minusculo = "abcdefghijklmnopqrstuvwxyz"
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifra = ''

def condicao_caractere(caractere, seq, chave):
    i = seq.index(caractere)
    novo_index = i + chave
    # Lidar com situação onde índice está à direita da seq
    while novo_index >= len(seq):
        novo_index -= len(seq)
    # Lidar com situação onde índice está à esquerda da seq
    while novo_index < 0:
        novo_index += len(seq)
    return seq[novo_index]

for caractere in texto:
    if caractere in minusculo:
        caractere_cifra = condicao_caractere(caractere, minusculo, chave)
    elif caractere in maiusculo:
        caractere_cifra = condicao_caractere(caractere, maiusculo, chave)
    else:
        caractere_cifra = caractere
    cifra += caractere_cifra

print(cifra)
