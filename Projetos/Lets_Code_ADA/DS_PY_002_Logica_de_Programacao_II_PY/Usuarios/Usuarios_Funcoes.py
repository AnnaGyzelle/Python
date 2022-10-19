import json, time

# from Main import *

# caminho = os.path.abspath("Usuarios_arquivo.json")
# print(os.getcwd())
# print(caminho)
# os.path.join(os.getcwd(), 'Usuarios_arquivo.json')
# os.path.join(os.path.dirname(__file__), "Usuarios.json")

CAMINHO = "h:\\Meu Drive\\Estudos\\Programação\\Python\\Lets_Code\\Git\\Python\\Projetos\\Lets_Code_ADA\\DS_PY_002_Logica_de_Programacao_II_PY\\Dados\\Usuarios.json"


def usuarios_arquivo_ler():
    with open(CAMINHO, "r") as arquivo:
        usuarios_dicionario = json.load(arquivo)

    return usuarios_dicionario


def usuarios_gravar_arquivo(usuarios_dicionario):
    with open(CAMINHO, "w") as arquivo:
        json.dump(usuarios_dicionario, arquivo, indent=4)


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
    endereco = input("Digite o endereco do usuario: ")
    return endereco


def usuario_consultar():
    nome = usuario_pedir_nome()

    if usuario_infomacoes(nome) != None:
        print(f"\nUsuario: {usuario_infomacoes(nome)}")
        return usuario_infomacoes(nome)
    print(f"Usuário {nome} não encontrado!")


def usuario_inserir(
    nome: str,
    telefone: str = "Nao Informado",
    endereco: str = "Nao Informado",
):
    nome = usuario_pedir_nome()
    telefone = usuario_pedir_telefone()
    endereco = usuario_pedir_endereco()
    usuarios_dicionario = usuarios_consultar()
    usuarios_dicionario[str(len(usuarios_dicionario) + 1)] = {
        "Status": True,
        "Nome": nome,
        "Telefone": telefone,
        "Endereco": endereco,
    }
    usuarios_gravar_arquivo(usuarios_dicionario)
    print("Adiconado com sucesso.")
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
    | 1 - Atualizar nome              |
    | 2 - Atualizar telefone          |
    | 3 - Atualizar endereço          |
    | 4 - Atualizar cadastro completo |
    ___________________________________
    """
    )


def menu_atualizar_ecolher(opcao, id):
    usuarios = usuarios_consultar()
    match opcao:
        case 1:
            nome = usuario_pedir_nome()
            usuarios[id]["Nome"] = nome
            usuarios_gravar_arquivo(usuarios)
            return "Alterado com sucesso."
        case 2:
            telefone = usuario_pedir_telefone()
            usuarios[id]["Telefone"] = telefone
            usuarios_gravar_arquivo(usuarios)
            return "Alterado com sucesso."
        case 3:
            endereco = usuario_pedir_endereco()
            usuarios[id]["Endereco"] = endereco
            usuarios_gravar_arquivo(usuarios)
            return "Alterado com sucesso."
        case 4:
            nome = usuario_pedir_nome()
            endereco = usuario_pedir_endereco()
            telefone = usuario_pedir_telefone()
            usuarios[id] = {
                "Status": True,
                "Nome": nome,
                "Telefone": telefone,
                "Endereco": endereco,
            }
            usuarios_gravar_arquivo(usuarios)
            return "Alterado com sucesso."
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
    return print(f"Usuário {usuario['Nome']} desativado com sucesso")


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
