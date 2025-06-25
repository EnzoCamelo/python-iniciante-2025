catalogo_produtos = {
    10: {'nome': 'PC Gamer', 'preco': 7200.00, 'estoque': 2000, 'categoria': 'eletrônico'},
    11: {'nome': 'teclado rgb', 'preco': 900.00, 'estoque': 3000, 'categoria': 'periférico'},
    12: {"nome": "Mouse Sem Fio", "preco": 120.00, "estoque": 507, "categoria": "Periféricos"},
    13: {"nome": "Monitor Ultrawide", "preco": 1800.00, "estoque": 57, "categoria": "Eletrônicos"},
    14: {"nome": "Webcam HD", "preco": 250.00, "estoque": 0, "categoria": "Acessórios"}, # Produto sem estoque
    
}

def listar_produtos(catalogo):
    print('\n--- CATÁLOGO DE PRODUTOS ---')
    if not catalogo:
        print('Nenhum produto cadastrado no catálogo')
        return
    for id, desc in catalogo.items():
        nome = desc["nome"]
        preco = desc["preco"]
        estoque = desc["estoque"]
        categoria = desc["categoria"]

        status_estoque = ''
        if estoque == 0:
            status_estoque = ' [FORA DE ESTOQUE]'

        print(f'ID: {id}')
        print(f'Nome: {nome}{status_estoque}')
        print(f'Preço: R${preco:.2f}')
        print(f'Estoque: {estoque}')
        print(f'Categoria: {categoria}')
        print('-' * 20)

def buscar_prod(catalogo, id):
    if id in catalogo:
        return catalogo[id]
    else:
        return None
    
def vendas(catalogo, id, quantidade):
    print(f'\n--- Tentando vender {quantidade} unidade(s) do produto ID: {id} ---')
    detalhes = buscar_prod(catalogo, id)
    if detalhes is None:
        print(f'Erro: Produto com ID {id} não encintrado.')
        return False
    nome_prod = detalhes['nome']
    estoque_atual = detalhes['estoque']
    if quantidade <= 0:
        print(f'A quantitade deve ser positiva. Quantidade: {quantidade}')
        return False
    if estoque_atual >= quantidade:
        catalogo[id]['estoque'] -= quantidade
        novo_estoque = catalogo[id]['estoque']
        print(f'Venda de {quantidade} unidade(s) de {nome_prod} realizada!')
        print(f'Estoque de {nome_prod}: {novo_estoque}')
        return True
    else:
        print(f'Erro: Estoque insuficiente para "{nome_prod}". Disponível {estoque_atual}')
        return False
    
print('--- GERENCIAMENTO DE PRODUTOS ---')

def menu():
    print("\n--- MENU ---")
    print("1. Listar todos os produtos")
    print("2. Vender produto")
    print("3. Buscar produto por ID")
    print("4. Sair")
    print("------------")

print('--- BEM-VINDO AO NOSSO SISTEMA DE GERENCIAMENTO ---')

while True:
    menu()
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite apenas números! ')
        continue
    if opcao == 1:
        listar_produtos(catalogo_produtos)
    elif opcao == 2:
        try:
            id_venda = int(input('Digite o ID do produto desejado: '))
            quantidade_venda = int(input('Digite a quantidade que deseja vender: '))
            vendas(catalogo_produtos, id_venda, quantidade_venda)
        except ValueError:
            print('Digite apenas números INTEIROS!')
    elif opcao == 3:
        try:
            id_busca = int(input('Digite o ID do produto desejado: ')) 
            detal_encontrados = buscar_prod(catalogo_produtos, id_busca)
            if detal_encontrados:
                print('\n--- DETALHES DO PRODUTO ---')
                print(f'\n ID: {id_busca}')
                print(f'\nNome: {detal_encontrados['nome']}')
                print(f'\nPreço: {detal_encontrados['preco']}')
                print(f'\nEstoque: {detal_encontrados['estoque']}')
                print(f'\nCategoria: {detal_encontrados['categoria']}')
                print('-' * 20)
            else:
                print(f'ID "{id_busca}" não encontrado')
        except ValueError:
             print('Digite apenas números INTEIROS!')
    elif opcao == 4:
        print('Saindo do sistama. Até mais!')
        break
    else:
        print('Número inválido.')
print('--- PROGRAMA ENCERRADO ---')
 
    





    


        
             
