#Desafio crie um programa que:
# - Pede pelo seu nome e idade
# - Da oi para voce
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(nome)
print(idade)

print("Oi")
qtdNome = len(nome)
qtdAnos = idade + 5

print(qtdNome)
print(qtdAnos)
