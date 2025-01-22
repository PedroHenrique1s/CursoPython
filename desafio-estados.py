# Crie um "jogo dos estados". neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deveperguntar
# ao usuário "Qual a capital do Estado x?", e chegar se o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o codigo mostra o número bruto e porcentagem de acertos.


estados_e_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

quer_continuar = True
rodadas = 0
acertos = 0

for estados,capital in estados_e_capitais.items():
    if not quer_continuar:
        break

    rodadas += 1
    print(f'\n -> Qual a capital do estados {estados}?')

    resposta = input('Sua resposta: ')
    if resposta.lower() == capital.lower():
        print('Resposta correta!')
        acertos += 1
    else:
        print(f'Respota errada! O correto seria {capital}')

    while True:
        opcao =  input('\nDeseja continuar [s/n] \n->').lower()
        if opcao not in ['s', 'n']:
            print('Responda apenas com "s" para sim ou "n" para não')
            continue
        elif opcao == 'n':
            quer_continuar = False
        break


porc = acertos / rodadas * 100
print(f'\nVocê acertou {acertos} de {rodadas}')
print(f'\nPorcentagem de acertos: {porc:.2f}')
print("\nJogo encerrado")
