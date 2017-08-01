from ArvoreVP import *
class Interface:
    def __init__(self, arvoreUser,arvoreLivro):
        self.__usuario = arvoreUser
        self.__livro = arvoreLivro

    def emprestimoCheck(self,userKey,livroKey):
        usuario = self.__usuario.busca(userKey)
        livro = self.__livro.busca(livroKey)
        if usuario != None and livro != None:
            if usuario.getSituacao():
                if livro.getQtddExemplar()<3:
                    if len(usuario.getListaLivros())<5:
                       return True
                    else:
                        print("usuario já atingiu a quantidade máxima de empréstimos")
                        return False
                else:
                    print("O Livro Solicitado pelo usuário não possui exemplares disponíveis para emprestimo")
                    return False
            else:
                print("Usuario está com pendência na biblioteca")
                return False
        else:
            if usuario == None:
                print("Usuário não encontrado...Tente novamente")
            elif livro == None:
                print("Livro não encontrado... Tente novamente")
            return False

    def emprestimo(self,userKey, livroKey):
        usuario = self.__usuario.busca(userKey)
        livro = self.__livro.busca(userKey)
        if self.emprestimoCheck(userKey,livroKey):
            if len(usuario.getListaLivros()) == 4:
                usuario.setEMlistaLivros(livro)
                livro.setExemplar()
                usuario.setSituacao(False)
                return "O emprestimo do livro: %s foi realizado com sucesso.\n" \
                       "O usuario atingiu o limite máximo de emprestimos.\n" \
                       "Para realizar mais emprestimos, devolva algum livro."%livro.getTitulo()
            else:
                usuario.setEMlistaLivros(livro)
                livro.setExemplar()
                return "O emprestimo do livro: %s foi realizado com sucesso.\n" \
                       "O usuário tem %i livros emprestados pela biblioteca.\n" \
                       "Para realizar mais emprestimos, devolva algum livro."%(livro.getTitulo(),usuario.getQttLivros())

        else:
            return self.menu() #METODO MENU É OBVIAMENTE O MENU

    def devolucao(self, userKey, livroKey):
        usuario = self.__usuario.busca(userKey)
        livro = self.__livro.busca(livroKey)
        if usuario!= None and livro!=None:
            if livro in usuario.getListaLivros():
                usuario.removeLivroListaLivros(livro)
                livro.setExemplar(1)
                return "Devolução realizada com sucesso."
            else:
                return "O usuário não pode devolver um livro que não possui"
        else:
            if usuario==None:
                print("Usuário não cadastrado")
            elif livro==None:
                print("Livro não cadastrado")
            return self.menu()
