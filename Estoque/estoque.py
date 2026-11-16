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
estoque_minimo = int(input("Digite o estoque mínimo: "))

#ficha produto
print()
print("-------- FICHA DO PRODUTO --------")
print("Código:", codigo)
print("Produto:", nome)
print("Preço: R$", preco)
print("Quantidade em estoque:", quantidade, "unidade(s)")
print("Estoque mínimo:", estoque_minimo)
print("----------------------------------")
