import string
import random
class Usuario:
    idd = 0
    def __init__(self,nome=None,curso=None,cpf=None,situacao = None,qttLivros = None):
        self.__nome = nome
        self.__curso = curso
        self.__cpf = cpf
        self.__situacao = situacao
        self.__qttLivros = qttLivros
        Usuario.idd += 1

    def getNome(self):
        return self.__nome

    def setNome(self,novo):
        self.__nome = novo

    def getCurso(self):
        return self.__curso

    def setCurso(self,novo):
        self.__curso = novo

    def getCpf(self):
        return self.__cpf

    def setCpf(self,novo):
        self.__cpf = novo

    def getSituacao(self):
        return self.__situacao

    def setSituacao(self,novo):
        self.__situacao = novo

    def getQttLivros(self):
        return self.__qttLivros

    def setQttLivros(self,novo):
        self.__qttlivros = novo

    def setIdd(self):
        Usuario.idd -= 1

    def getIdd(self):
        return Usuario.idd

    def printar(self,nome,cpf):
        print(nome,cpf)


teste = Usuario()
teste.setNome("pam")
teste.setCpf("1234445677")
print(teste.getIdd())
a = Usuario("le","vet","123456","1",2)
print(teste.getIdd())
teste.setIdd()
c = Usuario("pier","cvd","11109099009",0,0)
print(teste.getIdd())