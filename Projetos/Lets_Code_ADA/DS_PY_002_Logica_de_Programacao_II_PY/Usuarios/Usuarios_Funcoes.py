def usuarios_lista_ler_gravar(gravar=False):
    import json

    if gravar == False:
        with open("usuarios_lista.json", encoding="utf-8") as arquivo:
            usuarios_lista = json.load(arquivo)

    with open("usuarios_lista.json", "w") as arquivo:
        json.dump(usuarios_lista, "usuarios_lista.json", indent=4)

    return usuarios_lista


def usuario_inserir():
    pass


def usuario_excluir():
    pass


def usuario_atualizar():
    pass


def usuario_infomacoes():
    pass


def usuarios_consultar():
    print(usuarios_lista_ler_gravar())
