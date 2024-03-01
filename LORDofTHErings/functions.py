########  FICHEIRO DE FUNÇOES AUXILIARES #######
import os


def listar_arquivos_txt():
    '''
    Função para listar os arquivos .txt disponíveis na pasta atual e exibi-los na tela.
    '''
    arquivos_disponiveis = os.listdir()
    write_title("Ficheiros Disponíveis")
    for arquivo in arquivos_disponiveis:
        if arquivo.endswith('.txt'):
            print(arquivo)

def clear():
    '''
    Função para limpar ecrâ.
    '''
    os.system('cls')

def write_title(title):
    '''
    Função para escrever um título formatado.
    Recebe como argumento:
    
    - title: Título a ser exibido.
    '''
    design = ""
    comp = int((30 - len(title))/2)
    for i in range(comp):
        design += "-"

    print(f"{design}{title}{design}")
    print("-"*30)


def write_menu(title, cont, options):
    '''
    Função para exibir um menu.
    Recebe como argumentos:
    - title: Título do menu.
    - cont: Mensagem final para informar o usuário da ação pretendida pelo programa.
    - options: Opções que compõem o menu.
    '''
    design = ""
    comp = int((30 - len(title))/2)
    for i in range(comp):
        design += "-"

    print(f"{design}{title}{design}")
    print("-"*30)

    for i in range(len(options)-1):
        print(f"[{i+1}] -> {options[i]}")

    print(f"[0] -> {options[len(options)-1]}")
    try:
        return int(input(cont))
    except KeyboardInterrupt:
        print("Erro! Inválido!")


def is_valid_name(nome):
    '''
    Função para validar nomes.
    Recebe um argumento: 
    - nome: String contendo o nome a ser validado.
    
    Retorna:    
    - bool: True se o nome for válido, False caso contrário.
    '''
    lista = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
             ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    if not nome:
        print("O nome não pode estar vazio.")
        return False

    if not nome[0].isalpha():
        print("O primeiro caractere deve ser uma letra!")
        return False

    for i in range(1, len(nome)):
        if nome[i].isspace() and nome[i-1].isspace():
            print("Digite apenas um espaço entre as palavras!")
            return False
    for i in nome:
        if i in lista:
            print("O nome não pode conter caracteres especiais!")
            return False
    return True

