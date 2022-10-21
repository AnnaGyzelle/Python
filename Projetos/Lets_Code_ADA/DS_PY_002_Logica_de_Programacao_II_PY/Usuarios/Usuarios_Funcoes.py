import os, json, time

# from tabulate import tabulate

# from Main import *

# caminho = os.path.abspath("Usuarios_arquivo.json")
# print(os.getcwd())
# print(caminho)
# os.path.join(os.getcwd(),"dados\contatos.json")
# os.path.join(os.path.dirname(__file__), "Usuarios.json")
# caminho = "h:\\Meu Drive\\Estudos\\Programação\\Python\\Lets_Code\\Git\\Python\\Projetos\\Lets_Code_ADA\\DS_PY_002_Logica_de_Programacao_II_PY\\Dados\\Usuarios.json"

CAMINHO = "DS_PY_002_Logica_de_Programacao_II_PY\\Dados\\Usuarios.json"
caminho = os.path.join(os.getcwd(), CAMINHO)


def usuarios_arquivo_ler():
    with open(caminho, "r", encoding="utf-8") as arquivo:
        usuarios_dicionario = json.load(arquivo)
    return usuarios_dicionario


def usuarios_gravar_arquivo(usuarios_dicionario):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios_dicionario, arquivo, indent=4, ensure_ascii=False)
    return usuarios_dicionario


def usuarios_consultar():
    return usuarios_arquivo_ler()


def usuario_infomacoes(nome: str):
    for id, usuario in usuarios_consultar().items():
        if usuario["Nome"] == nome:
            return id, usuario
    return None


def usuario_pedir_nome():
    nome = input("Digite o nome do usuario: ")
    return nome


def usuario_pedir_telefone():
    telefone = input("Digite o telefone do usuario: ")
    return telefone


def usuario_pedir_endereco():
    endereco = input("Digite o endereço do usuario: ")
    return endereco


def usuario_consultar():
    nome = usuario_pedir_nome()

    if usuario_infomacoes(nome) != None:
        print(f"\nUsuario: {usuario_infomacoes(nome)}")
        return usuario_infomacoes(nome)
    print(f"Usuário {nome} não encontrado!")


def usuario_inserir(
    telefone: str = "Nao Informado",
    endereco: str = "Nao Informado",
):
    nome = usuario_pedir_nome()
    while not nome:
        nome = usuario_pedir_nome()
    telefone = usuario_pedir_telefone() or "Não informado"
    endereco = usuario_pedir_endereco() or "Não informado"
    usuarios_dicionario = usuarios_consultar()
    usuarios_dicionario[str(len(usuarios_dicionario) + 1)] = {
        "Status": True,
        "Nome": nome,
        "Telefone": telefone,
        "Endereço": endereco,
    }
    usuarios_gravar_arquivo(usuarios_dicionario)
    print("\nAdiconado com sucesso.")
    return usuarios_consultar()


def escolher():
    opcao = int(input("Escolha uma, entre as opções acima: "))
    return opcao


def menu_atualizar():
    print(
        """
    -----------------------------------
    |        Funcionalidades:         |
    |                                 |
    | 1 - Ativar/Desativar usuário    |
    | 2 - Atualizar nome              |
    | 3 - Atualizar telefone          |
    | 4 - Atualizar endereço          |
    | 5 - Atualizar cadastro completo |
    ___________________________________
    """
    )


def menu_atualizar_ecolher(opcao, id):
    usuarios = usuarios_consultar()
    match opcao:
        case 1:
            usuario_ativar_desativar()
        case 2:
            nome = usuario_pedir_nome()
            usuarios[id]["Nome"] = nome
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case 3:
            telefone = usuario_pedir_telefone()
            usuarios[id]["Telefone"] = telefone
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case 4:
            endereco = usuario_pedir_endereco()
            usuarios[id]["Endereço"] = endereco
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case 5:
            nome = usuario_pedir_nome()
            endereco = usuario_pedir_endereco()
            telefone = usuario_pedir_telefone()
            usuarios[id] = {
                "Status": True,
                "Nome": nome,
                "Telefone": telefone,
                "Endereço": endereco,
            }
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case _:
            print("\n-------------------------------------------------")
            print("| Opção inválida, escolha uma das opções acima. |")
            print("-------------------------------------------------\n")
            time.sleep(3)
            return escolher()


def usuario_atualizar():
    id, _ = usuario_consultar()
    menu_atualizar()
    opcao = escolher()
    menu_atualizar_ecolher(opcao, id)


def usuario_excluir():
    usuarios = usuarios_consultar()
    id, usuario = usuario_consultar()
    usuarios[id]["Status"] = False
    usuarios_gravar_arquivo(usuarios)
    return print(f"\nUsuário {usuario['Nome']} desativado com sucesso")


def usuarios_ativos():
    ativos = {}
    for id, usuario in usuarios_consultar().items():
        if usuario["Status"] == True:
            ativos[id] = usuario
    return print(ativos)


def usuarios_exclidos():
    desativados = {}
    for id, usuario in usuarios_consultar().items():
        if usuario["Status"] == False:
            desativados[id] = usuario
    return print(desativados)


def usuario_ativar_desativar():
    id, usuario = usuario_consultar()
    usuarios = usuarios_consultar()
    if usuarios[id]["Status"] == True:
        usuarios[id]["Status"] = False
        usuarios_gravar_arquivo(usuarios)
    else:
        usuarios[id]["Status"] = True
        usuarios_gravar_arquivo(usuarios)

    print(f"\nUsuario: {usuario_infomacoes(usuario['Nome'])}\n")
    return print("Status do usuario alterado com sucesso.")


# def tabela(id, usuario):
#     tabela = []
#     headers = ["NOME", "TELEFONE", "ENDEREÇO"]
#     tabela.append(
#         [
#             id,
#             usuario[id]["Status"],
#             usuario[id]["Nome"],
#             usuario[id]["Telefone"],
#             usuario[id]["Endereço"],
#         ]
#     )
#     print(tabulate(tabela, headers, tablefmt="simple_grid"))
