import os
def titulo_do_projeto():
    print ('\nGerenciamento de Estoque \n')

estoque_lista = [{'produto': 'smartphones', 'quantidade': 6, 'valor_unitario': 120, 'total': 0},
                 {'produto': 'tablet', 'quantidade': 5, 'valor_unitario': 207, 'total': 0}]

def menu_principal():
    print('1. Adicionar Produto ao Estoque ')
    print('2. Remover Produto do Estoque ')
    print('3. Visualizar Estoque ')
    print('4. Calcular valor total do Estoque ')
    print('5. Sair\n ')

def voltar_ao_menu_incial():
    #os.system('cls')
    input('\nDigite uma tecla para voltar ao menu inicial')
    main()

def adicionar_produtos():
    '''
    Função para adicionar produtos ao estoque.
    '''
    nome = input('Digite o nome do produto que deseja cadastrar: ')
    nome_do_produto = nome.casefold()
   
    quantidade_do_produto = int(input(f'Digite a quantidade do produto {nome_do_produto}: '))
    valor_do_produto = float(input(f'Digite o valor do produto {nome_do_produto}: '))

    dados_do_produto = {'produto':nome_do_produto, 'quantidade': quantidade_do_produto, 'valor_unitario': valor_do_produto, 'total':0 }
    estoque_lista.append(dados_do_produto)

    print(f'\nO produto {nome_do_produto} foi cadastrado com sucesso')

    voltar_ao_menu_incial()


def remover_produto():
    '''
    Função para remover produtos do estoque. 
    '''
    nome = input('Digite o nome do produto que deseja remover: ')
    nome_do_produto = nome.casefold() 

    for produto in estoque_lista:
         if produto['produto'] == nome_do_produto: 
          estoque_lista.remove(produto)
          print(f'O produto {nome_do_produto} foi removido do estoque. ')

    if not produto['produto'] == nome_do_produto:
        print(f'O produto {nome_do_produto} não foi encontrado no estoque. ')
        
    voltar_ao_menu_incial()

def visualizar_produto():
    '''
    Função para mostrar o estoque disponivel
    '''
    print('\nLista dos produtos disponivéis no Estoque: \n')
    print(f'Nome do Produto | Quantidade | Valor')

    for produto in estoque_lista:
        nome_do_produto = produto['produto']
        quantidade_do_produto = produto['quantidade']
        valor_do_produto = produto['valor_unitario']

        print(f'{nome_do_produto.ljust(15)} | {quantidade_do_produto}          | {valor_do_produto}')
      
    voltar_ao_menu_incial()

def calcular_valor_total():
    '''
    Calcular o valor total do estoque
    '''
    print(f'Nome do Produto | Quantidade | Valor unítario | valor total do Estoque')

    soma_estoque = 0
    soma_unitario = 0
    
    for produto in estoque_lista:
        nome_do_produto = produto['produto']
        quantidade_do_produto = produto['quantidade']
        valor_do_produto = produto['valor_unitario']
        total_do_estoque = produto['total']

        total_do_estoque = valor_do_produto * quantidade_do_produto

        print(f'{nome_do_produto.ljust(15)} | {quantidade_do_produto}          | {valor_do_produto}            | {total_do_estoque}')

        soma_estoque += total_do_estoque
        soma_unitario += produto['valor_unitario']
    print(f'O Valor total do estoque é R${soma_estoque} ')
    print(f'O valor unitario é R${soma_unitario}')
        
    voltar_ao_menu_incial()

def opcao_escolhida():
    try:

        escolha_opcao = int(input('Escolhar uma opção: '))

        if escolha_opcao == 1:
            adicionar_produtos()
        elif escolha_opcao == 2: 
            remover_produto()
        elif escolha_opcao == 3:
            visualizar_produto()
        elif escolha_opcao == 4:
            calcular_valor_total()
        elif escolha_opcao == 5:
            voltar_ao_menu_incial()
        else:
            print(f'{escolha_opcao} é uma opção Inválida')
            voltar_ao_menu_incial()    
    except:
        print('ERRO: Digite somente número. ')
        voltar_ao_menu_incial()
    
def main():
    os.system('cls')
    titulo_do_projeto()
    menu_principal()
    opcao_escolhida()


if __name__ == '__main__':
 main()

