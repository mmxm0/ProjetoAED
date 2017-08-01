from random import *
def geraListaCPF():
    lista = []
    while len(lista)<9:
        lista.append(randint(0,9))
    return lista

def geradorCPF(lista_CPF):
    soma1=0
    for digito,peso in zip(lista_CPF,range(10,1,-1)):
        soma1 +=digito*peso
    digverificador1 = soma1%11
    digverificador1 = 11-digverificador1
    if digverificador1 >9:
        digverificador1 = 0
    lista_CPF.append(digverificador1)
    soma2=0
    for digito,peso in zip(lista_CPF,range(11,1,-1)):
        soma2 +=digito*peso
    digverificador2 = soma2%11
    digverificador2 = 11-digverificador2
    if digverificador2 >9:
        digverificador2 = 0
    lista_CPF.append(digverificador2)
    cpf =""
    for i in lista_CPF:
        cpf+=str(i)
    return cpf