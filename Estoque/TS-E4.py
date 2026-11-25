# ============================================
# TechStock - Controle de estoque TechPoint
# Aluno(a): Raul CM
# ============================================

produtos = []


# cadastro dos produtos
def cadastrar():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


# listagem dos produtos
def listar():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n=== PRODUTOS CADASTRADOS ===")

    for indice in range(len(produtos)):
        produto = produtos[indice]
        situacao = ""

        if produto["quantidade"] == 0:
            situacao = " | SEM ESTOQUE"

        print(f'{indice + 1} - {produto["nome"]} | '
              f'Qtd: {produto["quantidade"]} | '
              f'R$ {produto["preco"]:.2f}{situacao}')

    print("Tipos de produtos:", len(produtos))

    baixo = 0
    for indice in range(len(produtos)):
        if produtos[indice]["quantidade"] < 5:
            baixo = baixo + 1

    print("Produtos com menos de 5 unidades:", baixo)


# consulta pelo número
def consultar_numero():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    listar()
    texto = input("Digite o número do produto: ")

    if not texto.isdigit():
        print("Digite um número inteiro válido.")
        return

    numero = int(texto)

    if numero < 1 or numero > len(produtos):
        print("Produto fora da lista.")
        return

    produto = produtos[numero - 1]

    print(f'Produto: {produto["nome"]}')
    print(f'Quantidade: {produto["quantidade"]}')
    print(f'Preço: R$ {produto["preco"]:.2f}')

    valor_total = produto["quantidade"] * produto["preco"]
    print(f'Valor total em estoque: R$ {valor_total:.2f}')


# menu principal
opcao = ""

while opcao != "0":
    print()
    print("============ MENU ============")
    print("[1] Cadastrar produto")
    print("[2] Registrar entrada")
    print("[3] Registrar venda")
    print("[4] Listar produtos")
    print("[10] Consultar pelo número")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            listar()
            texto = input("Digite o número do produto: ")

            if texto.isdigit():
                numero = int(texto)

                if numero >= 1 and numero <= len(produtos):
                    produto = produtos[numero - 1]
                    entrada = int(input("Quantas unidades chegaram? "))

                    if entrada > 0:
                        produto["quantidade"] = produto["quantidade"] + entrada
                        print("Entrada registrada.")
                    else:
                        print("A quantidade precisa ser maior que zero.")
                else:
                    print("Produto fora da lista.")
            else:
                print("Digite um número inteiro válido.")

    elif opcao == "3":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            listar()
            texto = input("Digite o número do produto: ")

            if texto.isdigit():
                numero = int(texto)

                if numero >= 1 and numero <= len(produtos):
                    produto = produtos[numero - 1]

                    if produto["quantidade"] == 0:
                        print("Produto SEM ESTOQUE. Não é possível vender.")
                    else:
                        saida = int(input("Quantas unidades foram vendidas? "))

                        if saida > 0 and saida <= produto["quantidade"]:
                            produto["quantidade"] = produto["quantidade"] - saida
                            print("Venda registrada.")
                        else:
                            print("Quantidade inválida ou estoque insuficiente.")
                else:
                    print("Produto fora da lista.")
            else:
                print("Digite um número inteiro válido.")

    elif opcao == "4":
        listar()

    elif opcao == "10":
        consultar_numero()

    elif opcao == "0":
        print("Encerrando o TechStock... até logo!")

    else:
        print("Opção inválida. Tente de novo.")
