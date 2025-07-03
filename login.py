def cadastro(lista):
    usuario = input('Digite seu usuario: ').strip()
    senha = str(input('Digite sua senha: ')).strip()
    login = {'usuario' : usuario, 'senha' : senha}
    lista.append(login)
    print('Usuário cadastrado com sucesso!')

def valid(lista):
    tentativas = 3
    while tentativas > 0:
        usuario = input('Digite seu usuario: ').strip()
        senha = str(input('Digite sua senha: ')).strip()
        usuario_enc = any(
            cadastro['usuario'] == usuario and cadastro['senha'] == senha
            for cadastro in lista
        )
        if usuario_enc:
            print('login bem sucedido')
            return
        else:
            tentativas -= 1
            print(f'Usuario ou senha errados. Tentativas {tentativas}')
    print('Tentativas esgotadas.')
    

teste = []

# Menu principal
while True:
    print('1 - Cadastrar novo usuário')
    print('2 - Fazer login')
    print('3 - Sair')
    try:
        opt = int(input('Digite sua opção: '))
    except ValueError:
        print('❌ Digite um número válido (1, 2 ou 3).\n')
        continue

    if opt == 1:
        cadastro(teste)
    elif opt == 2:
        valid(teste)
    elif opt == 3:
        print('👋 Até logo!')
        break
    else:
        print('⚠️ Opção inválida. Tente novamente.\n')







