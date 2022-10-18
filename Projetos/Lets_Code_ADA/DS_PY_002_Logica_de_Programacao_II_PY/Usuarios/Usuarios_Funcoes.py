import json


def usuarios_arquivo_ler():

    with open("Usuarios_arquivo.json", encoding="utf-8") as arquivo:
        usuarios_dicionario = json.load(arquivo)

    return usuarios_dicionario


def usuarios_gravar_arquivo(dicionario):

    with open("Usuarios_arquivo.json", "w", indent=4) as arquivo:
        json.dump(dicionario, arquivo, indent=4)


def usuarios_consultar(imprimir=False):
    """Coloque 'True' como parametro para imprimir todos usuarios."""
    if imprimir == True:
        print(usuarios_arquivo_ler())

    usuarios_dicionario = usuarios_arquivo_ler()
    return usuarios_dicionario


def usuario_consultar():
    nome = input("Digite o nome do usuário: ")

    for id, usuario in usuarios_consultar().items():
        if usuario["Nome"] == nome:
            return id, usuario
    print(f"Usuário {nome} não encontrado!")


def usuario_infomacoes(nome: str):
    for id, usuario in usuarios_consultar().items():
        if usuario["Nome"] == nome:
            return f"""
            Id: {id},
            Status: {usuario['Status']},
            Nome: {usuario['Nome']},
            Telefone: {usuario['Telefone']},
            Endereço: {usuario['Endereço']}
            """


def usuario_inserir(nome: str, telefone: str, endereco: str):
    usuarios_dicionario = usuarios_consultar()
    usuarios_dicionario[str(len(usuarios_dicionario) + 1)] = {
        "Status": True,
        "Nome": nome,
        "Telefone": telefone,
        "Endereço": endereco,
    }
    return usuarios_dicionario


def usuario_atualizar():
    pass


def usuario_excluir():
    pass


def usuarios_ativos():
    pass


def usuarios_exclidos():
    pass
