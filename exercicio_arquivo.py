from pathlib import Path

# Desenvolva um script para enconstrar um arquivo dentro da pasta home do usuário




def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file() :
            if arquivo.name == 'arquivo_primeira_pasta':
                print(arquivo)


encontra_arquivo(Path.cwd(), 'arquivo1')