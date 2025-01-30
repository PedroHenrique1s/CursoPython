from pathlib import Path

#Retornando caminho do diretório de trabalho atual
print(Path.cwd())

#Esse caminho é absoluto 
print(Path.cwd().is_absolute()) 

#Retornando caminho da primeira pasta
print(Path('primeira_pasta'))

#Esse caminho é absoluto 
print(Path('primeira_pasta').is_absolute())

#Transformando o caminho em absoluto
print(Path.cwd() / 'primeira_pasta')
#Não recomendavél
print((Path.cwd() / 'primeira_pasta').exists()) #verificação para vê se a pasta existe no caminho absoluto

#Garantindo que estamos retornando o caminho para a pasta do script 
print(__file__)
print(Path(__file__).is_absolute())
print(Path(__file__).parent())

print((Path(__file__).parent() / 'primeira_pasta').exists())


#Trabalhando com partes de caminho

caminho_arquivo = Path(__file__)

print(caminho_arquivo)
print(caminho_arquivo.anchor) #nossa pasta raiz que fica dentro do nosso disco
print(caminho_arquivo.name) #é o nome do arquivo que traz com extensão
print(caminho_arquivo.stem) #é base do nome sem a extensão
print(caminho_arquivo.suffix) #trás apenas a extensão do arquivo
print(caminho_arquivo.drive) #traz o nome do nosso disco

print(caminho_arquivo.parent) #é a pasta anterior que está contido este arquivo
print(caminho_arquivo.parent[0]) #é a pasta anterior que está contido este arquivo retornando a pasta anterior com mais facilidade
 