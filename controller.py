from model import Banco

class Controller:
    def __init__(self, banco):
        self.banco = banco
        
    def criar_tabelas(self):
        self.banco.criar_tabelas()

# - - - CATEGORIA - - - #
    def adicionar_categoria(self, nome):
        if nome == "":
            print("Nome da categoria não pode ser vazio")
        else:
            self.banco.adicionar_categoria(nome)
        
    def listar_categorias(self):
        categorias = self.banco.listar_categorias()
        for categoria in categorias:
            print(categoria)
            
    def remover_categoria(self, id_categoria):
        if id_categoria == "":
            print("Id da categoria não pode ser vazio")
        self.banco.remover_categoria(id_categoria)
    
    def alterar_categoria(self, id_categoria, novo_nome):
        if id_categoria == "":
            print("Id da categoria não pode ser vazio")
        elif novo_nome == "":
            print("Nome da categoria não pode ser vazio")
        else:
            self.banco.alterar_categoria(id_categoria, novo_nome)
    

# - - - FORNECEDOR - - - #
    
    def adicionar_fornecedor(self, nome):
        self.banco.adicionar_fornecedor(nome)
    
    def listar_fornecedores(self):
        fornecedores = self.banco.listar_fornecedores()
        for fornecedor in fornecedores:
            print(fornecedor)
    
    def remover_fornecedor(self, id_fornecedor):
        if id_fornecedor == "":
            print("Id do fornecedor não pode ser vazio")
        self.banco.remover_fornecedor(id_fornecedor)
        
    def alterar_fornecedor(self, id_fornecedor, novo_nome):
        if id_fornecedor == "":
            print("Id do fornecedor não pode ser vazio")
        elif novo_nome == "":
            print("Nome do fornecedor não pode ser vazio")
        else:
            self.banco.alterar_fornecedor(id_fornecedor, novo_nome)
    

# - - - PRODUTO - - - #

    def adicionar_produto(self, nome, quantidade_disponivel, preco, id_fornecedor, id_categoria):
        self.banco.adicionar_produto(nome, quantidade_disponivel, preco, id_fornecedor, id_categoria)
        
    def listar_produtos(self):
        produtos = self.banco.listar_produtos()
        for produto in produtos:
            print(produto)
    
    def adicionar_cliente(self, nome, telefone, endereco):
        self.banco.adicionar_cliente(nome, telefone, endereco)
        
    def remover_produto(self, id_produto):
        if id_produto == "":
            print("Id do produto não pode ser vazio")
        self.banco.remover_produto(id_produto)
        
    def alterar_nome_produto(self, id_produto, novo_nome):
        if id_produto == "":
            print("Id do produto não pode ser vazio")
        elif novo_nome == "":
            print("Nome do produto não pode ser vazio")
        else:
            self.banco.alterar_nome_produto(id_produto, novo_nome)
    
    def alterar_preco_produto(self, id_produto, novo_preco):
        if id_produto == "":
            print("Id do produto não pode ser vazio")
        elif novo_preco == "":
            print("O preço do produto não pode ser vazio")
        else:
            self.banco.alterar_preco_produto(id_produto, novo_preco)
        
    def alterar_quantidade_produto(self, id_produto, nova_quantidade):
        if id_produto == "":
            print("Id do produto não pode ser vazio")
        elif nova_quantidade == "":
            print("A quantidade do produto não pode ser vazio")
        else:
            self.banco.alterar_quantidade_produto(id_produto, nova_quantidade)
    
    def alterar_categoria_produto(self, id_produto, nova_categoria):
        if id_produto == "":
            print("Id do produto não pode ser vazio")
        elif nova_categoria == "":
            print("A categoria do produto não pode ser vazio")
        else:
            self.banco.alterar_categoria_produto(id_produto, nova_categoria)
    
    def alterar_fornecedor_produto(self, id_produto, novo_fornecedor):
        if id_produto == "":
            print("Id do produto não pode ser vazio")
        elif novo_fornecedor == "":
            print("A fornecedor do produto não pode ser vazio")
        else:
            self.banco.alterar_fornecedor_produto(id_produto, novo_fornecedor)
    
    
# - - - CLIENTE - - - #
    
    def adicionar_cliente(self, nome, telefone, endereco):
        self.banco.adicionar_cliente(nome, telefone, endereco)
    
    def listar_clientes(self):
        clientes = self.banco.listar_clientes()
        for cliente in clientes:
            print(cliente)
    
    def remover_cliente(self, id_cliente):
        if id_cliente == "":
            print("Id do cliente não pode ser vazio")
        self.banco.remover_cliente(id_cliente)
        
    def alterar_cliente(self, id_cliente, novo_telefone, novo_endereco):
        if id_cliente == "":
            print("Id do cliente não pode ser vazio")
        elif novo_telefone == "":
            print("Telefone do cliente não pode ser vazio")
        elif novo_endereco == "":
            print("Endereço do cliente não pode ser vazio")
        else:
            self.banco.alterar_cliente(id_cliente, novo_telefone, novo_endereco)
    
    
    
# - - - TRANSAÇÃO - - - #

    def realizar_transacao(self, id_cliente, id_produto, quantidade):
        self.banco.realizar_transacao(id_cliente, id_produto, quantidade)
    
    def listar_transacoes(self):
        transacoes = self.banco.listar_transacoes()
        for transacao in transacoes:
            print(transacao)
    
    
# - - - RELATÓRIOS - - - #
    
    def listar_produtos_em_estoque(self):
        produtos = self.banco.listar_produtos_em_estoque()
        for produto in produtos:
            print(produto)
    
    def listar_vendas_cliente(self, id_cliente):
        vendas_cliente = self.banco.listar_vendas_cliente(id_cliente)
        for venda in vendas_cliente:
            print(venda)

    def listar_total_vendas_categoria(self):
        categorias = self.banco.listar_total_vendas_categoria()
        for categoria in categorias:
            print(categoria)

    def listar_produtos_mais_vendidos(self):
        produtos = self.banco.listar_produtos_mais_vendidos()
        for produto in produtos:
            print(produto)
    
    

    
        
    