# Argumentos arbitrários com *args e **kwargs


def exibe_argumentos(*args, **kwargs):
    print(f'Argumento passados sem palavras-chaves: {args}')
    print(f'Argumento passados com palavras-chaves: {kwargs}')



exibe_argumentos(1,2,3,4, x=6, y=20)