import os

class Cadastro:
    def __init__(self):
        self.administradores = {}
        self.clientes = {}

    def cadastrar_administrador(self, username, password):
        self.administradores[username] = password

    def cadastrar_cliente(self, username, password):
        self.clientes[username] = password

    def verificar_administrador(self, username, password):
        return username in self.administradores and self.administradores[username] == password

    def verificar_cliente(self, username, password):
        return username in self.clientes and self.clientes[username] == password

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade, preco=None):
        if nome in self.produtos:
            self.produtos[nome]["quantidade"] += quantidade
        else:
            self.produtos[nome] = {"quantidade": quantidade, "preco": preco}

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome]["quantidade"] >= quantidade:
                self.produtos[nome]["quantidade"] -= quantidade
                if self.produtos[nome]["quantidade"] == 0:
                    del self.produtos[nome]
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado no estoque.")

    def listar_estoque(self):
        print("Produtos em estoque:")
        for produto, info in self.produtos.items():
            print(f"{produto}: Quantidade: {info['quantidade']}, Preço: {info['preco']:.2f}")

def menu_administrador(cadastro, estoque):
    print("Menu do Administrador")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Listar Estoque")
    print("4 - Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        os.system("cls" if os.name == "nt" else "clear")
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        preco = float(input("Digite o preço do produto: "))
        estoque.adicionar_produto(nome, quantidade, preco)
        print("Produto adicionado com sucesso!")
        input("Pressione Enter para continuar...")
        menu_administrador(cadastro, estoque)
    elif opcao == "2":
        os.system("cls" if os.name == "nt" else "clear")
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a ser removida: "))
        estoque.remover_produto(nome, quantidade)
        print("Produto removido com sucesso!")
        input("Pressione Enter para continuar...")
        menu_administrador(cadastro, estoque)
    elif opcao == "3":
        os.system("cls" if os.name == "nt" else "clear")
        estoque.listar_estoque()
        input("Pressione Enter para continuar...")
        menu_administrador(cadastro, estoque)
    elif opcao == "4":
        print("Saindo...")
    else:
        print("Opção inválida.")

def menu_cliente(estoque):
    print("Menu do Cliente")
    print("1 - Comprar Produto")
    print("2 - Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        os.system("cls" if os.name == "nt" else "clear")
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a ser comprada: "))
        if nome in estoque.produtos and quantidade <= estoque.produtos[nome]["quantidade"]:
            valor_total = quantidade * estoque.produtos[nome]["preco"]
            print(f"Valor total da compra: R${valor_total:.2f}")
            estoque.remover_produto(nome, quantidade)
            print("Compra realizada com sucesso!")
        else:
            print("Desculpe, produto ou quantidade indisponível.")
        input("Pressione Enter para continuar...")
        menu_cliente(estoque)
    elif opcao == "2":
        print("Saindo...")
    else:
        print("Opção inválida.")

def menu_inicial(cadastro, estoque):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Bem-vindo! Por favor, escolha uma opção:")
        print("1 - Login como Administrador")
        print("2 - Login como Cliente")
        print("3 - Cadastrar Administrador")
        print("4 - Cadastrar Cliente")
        print("5 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            if cadastro.verificar_administrador(username, password):
                menu_administrador(cadastro, estoque)
            else:
                print("Credenciais inválidas.")
        elif opcao == "2":
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            if cadastro.verificar_cliente(username, password):
                menu_cliente(estoque)
            else:
                print("Credenciais inválidas.")
        elif opcao == "3":
            username = input("Digite o nome de usuário para cadastro: ")
            password = input("Digite a senha para cadastro: ")
            cadastro.cadastrar_administrador(username, password)
            print("Administrador cadastrado com sucesso!")
        elif opcao == "4":
            username = input("Digite o nome de usuário para cadastro: ")
            password = input("Digite a senha para cadastro: ")
            cadastro.cadastrar_cliente(username, password)
            print("Cliente cadastrado com sucesso!")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Criar instância de Cadastro e Estoque
cadastro = Cadastro()
estoque = Estoque()

# Iniciar o menu inicial
menu_inicial(cadastro, estoque)
