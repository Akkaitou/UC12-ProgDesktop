# ============================================
#  TechStock - Controle de estoque TechPoint
#  Aluno(a): Raul CM
# ============================================

print("Bem-vindo ao TechStock - Controle de Estoque TechPoint")

#cadastro do produto
codigo = input("Digite o código do produto: ")
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade em estoque: "))
estoque_minimo = 5

# validação do cadastro
if preco > 0 and quantidade >= 0 and estoque_minimo > 0:
    print("Cadastro válido!")

    # menu de operações
    print()
    print("O que você deseja fazer?")
    print("[1] Registrar entrada (chegou mercadoria)")
    print("[2] Registrar saída (venda)")
    print("[3] Apenas consultar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        entrada = int(input("Quantas unidades chegaram? "))
        if entrada > 0:
            quantidade = quantidade + entrada
            print("Entrada registrada:", entrada, "unidade(s).")
        else:
            print("ERRO: a quantidade de entrada precisa ser maior que zero.")
    elif opcao == "2":
        saida = int(input("Quantas unidades foram vendidas? "))
        if saida <= 0:
            print("ERRO: a quantidade de saída precisa ser maior que zero.")
        elif saida > quantidade:
            print("ERRO: estoque insuficiente. Disponível:", quantidade)
        else:
            quantidade = quantidade - saida
            print("Saída registrada:", saida, "unidade(s).")
    elif opcao == "3":
        print("Consulta selecionada.")
    else:
        print("Opção inválida. Mostrando apenas a ficha do produto.")

    # cálculos
    valor_total_estoque = preco * quantidade
    valor_total_estoque = round(valor_total_estoque, 2)

    # ficha produto
    print()
    print("-------- FICHA DO PRODUTO --------")
    print("Código:", codigo)
    print("Produto:", nome)
    print("Preço: R$", preco)
    print("Quantidade em estoque:", quantidade, "unidade(s)")
    print("Estoque mínimo:", estoque_minimo)
    print("Valor total em estoque: R$", valor_total_estoque)
    if quantidade == 0:
        print("Situação: ATENÇÃO: Sem estoque!")
    elif quantidade < estoque_minimo:
        faltam = estoque_minimo - quantidade
        print("ESTOQUE BAIXO, faltam", faltam)
    else:
        print("ESTOQUE OK")
    print("----------------------------------")
else:
    print("ERRO: cadastro inválido.")
    print("O preço e o estoque mínimo devem ser maiores que zero, e a quantidade não pode ser negativa.")
