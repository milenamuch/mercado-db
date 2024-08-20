import sqlite3

from datetime import datetime

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
    
        
        """Criando a tabela de produtos"""
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produto (
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            quantidade_disponivel INTEGER,
            preco FLOAT,
            id_fornecedor INTEGER,
            id_categoria INTEGER,
            FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor)
            FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
        );
        ''')
        
        """Criando a tabela de transações"""
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
    
        """Commit para salvamento e fechamento da conexão"""
        conn.commit()
        conn.close()
        
        
    """ - - - CATEGORIA - - - """
    def adicionar_categoria(self, nome):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO categoria (nome) VALUES (?)
        ''', (nome,))

        conn.commit()
        conn.close()
    
    def listar_categorias(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM categoria
        ''')

        conn.commit()
        return cursor.fetchall()

    def remover_categoria(self, id_categoria):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        DELETE FROM categoria WHERE id_categoria = ?
        ''', (id_categoria,))
        conn.commit()
        conn.close()
        
    def alterar_categoria(self, id_categoria, novo_nome):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE categoria SET nome = ? WHERE id_categoria = ?
        ''', (novo_nome, id_categoria))
        conn.commit()
        conn.close()
        

    """ - - - FORNECEDOR - - - """
    
    def adicionar_fornecedor(self, nome):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO fornecedor (nome) VALUES (?)
        ''', (nome,))
        
        conn.commit()   
        conn.close()
        
    
    
    def listar_fornecedores(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM fornecedor
        ''')
        
        return cursor.fetchall()
    
    def remover_fornecedor(self, id_fornecedor):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        DELETE FROM fornecedor WHERE id_fornecedor = ?
        ''', (id_fornecedor,))
        
        conn.commit()
        conn.close()
        
    def alterar_fornecedor(self, id_fornecedor, novo_nome):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE fornecedor SET nome = ? WHERE id_fornecedor = ?
        ''', (novo_nome, id_fornecedor))
        
        conn.commit()
        conn.close()
    
    
    """ - - - PRODUTO - - - """
    def adicionar_produto(self, nome, quantidade_disponivel, preco, id_fornecedor, id_categoria):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO produto (nome, quantidade_disponivel, preco, id_fornecedor, id_categoria) VALUES (?, ?, ?, ?, ?)
        ''', (nome, quantidade_disponivel, preco, id_fornecedor, id_categoria))
        
        conn.commit()
        conn.close()
    
    def listar_produtos(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM produto
        ''')
        
        return cursor.fetchall()
    
    def remover_produto(self, id_produto):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        DELETE FROM produto WHERE id_produto = ?
        ''', (id_produto,))
        
        conn.commit()
        conn.close()
    
    def alterar_nome_produto(self, id_produto, nome):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        UPDATE produto SET nome = ? WHERE id_produto = ?
        ''', (nome, id_produto))
        
        conn.commit()
        conn.close()
        
    def alterar_preco_produto(self, id_produto, preco):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        UPDATE produto SET preco = ? WHERE id_produto = ?
        ''', (preco, id_produto))
        
        conn.commit()
        conn.close()
    
    def alterar_quantidade_produto(self, id_produto, quantidade):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        UPDATE produto SET quantidade_disponivel = ? WHERE id_produto = ?
        ''', (quantidade, id_produto))
        
        conn.commit()
        conn.close()
        
        
    def alterar_categoria_produto(self, id_produto, categoria):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        UPDATE produto SET id_categoria = ? WHERE id_produto = ?
        ''', (categoria, id_produto))
        
        conn.commit()
        conn.close()
    
    def alterar_fornecedor_produto(self, id_produto, fornecedor):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        UPDATE produto SET id_fornecedor = ? WHERE id_produto = ?
        ''', (fornecedor, id_produto))
        
        conn.commit()
        conn.close()
    
    """ - - - CLIENTE - - - """
    
    def adicionar_cliente(self, nome, telefone, endereco):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO cliente (nome, telefone, endereco) VALUES (?, ?, ?)
        ''', (nome, telefone, endereco))
        conn.commit()
        conn.close()

    def listar_clientes(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM cliente
        ''')
        
        return cursor.fetchall()

            
    def remover_cliente(self, id_cliente):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        DELETE FROM cliente WHERE id_cliente = ?
        ''', (id_cliente,))
        
        conn.commit()   
        conn.close()    
    
    def alterar_cliente(self, id_cliente, telefone, endereco):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        UPDATE cliente SET telefone = ?, endereco = ? WHERE id_cliente = ?
        ''', (telefone, endereco, id_cliente))
        
        conn.commit()   
        conn.close()
    
    """ - - - TRANSAÇÃO - - - """
    def realizar_transacao(self, id_cliente, id_produto, quantidade):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT preco FROM produto WHERE id_produto = ?
        ''', (id_produto,))
        
        preco = cursor.fetchone()[0]
        
        valor_total = preco * quantidade
        
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
        INSERT INTO transacao (id_cliente, id_produto, quantidade_produto, valor_total, data) VALUES (?, ?, ?, ?, ?)
        ''', (id_cliente, id_produto, quantidade, valor_total, data))
        
        cursor.execute('''
        UPDATE produto SET quantidade_disponivel = quantidade_disponivel - ? WHERE id_produto = ?
        ''', (quantidade, id_produto))
        
        conn.commit()
        conn.close()
    
        
    def listar_transacoes(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM transacao
        ''')
        
        return cursor.fetchall()
    
    def listar_produtos_em_estoque(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM produto WHERE quantidade_disponivel > 0
        ''')
        
        return cursor.fetchall()
    
    def listar_vendas_cliente(self, id_cliente):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM transacao WHERE id_cliente = ?
        ''', (id_cliente,))
        
        return cursor.fetchall()
    
    def listar_total_vendas_categoria(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT c.nome, t.valor_total FROM transacao t 
        INNER JOIN produto p ON t.id_produto = p.id_produto
        INNER JOIN  categoria c ON p.id_categoria = c.id_categoria
        ORDER BY t.valor_total DESC 
        ''')
        
        return cursor.fetchall()

    
    def listar_produtos_mais_vendidos(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT p.nome, SUM(t.valor_total) FROM transacao t 
        INNER JOIN produto p ON t.id_produto = p.id_produto 
        ORDER BY t.valor_total DESC''')
    
        return cursor.fetchall()
    
    
