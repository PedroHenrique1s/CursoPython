import os 

carros = [
    ("Tracker", 120),
    ("Onix", 90),
    ("Spin",150),
    ("HB20",85),
    ("Tucson",120),
    ("Uno",60),
    ("Mobi",70),
    ("Pulse",130) 
]

alugados = []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} / dia.".format(i, car[0], car[1]))



while True:
    limpar_tela()

    print("=====")
    print("Bem vindo á locadora de carros")
    print("=====")

    print("O que deseja fazer ?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2- Devolver um carro")

    op = int(input("\n->"))
    if op == 0:
        limpar_tela()
        mostrar_lista_de_carros(carros)
    elif op == 1:
        limpar_tela()
        mostrar_lista_de_carros(carros)
        print("=====")
        print("Escolha o código do carro")
        cod_car = int(input("\n->"))

        print("Por quantos dias você deseja alugar este carro ?")
        dias = int(input("\n->"))
        limpar_tela()

        print("Você escolheo {} por {} dias.".format(carros[cod_car][0], dias))
        print("O aluguel totalizaria R${}. Deseja alugar".format(dias * carros[cod_car][1]))

        print("0 - SIM | 1 - NÃO")
        conf = int(input("->"))
        if conf == 0:
            print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros a devolver.")
        else :
            print("Segue a lista de carros alugados. Qual você deseja devolver ?")
            mostrar_lista_de_carros(alugados)
            print("\nEscolha o código do carro que deseja devolver")
            cod = int(input("->"))
            if conf == 0:
                print("Obrigado por devolver o carro {}".format(alugados[cod][0]))
                alugados.append(alugados.pop(cod))
    
    print("")
    print("=====")
    print("Digite 0 para CONTINUAR | Digite 1 para SAIR")
    if int(input()) == 1:
        break

        
