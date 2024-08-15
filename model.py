import sqlite3

class Banco:
    def __init__(self, banco_nome='mercado.db'):
        self.banco_nome = banco_nome
    
    def _connect(self):
        return sqlite3.connect(self.banco_nome)
    
    def criar_tabelas(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        """Criando a tabela de clientes"""
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            telefone VARCHAR(20),
            endereco VARCHAR(100)
        );
        ''')
        
        """Criando a tabela de fornecedores"""
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS fornecedor (
            id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL
        );
        ''')
        
        """Criando a tabela de categorias"""
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS categoria (
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL
        );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produto (
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            quantidade_disponivel INTEGER,
            preco FLOAT,
            id_fornecedor INTEGER,
            FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor)
        );
        ''')
        
        """Criando a tabela intermediária entre produtos e categorias"""
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produto_categoria (
            id_produto INTEGER,
            id_categoria INTEGER,
            FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
            FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
        );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacao (
            id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER,
            id_produto INTEGER,
            quantidade_produto INTEGER,
            valor_total FLOAT,
            data DATE,
            FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
            FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
        );
        ''')
        
        conn.commit()
        conn.close()
        
    