# Desafio 01 

# Crie uma função que retorna se um número inteiro n 
# (maior que zero) é primo

#Dica: um número primo é um número que só é divisível por 1 
# ou por ele mesmo


def numero_primo(x, y):
    while True:
        if (x == y) or (y == 1):
            print("Numero Primo")
            break
        else:
            print("Numero não primo")
            break


numero_primo(10,0)


    
