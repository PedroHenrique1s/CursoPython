import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculadora():
    print("***Calculadora do Pedrin***")
    print("0 -> Soma")
    print("1 -> Subtração")
    print("2 -> Multiplicação")
    print("3 -> Divisão")
    print("4 -> Exponencial")

    op = int(input("Escolha uma dessa operações: "))
    while op not in [0,1,2,3,4]:
        print("Por favor escolha um dos números que estão acima: ")
        op = int(input())
    limpar_tela

    return op
    

def processamento(op):

    limpar_tela()
    resultado = 0
    if op == 0:
        print("Escolha Soma")

        num1 = int(input("Digite o primeiro número: ")) 
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 + num2
        return resultado 
    elif op == 1:
        print("Escolha Subtração")

        num1 = int(input("Digite o primeiro número: ")) 
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 - num2
        return resultado 
    elif op == 2:
        print("Escolha Subtração")

        num1 = int(input("Digite o primeiro número: ")) 
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 * num2
        return resultado
    elif op == 3:
        print("Escolha Subtração")

        num1 = int(input("Digite o primeiro número: ")) 
        while num1 not in 0:
            print("Não é possivel dividir por zero ")
            num1 = int(input("Digite o primeiro número corretamente: "))  
        num2 = int(input("Digite o segundo número: "))
        while num2 not in 0:
            print("Não é possivel dividir por zero ")
            num2 = int(input("Digite o segundo número corretamente: "))  
        resultado = num1 / num2
        return resultado
    else: 
        print("Escolha Exponencial")

        num1 = int(input("Digite o primeiro número: ")) 
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 ^ num2
        return resultado
    
while True:
    limpar_tela()
    quer_continuar = True 
    if not quer_continuar:
        break
    operacao = calculadora()
    resultado = processamento(operacao)
    print(f"\nResultado da conta: {resultado}")

    opcao = input("\nDeseja calcular outro valor ? [s/n]\n->")
    if opcao not in ['s', 'n']:
        print('\nResponda apenas com "s" para sim ou "n" para não\n->')
        continue
    elif opcao == 'n':
        quer_continuar = False
    break