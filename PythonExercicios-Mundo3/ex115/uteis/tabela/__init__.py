from ex115.uteis.texto import titulo

pessoas = list()
anos = list()

def adicionar(nome, idade):
    pessoas.append(nome)
    anos.append(idade)
    print(f'\033[1;37mNovo registro de \033[33m{nome}\033[37m adicionado.\033[m')


def mostrar_tabela():
    titulo('PESSOAS CADASTRADAS')
    if len(pessoas) != 0:
        for num, v in enumerate(pessoas):
            print(f'\033[1;35m{v:<32}{anos[num]} anos\033[m')
    else:
        print('\033[1;37mNenhuma pessoa cadastrada no momento.\033[m')