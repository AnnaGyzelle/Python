import os, time

from DS_PY_002_Logica_de_Programacao_II_PY.Usuarios.Usuarios_Funcoes import *


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

    opcao = int(input("Escolha uma, entre as opções acima: "))

    opcao = menu_principal_escolher(opcao)

    return opcao


def menu_principal_escolher(opcao):
    match opcao:
        case 1:
            # return usuario_inserir()
            return print("1")
        case 2:
            # return usuario_excluir()
            return print("2")
        case 3:
            # return usuario_atualizar()
            return print("3")
        case 4:
            # return usuario_infomacoes()
            return print("4")
        case 5:
            # return usuarios_consultar()
            return print("5")
        case 6:
            pass
        case 7:
            pass
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


run()
