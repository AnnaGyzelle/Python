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
    | 8 - Ativar/Desativar usuário                               |
    | 0 - Sair                                                   |
    --------------------------------------------------------------
    """
    )


def run():

    # limpar_tela()

    menu_principal()

    opcao = escolher()

    menu_principal_escolher(opcao)

    return opcao


def menu_principal_escolher(opcao):
    match opcao:
        case 1:
            usuario_inserir()
            return run()
        case 2:
            usuario_excluir()
            return run()
        case 3:
            usuario_atualizar()
            return run()
        case 4:
            usuario_consultar()
            return run()
        case 5:
            tabela(usuarios_consultar())
            return run()
        case 6:
            tabela(usuarios_ativos())
            return run()
        case 7:
            tabela(usuarios_exclidos())
            return run()
        case 8:
            usuario_ativar_desativar()
            return run()
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
