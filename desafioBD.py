import sqlite3
conexao = sqlite3.connect('teste.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS teste (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
               )
               ''')
conexao.commit()

def cadastro():
    nome = input('Seu nome: ')
    idade = int(input('Sua idade: '))
    email = input('Seu email: ')
    senha = input('Sua senha: ')
    cursor.execute('INSERT INTO teste (nome, idade, email, senha) VALUES (?, ?, ?, ?)', 
    (nome, idade, email, senha))
    conexao.commit()
    print('Usuário cadastrado com sucesso!')

def login():
    nome = input('Seu user: ').strip()
    senha = input('Sua senha: ').strip()
    cursor.execute('SELECT * FROM teste WHERE nome = ? AND senha = ?', (nome, senha))
    usuarios = cursor.fetchone()
    if usuarios:
        print(f'Bem-Vindo {usuarios[1]}')
        print('Perfil: ')
        print(f'Nome: {usuarios[1]}')
        print(f'Idade: {usuarios[2]}')
        print(f'Email: {usuarios[3]}')
        return True
    else:
        print('Usuario ou senha incorretos. ')
        return False

def listar():
    cursor.execute('SELECT * FROM teste')
    usuarios = cursor.fetchall()
    if not usuarios:
        print('nenhum usuário cadastrado.')
    else:
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Idade: {usuario[2]} | Email: {usuario[3]}")
while True:
    print("\n1 - Cadastrar novo usuário")
    print("2 - Fazer login")
    print("3 - listar")
    print('4- sair')

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastro()
    elif opcao == "2":
        if login():
            print("🎉 Acesso ao sistema liberado!")
    elif opcao == "3":
        listar()
    elif opcao == '4':
        print('Até mais!')
        break
    else:
        print("⚠️ Opção inválida.")