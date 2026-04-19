import json

def carregar_dados():
    try:
        with open("produtos.json", "r") as f:
            dados = json.load(f)
            # converter chave de string para int
            return {int(k): v for k, v in dados.items()}
    except:
        return {}

def salvar_dados():
    with open("produtos.json", "w") as f:
        json.dump(produtos, f, indent=4)

produtos = carregar_dados()

def cadastrar_produto():
    try:
        codigo = int(input("Código: "))

        if codigo in produtos:
            print("Já existe um produto com esse código!")
            return

        nome = input("Nome: ")
        preco = float(input("Preço: ").replace(",", "."))
        quantidade = int(input("Quantidade: "))

        produtos[codigo] = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        salvar_dados()
        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Entrada inválida!")


def listar_produtos():
    if not produtos:
        print(" Nenhum produto cadastrado.")
        return

    print("\n PRODUTOS CADASTRADOS:")
    for codigo, p in produtos.items():
        print(f"""
Código: {codigo}
Nome: {p['nome']}
Preço: R$ {p['preco']:.2f}
Quantidade: {p['quantidade']}
------------------------""")

def buscar_produto():
    print("\nBuscar por:")
    print("1 - Código")
    print("2 - Nome")

    opcao = input("Escolha: ")

    if opcao == "1":
        try:
            codigo = int(input("Digite o código: "))

            if codigo in produtos:
                p = produtos[codigo]
                print(f"""
Produto encontrado:
Código: {codigo}
Nome: {p['nome']}
Preço: R$ {p['preco']:.2f}
Quantidade: {p['quantidade']}
""")
            else:
                print("Produto não encontrado!")

        except ValueError:
            print("Código inválido!")

    elif opcao == "2":
        nome_busca = input("Digite o nome do produto: ").lower()

        encontrados = False

        for codigo, p in produtos.items():
            if nome_busca in p["nome"].lower():
                print(f"""
Produto encontrado:
Código: {codigo}
Nome: {p['nome']}
Preço: R$ {p['preco']:.2f}
Quantidade: {p['quantidade']}
""")
                encontrados = True

        if not encontrados:
            print("Nenhum produto encontrado com esse nome!")

    else:
        print("Opção inválida!")


def atualizar_produto():
    try:
        codigo = int(input("Código do produto: "))

        if codigo in produtos:
            print("Deixe vazio para não alterar o produto.")

            nome = input("Novo nome: ")
            preco = input("Novo preço: ")
            quantidade = input("Nova quantidade: ")

            if nome:
                produtos[codigo]["nome"] = nome
            if preco:
                produtos[codigo]["preco"] = float(preco.replace(",", "."))
            if quantidade:
                produtos[codigo]["quantidade"] = int(quantidade)

            salvar_dados()
            print("Produto atualizado!")

        else:
            print("Produto não encontrado!")

    except ValueError:
        print("Entrada inválida!")


def excluir_produto():
    try:
        codigo = int(input("Código: "))

        if codigo in produtos:
            p = produtos[codigo]

            print(f"""
Produto:
Nome: {p['nome']}
Preço: R$ {p['preco']:.2f}
Quantidade: {p['quantidade']}
""")

            confirm = input("Tem certeza que deseja excluir? (s/n): ").strip().lower()

            if confirm == "s":
                del produtos[codigo]
                salvar_dados()
                print("Produto excluído!")
            else:
                print("Exclusão cancelada!")

        else:
            print("Produto não encontrado!")

    except ValueError:
        print("Código inválido!")


def menu():
    while True:
        print("""
===== MENU =====
1 - Cadastrar Produto
2 - Listar Produtos
3 - Buscar Produto
4 - Atualizar Produto
5 - Excluir Produto
0 - Sair
""")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            atualizar_produto()
        elif opcao == "5":
            excluir_produto()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()