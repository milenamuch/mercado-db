from model import Banco
from controller import Controller
import os

banco = Banco()
banco.criar_tabelas()
controller = Controller(banco)


if __name__ == "__main__":
    print('Bem vindo ao sistema Mercado da Esquina')
    while True:
        os.system('clear')
        local = int(input(
            f'Escolha uma das opções:\n'
            f'[1] Categorias\n'
            f'[2] Fornecedor\n'
            f'[3] Produto\n'
            f'[4] Cliente\n'
            f'[5] Transações\n'
            f'[6] Relatórios\n'
            f'[7] Sair\n'
            f'Qual é a sua escolha? '
        ))

        #Categorias
        if local == 1:
            os.system('clear')
            print('= = = = = CATEGORIAS = = = = = ')
            while True:
                escolha = int(input(
                            f'\nEscolha uma das opções para Categorias:\n'
                            f'[1] Cadastrar\n'
                            f'[2] Remover\n'
                            f'[3] Alterar\n'
                            f'[4] Visualizar\n'
                            f'[5] Voltar ao menu principal\n'
                            f'Qual é a sua escolha? '))
                print()
                
                if escolha == 1:
                    nome_categoria = input('Digite a categoria que deseja cadastrar: ')
                    controller.adicionar_categoria(nome_categoria)
                    print(f"Categoria adicionada com sucesso!")
                    
                elif escolha == 2:
                    controller.listar_categorias()
                    print()
                    id_categoria = input('Digite o ID que deseja remover: ')
                    controller.remover_categoria(id_categoria)
                    print(f"Categoria removida com sucesso!")
                    
                elif escolha == 3:
                    controller.listar_categorias()
                    print()
                    id = input('Qual é o id da categoria? ')
                    nome_novo = input('Qual é o novo nome da categoria? ')
                    controller.alterar_categoria(id, nome_novo)
                    
                elif escolha == 4:
                    controller.listar_categorias()
                    print()
                    
                elif escolha == 5:
                    break
                else:
                    print('Escolha uma opção válida.\n')
                    continue
        
        #Fornecedor
        elif local == 2:
            os.system('clear')
            print('= = = = = FORNECEDOR = = = = = ')
            while True:
                escolha = int(input(
                            f'\nEscolha uma das opções para Fornecedor:\n'
                            f'[1] Cadastrar\n'
                            f'[2] Remover\n'
                            f'[3] Alterar\n'
                            f'[4] Visualizar\n'
                            f'[5] Voltar ao menu principal\n'
                            f'Qual é a sua escolha? '))
            
                if escolha == 1:
                    os.system('clear')
                    nome_fornecedor = input('Digite o nome do fornecedor que deseja cadastrar: ')
                    controller.adicionar_fornecedor(nome_fornecedor)
                    print(f"Fornecedor adicionado com sucesso!")
                    
                elif escolha == 2:
                    os.system('clear')
                    controller.listar_fornecedores()
                    id_fornecedor = input('Digite o id do fornecedor que deseja remover: ')
                    controller.remover_fornecedor(id_fornecedor)
                    print(f"Fornecedor removido com sucesso!")
                    
                elif escolha == 3:
                    controller.listar_fornecedores()
                    print()
                    id = input('Qual é o id do fornecedor? ')
                    nome_novo = input('Qual é o novo nome do fornecedor? ')
                    controller.alterar_fornecedor(id, nome_novo)
                    print(f"Fornecedor alterado com sucesso!")
                    
                elif escolha == 4:
                    print("- - - FORNECEDORES - - - \n")
                    controller.listar_fornecedores()
                    
                elif escolha == 5:
                    break
                else:
                    print('Escolha uma opção válida.\n')
                    continue
        
        #Produto
        elif local == 3:
            os.system('clear')
            print('= = = = = PRODUTOS = = = = = ')
            while True:
                escolha = int(input(
                            f'\nEscolha uma das opções para Produtos:\n'
                            f'[1] Cadastrar\n'
                            f'[2] Remover\n'
                            f'[3] Alterar\n'
                            f'[4] Visualizar\n'
                            f'[5] Voltar ao menu principal\n'
                            f'Qual é a sua escolha? '))
                
                if escolha == 1:
                    os.system('clear')
                    nome_produto= input('Digite o nome do produto: ')
                    quantidade_disponivel = int((input('Digite o quantidade disponível em estoque para este produto: ')))
                    preco = float(input('Digite o preco do produto: '))
                    controller.listar_fornecedores()
                    id_fornecedor = (input('Digite o ID do fornecedor: '))
                    controller.listar_categorias()
                    id_categoria = (input('Digite o ID da categoria: '))
                    
                    controller.adicionar_produto(nome_produto, quantidade_disponivel, preco,id_fornecedor, id_categoria)
                    print(f"Produto adicionado com sucesso!")
                    
                elif escolha == 2:
                    os.system('clear')
                    controller.listar_produtos()
                    id_produto = input('Digite o id do produto que deseja remover: ')
                    controller.remover_produto(id_produto)
                    print(f"Produto removido com sucesso!")
                    
                elif escolha == 3:
                    os.system('clear')
                    while True:
                        escolha_alterar = int(input(
                            f'\nEscolha uma das opções de alteração de produto:\n'
                            f'[1] Alterar nome\n'
                            f'[2] Alterar preço\n'
                            f'[3] Alterar quantidade\n'
                            f'[4] Alterar categoria\n'
                            f'[5] Alterar fornecedor\n'
                            f'[6] Voltar ao menu de produtos: '))
                        
                        if escolha_alterar == 1:
                            os.system('clear')
                            controller.listar_produtos()
                            id = input('Qual é o id do produto? ')
                            novo_nome = input('Qual é o novo nome do produto? ')
                            controller.alterar_nome_produto(id, novo_nome)
                            print(f"Produto alterado com sucesso!")
                            
                        elif escolha_alterar == 2:
                            os.system('clear')
                            controller.listar_produtos()
                            id = input('Qual é o id do produto? ')
                            novo_preco = input('Qual é o novo preço do produto? ')
                            controller.alterar_preco_produto(id, novo_preco)
                            print(f"Produto alterado com sucesso!")
                            
                        elif escolha_alterar == 3:
                            os.system('clear')
                            controller.listar_produtos()
                            id = input('Qual é o id do produto? ')
                            nova_quantidade = input('Qual é a nova quantidade do produto? ')
                            controller.alterar_quantidade_produto(id, nova_quantidade)
                            print(f"Produto alterado com sucesso!")
                        
                        elif escolha_alterar == 4:
                            os.system('clear')
                            controller.listar_produtos()
                            id = input('Qual é o id do produto? ')
                            os.system('clear')
                            controller.listar_categorias()
                            id_categoria = input('Qual é o id da nova categoria? ')
                            controller.alterar_categoria_produto(id, id_categoria)
                            print(f"Produto alterado com sucesso!")
                            
                        elif escolha_alterar == 5:
                            os.system('clear')
                            controller.listar_produtos()
                            id = input('Qual é o id do produto? ')
                            os.system('clear')
                            controller.listar_fornecedores()
                            id_fornecedor = input('Qual é o id do novo fornecedor? ')
                            controller.alterar_fornecedor_produto(id, id_fornecedor)
                            print(f"Produto alterado com sucesso!")
                        
                        elif escolha_alterar == 6:
                            break
                        
                        else:
                            print('Escolha uma opção válida.\n')
                            continue
                        
                elif escolha == 4:
                    os.system('clear')
                    print("- - - PRODUTOS - - - \n")
                    controller.listar_produtos()

                elif escolha == 5:
                    break
                else:
                    print('Escolha uma opção válida.\n')
                    continue
        
        #Cliente    
        elif local == 4:
            os.system('clear')
            print('= = = = = CLIENTES = = = = = \n')
            while True:
                escolha = int(input(
                            f'Escolha uma das opções para Cliente:\n'
                            f'[1] Cadastrar\n'
                            f'[2] Remover\n'
                            f'[3] Alterar\n'
                            f'[4] Visualizar\n'
                            f'[5] Voltar ao menu principal\n'
                            f'Qual é a sua escolha? '))
                
                if escolha == 1:
                    os.system('clear')
                    nome = input('Digite o nome do cliente: ')
                    telefone = input('Digite o telefone (11 dígitos): ')
                    endereco = (input('Digite o endereço do cliente: '))
                    controller.adicionar_cliente(nome, telefone, endereco)
                    print(f"Cliente adicionado com sucesso!")
                    
                elif escolha == 2:
                    os.system('clear')
                    controller.listar_clientes()
                    print()
                    id_cliente = input('Digite o ID do cliente que deseja remover: ')
                    controller.remover_cliente(id_cliente)
                    
                elif escolha == 3:
                    os.system('clear')
                    controller.listar_clientes()
                    id__cliente= input('Qual é o ID do cliente que deseja alterar? ')
                    novo_telefone = input('Digite o novo telefone (11 dígitos): ')
                    novo_endereco = (input('Digite o endereço do cliente: '))
                    controller.alterar_cliente(id__cliente, novo_telefone, novo_endereco)
                    
                elif escolha == 4:
                    os.system('clear')
                    controller.listar_clientes()
                elif escolha == 5:
                    break
                else:
                    print('Escolha uma opção válida.\n')
                    continue

        #Transações
        elif local == 5:
            os.system('clear')
            print('= = = = = TRANSAÇÕES = = = = =\n ')
            while True:
                escolha = int(input(
                            f'Escolha uma das opções para transação:\n'
                            f'[1] Cadastrar\n'
                            f'[2] Listar transações\n'
                            f'[3] Voltar ao menu principal\n'
                            f'Qual é a sua escolha? '))
                
                if escolha == 1:
                    os.system('clear')
                    controller.listar_produtos_em_estoque()
                    id_produto = input('Qual o ID do produto vendido? ')
                    controller.listar_clientes()
                    comprador = (input('Quem foi o cliente comprador? '))
                    quantidade_vendida = int((input('Quantas unidades deste produto foram vendidas? ')))
                    controller.realizar_transacao(comprador, id_produto, quantidade_vendida)
                elif escolha == 2:
                    os.system('clear')
                    controller.listar_transacoes()

                elif escolha == 3:
                    break
                else:
                    print('Escolha uma opção válida.\n')
                    continue
                
        elif local == 6:
            os.system('clear')
            print('= = = = = RELATÓRIOS = = = = =\n ')
            while True:
                escolha = int(input(
                            f'Escolha uma das opções para relatórios:\n'
                            f'[1] Produtos em estoque\n'
                            f'[2] Consultar vendas por cliente\n'
                            f'[3] Total de vendas por categoria\n'
                            f'[4] Produtos mais vendidos\n'
                            f'[5] Voltar ao menu principal\n'
                            f'Qual é a sua escolha? '))
                
                if escolha == 1:
                    os.system('clear')
                    print("Produtos em estoque")

                    controller.listar_produtos_em_estoque()
                    
                elif escolha == 2:
                    os.system('clear')
                    controller.listar_clientes()
                    id_cliente = input('Digite o ID do cliente: ')
                    controller.listar_vendas_cliente(id_cliente)
                    
                elif escolha == 3:
                    os.system('clear')
                    controller.listar_total_vendas_categoria()
                    
                elif escolha == 4:
                    os.system('clear')
                    controller.listar_produtos_mais_vendidos()
                    
                elif escolha == 5:
                    break
                else:
                    print('Escolha uma opção válida.\n')
                    continue
        
        elif local == 7:
            print('Obrigada por escolher os produtos da MM Software. Até logo!')
            break
        
        else:
            print('Você precisa escolher uma opção válida!\n\n')
            continue
            



