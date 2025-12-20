from ex115part2.uteis.texto import *
from ex115part2.uteis.arquivo import *

arquivo = 'dados'

if not arquivoexiste(arquivo):
    criararquivo(arquivo)

while True:
    titulo('MENU PRINCIPAL')
    print('\033[1;33m1- \033[34mVer pessoas cadastradas\033[m\n'
          '\033[1;33m2- \033[34mCadastrar nova Pessoa\033[m\n'
          '\033[1;33m3- \033[34mSair do Sistema\033[m')
    print('\033[1;35m-\033[m'*40)
    options = (1, 2, 3)
    while True:
        try:
            while True:
                escolha = int(input('\033[1;32mSua escolha: \033[m'))
                if escolha not in options:
                    print('\033[1;31mERRO: por favor, escolha uma opção do menu válida.\033[m')
                else:
                    break
        except ValueError:
            print('\033[1;31mERRO: por favor, escolha uma opção do menu válida.\033[m')
        else:
            break

    if escolha == 1:
        titulo('PESSOAS CADASTRADAS')
        lerarquivo(arquivo)
    elif escolha == 2:
        while True:
            try:
                while True:
                    n = str(input('\033[1;34mNome: \033[m')).strip()
                    if n == '':
                        print('\033[1;31mERRO: por favor, digite um nome válido.\033[m')
                    else:
                        break
            except ValueError:
                print('\033[1;31mERRO: por favor, digite um nome válido.\033[m')
            else:
                break
        while True:
            try:
                i = int(input('\033[1;34mIdade: \033[m'))
            except ValueError:
                print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            else:
                break
        cadastrar(arquivo, n, i)
    else:
        titulo('ATÉ LOGO!!!')
        break