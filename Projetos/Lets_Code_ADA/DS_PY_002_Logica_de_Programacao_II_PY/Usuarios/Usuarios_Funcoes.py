import os, json, time

from tabulate import tabulate

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
    if nome.isalpha():
        return nome.title()
    else:
        print("Digite apenas LETRAS no nome.")
        return usuario_pedir_nome()


def usuario_pedir_telefone():
    telefone = input("Digite o telefone do usuario: ")
    if telefone.isdigit():
        return telefone
    else:
        print("Digite apenas NÚMEROS.")
        return usuario_pedir_telefone()


def usuario_pedir_endereco():
    endereco = input("Digite o endereço do usuario: ")
    return endereco


def usuario_consultar():
    nome = usuario_pedir_nome()
    usuario = usuario_infomacoes(nome)
    if usuario != None:
        tabela(usuario)
        return usuario
    print(f"Usuário {nome} não encontrado!")
    usuario_consultar()


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
    menu_inserir_escolher()
    return usuarios_consultar()


def menu_inserir_usuario():
    print(
        """
    -----------------------------------
    |        Funcionalidades:         |
    |                                 |
    | 1 - Inserir outro usuário       |
    | 2 - Votar ao Menu Pincipal      |
    ___________________________________
    """
    )


def menu_inserir_escolher():
    menu_inserir_usuario()
    opcao = escolher()
    match opcao:
        case 1:
            return usuario_inserir()
        case 2:
            return None


def escolher():
    opcao = input("Escolha uma, entre as opções acima: ")
    if opcao.isdigit():
        return int(opcao)
    else:
        print("Digite apenas o NÚMERO da opção escolhida.")
        return escolher()


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


def menu_atualizar_ecolher(opcao, usuario):
    id, _ = usuario
    usuarios = usuarios_consultar()
    match opcao:
        case 1:
            usuario_ativar_desativar(usuario)
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


def usuario_atualizar(usuario):
    menu_atualizar()
    opcao = escolher()
    menu_atualizar_ecolher(opcao, usuario)


def usuario_excluir():
    usuarios = usuarios_consultar()
    id, _ = usuario_consultar()
    usuarios[id]["Status"] = False
    usuarios_gravar_arquivo(usuarios)
    return print(f"\nUsuário modificado com sucesso")


def usuarios_ativos():
    ativos = {}
    for id, usuario in usuarios_consultar().items():
        if usuario["Status"] == True:
            ativos[id] = usuario
    return ativos


def usuarios_exclidos():
    inativos = {}
    for id, usuario in usuarios_consultar().items():
        if usuario["Status"] == False:
            inativos[id] = usuario
    return inativos


def usuario_ativar_desativar(usuario):
    id, _ = usuario
    usuarios = usuarios_consultar()
    if usuarios[id]["Status"] == True:
        usuarios[id]["Status"] = False
        usuarios_gravar_arquivo(usuarios)
    else:
        usuarios[id]["Status"] = True
        usuarios_gravar_arquivo(usuarios)
    tabela(usuario_infomacoes(usuario[1]["Nome"]))
    return print("Status do usuario alterado com sucesso.")


def tabela(dicionario):
    tabela = []
    headers = ["ID", "STATUS", "NOME", "TELEFONE", "ENDEREÇO"]
    if type(dicionario) == dict:
        for id, usuario in dicionario.items():
            tabela.append(
                [
                    id,
                    usuario["Status"],
                    usuario["Nome"],
                    usuario["Telefone"],
                    usuario["Endereço"],
                ]
            )
    else:
        id, usuario = dicionario
        tabela.append(
            [
                id,
                usuario["Status"],
                usuario["Nome"],
                usuario["Telefone"],
                usuario["Endereço"],
            ]
        )

    print(tabulate(tabela, headers, tablefmt="simple_grid"))
