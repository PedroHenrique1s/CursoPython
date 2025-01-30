# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções

# gerar_baralho -> retorna um baralho novo. Parâmetro da função
# definem quantas cópias retornar (1 baralho, 2 baralho, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado

# mostrar_baralho -> exibe a quantidade de cartas no baralho
# e quais são

# dar_as_cartas -> distribui as cartas do baalho entre X jogadores,
# de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
#     - gerar o baralho e exibi-load
#     - dar as cartas para os jogadores
#     - exibir o baralho após as cartas terem sido dustrubuídas
#     - exibir a mão de cada jogador

# DICA: utilize os símbolos para representar '♠', '♣', '♥', '♦' os naipes
# DICA: utiliza a função ram.shuffle (módulo random) para embaralhar.

import random

def gerar_baralho(n_copias = 1, coringas=False, embaralhado= True):
    baralho = []

    naipes =  ['♠','♣','♥','♦']
    numeros = ["A", "2", "3", "4", "5", "6", "7","Q","J","K"]

    for _ in range(n_copias):
        for naipe in naipes:
            for numero in numeros:
                carta = numero + naipe
                baralho.append(carta)
        if coringas :
            baralho.extend(['JK1', 'JK2'])
    if embaralhado:
        random.shuffle(baralho)

    return baralho

def mostrar_baralho(baralho):
    print(f'Há {len(baralho)} cartas no baralho')
    print('Cartas: ')
    print(', '.join(baralho))


def dar_as_cartas(baralho, n_jogadores=4, n_cartas=3):
    jogadores = {}

    for i in range(n_jogadores):
        mao = []
        while len(mao) < n_cartas:
            carta = baralho.pop(0)
            mao.append(carta)
        nome_jogador = f'Jogador {i + 1}'
        jogadores[nome_jogador] = mao
    return jogadores

def mostrar_jogadores(jogadores):
    for nomeJogador, mao in jogadores.items():
        print(f'Há {len(mao)} cartas na mão do jogador {jogador}')
        print('Cartas:')
        for carta in mao:
            print(f' ->{carta}')


baralho = gerar_baralho()
mostrar_baralho(baralho)
jogador = dar_as_cartas(baralho)
mostrar_baralho(baralho)
mostrar_jogadores(jogador)
