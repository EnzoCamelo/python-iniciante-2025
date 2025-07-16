import os
import shutil

diretorio_down = r'C:\Users\seu user\OneDrive\diretório desejado'

pastas_destino = {
    "PDFs": [".pdf"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".doc", ".docx", ".txt", ".rtf"],
    "Executaveis": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audios": [".mp3", ".wav"],
    "Outros": [] 
}

print(f'Iniciando organização da pasta {diretorio_down}\n')

for pasta in pastas_destino.keys():
    caminho_pasta = os.path.join(diretorio_down, pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        print(f'Pasta {pasta} criada.')
print("-" * 30)
try:
    for nome_arquivo in os.listdir(diretorio_down):
        caminho_novo = os.path.join(diretorio_down, nome_arquivo)
        if os.path.isfile(caminho_novo):
            nome_base, extensao = os.path.splitext(nome_arquivo)
            extensao = extensao.lower()
            
            destino = False
            for pasta, extensoes in pastas_destino.items():
                if extensao in extensoes:
                    caminho_destino = os.path.join(diretorio_down, pasta, nome_arquivo)
                    print(f'Movendo "{nome_arquivo}" para "{pasta}"')
                    try:
                        shutil.move(caminho_novo, caminho_destino)
                        destino = True
                        break
                    except shutil.Error as e:
                        print(f'Erro ao mover {nome_arquivo}: {e}')
                        destino = True
                        break
                    except Exception as e:
                        print(f'Erro imprevisto ao mover {nome_arquivo}')
                        destino = True
            if not destino and nome_arquivo not in pastas_destino.keys():
                caminho_outros = os.path.join(diretorio_down, 'Outros', nome_arquivo)
                print(f'Movendo {nome_arquivo} para a "Outros"')
                try:
                    shutil.move(caminho_novo, caminho_outros)
                except shutil.Error as e:
                    print(f'Erro ao mover "{nome_arquivo}" para "Outros"')
                except Exception as e:
                    print(f'Erro imprevisto ao mover {nome_arquivo}')
except FileNotFoundError:
    print(f'ERRO! o diretório {diretorio_down} não foi encontrado.')
except PermissionError:
    print('ERRO! Verifque se você tem permissão para acessar o diretório.')
except Exception:
    print('Erro Inesperado.')

print('Fim da organização')