#Funções Lambda 
#usado para lógicas curtas

def meu_filtro(x):
    return x > 2

lambda x: x > 2

# lambda x,y,z: x + y + z

filtro = filter(lambda x: x > 2, [1,2,3,4])
list(filtro)