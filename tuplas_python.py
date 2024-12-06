# Inicializando a lista de estoque
estoque = []

def adicionar_item():
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade do item: "))
    preço = float(input("Digite o preço do item: "))
    item = (nome, quantidade, preço)
    estoque.append(item)
    print(f"Item {nome} adicionado com sucesso!")

def remover_item():
    nome = input("Digite o nome do item a ser removido: ")
    quantidade_remover = int(input("Digite a quantidade do item a ser removida: "))
    global estoque
    novo_estoque = []
    for item in estoque:
        if item[0] == nome:
            if item[1] > quantidade_remover:
                novo_item = (item[0], item[1] - quantidade_remover, item[2])
                novo_estoque.append(novo_item)
                quantidade_remover = 0  # Quantidade removida
            elif item[1] == quantidade_remover:
                quantidade_remover = 0  # Quantidade removida, não adicionar este item
            else:
                quantidade_remover -= item[1]  # Ainda resta quantidade para remover
        else:
            novo_estoque.append(item)
    estoque = novo_estoque # linha que de fato garante que o item foi removido, pq não adiciona na nova lista
    print(f"Item {nome} removido com sucesso!")

def exibir_itens():
    if not estoque:
        print("Estoque vazio.")
    else:
        for item in estoque:
            print(f"Nome: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]}")

while True:
    print("\n1. Adicionar um novo item")
    print("2. Remover um item")
    print("3. Exibir todos os itens do estoque")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        adicionar_item()
    elif escolha == '2':
        remover_item()
    elif escolha == '3':
        exibir_itens()
    elif escolha == '4':
        break
    else:
        print("Opção inválida, por favor escolha novamente.")

    #fim :D
