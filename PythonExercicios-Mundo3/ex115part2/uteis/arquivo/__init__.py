def arquivoexiste(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    a = open(nome, 'wt+')
    a.close()


def lerarquivo(nome):
    a = open(nome)
    if a.read() == '':
        print('\033[1;37mNenhuma pessoa cadastrada no momento.\033[m')
    else:
        a.seek(0)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[1;37m{dado[0]:<32}{dado[1]} anos\033[m')
    a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    a = open(arq, 'at')
    a.write(f'{nome};{idade}\n')
    a.close()
    print(f'\033[1;37mNovo registro de \033[33m{nome}\033[37m adicionado.\033[m')