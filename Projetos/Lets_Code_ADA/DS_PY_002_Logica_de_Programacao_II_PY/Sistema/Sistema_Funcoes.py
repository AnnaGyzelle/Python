import os, time

from Usuarios.Usuarios_Funcoes import *


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    pass


def menu_principal():
    return print(
        f""" 
    --------------------------------------------------------------
    | Boas vindo(a) ao nosso sistema de cadastro de usuário(a):  |
    |                                                            |
    | 1 - Inserir usuário                                        |   
    | 2 - Excluir usuário                                        |   
    | 3 - Atualizar usuário                                      |   
    | 4 - Informações de um usuário                              |
    | 5 - Informações de todos os usuários                       |
    | 6 - Informações de todos os usuários ativos                |
    | 7 - Informações de todos os usuários excluídos             |
    | 0 - Sair                                                   |
    --------------------------------------------------------------
    """
    )


def run():

    limpar_tela()

    menu_principal()

    opcao = escolher()

    menu_principal_escolher(opcao)

    return opcao


def menu_principal_escolher(opcao):
    match opcao:
        case 1:
            return usuario_inserir()
        case 2:
            return usuario_excluir()
        case 3:
            return usuario_atualizar()
        case 4:
            return usuario_consultar()
        case 5:
            return usuarios_consultar()
        case 6:
            return usuarios_ativos()
        case 7:
            return usuarios_exclidos()
        case 0:
            return sistema_sair()
        case _:
            print("\n-------------------------------------------------")
            print("| Opção inválida, escolha uma das opções acima. |")
            print("-------------------------------------------------\n")
            time.sleep(3)
            return run()


def sistema_sair():
    print("\n------------------")
    print("| Até a próxima. |")
    print("------------------\n")
    pass
