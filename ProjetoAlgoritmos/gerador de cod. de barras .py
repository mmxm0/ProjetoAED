#validação do código de barras do tipo EAN - 13 e verificação de origem de um produto
from random import *
import string
def geraCod(lista_cod=[]):
    for i in range(13):
        lista_cod.append(randint(0,9))

    return lista_cod

def GeradorCodBarras(produtode1=[],produtode3=[]):
    lista_cod = geraCod()
    pop13 = lista_cod.pop(-1)
    for a,b in enumerate(lista_cod):
        if a%2 == 0:
            produtode1.append(b)
        else:
            produtode3.append(b)

    produtode1 = [ y*1 for y in produtode1]
    produtode3 = [ z*3 for z in produtode3]

    soma = sum(produtode1) + sum(produtode3)
    soma = 10 - soma%10
    lista_cod.append(soma)

    return lista_cod


def printaCodBarras():
    cod_de_barras = GeradorCodBarras()
    string = ""
    for i in cod_de_barras:
        string+=str(i)
    return string

print(printaCodBarras())