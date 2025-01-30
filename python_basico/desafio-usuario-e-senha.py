# Desafio - crie um programa que :
# - Pede por um nome de usuário e uma senha.
# - Se amabos forem corretos, exibe uma mensagem de sucesso;
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como variáveis dentro do próprio código

usuario_correto = "Pedro"
senha_correta = "senha secreta"

usuario = input('Digite um nome de usuário: ') == usuario_correto
senha = input('Digite a senha: ') == senha_correta


if usuario and senha:
    print("Usuário logado com sucesso")
if usuario and not senha:
    print("senha incorreta")
else:
    print(f'Usuário {usuario} não existe')




