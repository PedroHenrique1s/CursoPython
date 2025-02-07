# Decoradores 

# def func():
#     return 2 


# minha_funcao = func
# retorno = minha_funcao()

# print(retorno)


# def func():
#     return 2 


# def exibe_func(f):
#     print(f'Objeto de função recebido {f}')
#     print(f'Nome da função: "{f.__name__}"')



# exibe_func(func)


# def func_externa(x):
#     def func_interna():
#         return x + 2
#     valor = func_interna()
#     return valor 

# resultado = func_externa(3)
# print(resultado)



def func_externa(x):
    def func_interna(y):
        return x + y + 2
    return func_interna 

f = func_externa(2)
print(f)
print(f(2))

