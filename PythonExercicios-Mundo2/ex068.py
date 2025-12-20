from time import sleep
from random import randint
v = 0
while True:
    e = str(input('\033[1;33m[ P ]: \033[34mPAR\033[m\n'
                  '\033[1;33m[ I ]: \033[34mÍMPAR\033[m\n'
                  '\033[1;34mEscolha uma das opções para jogar par ou ímpar, contra o computador: \033[m')).strip().upper()
    if e in 'PI':
        n = int(input('\033[1;34mEscolha um número: \033[m'))
        c = randint(0, 10)
        print('')
        print('\033[1;35mPAR', end='')
        sleep(1)
        print(' OU ', end='')
        sleep(1)
        print('ÍMPAR!\033[m')
        sleep(1)
        print('')
        if e == 'P':
            if (n + c) % 2 == 0:
                print(f'\033[1;34mComputador jogou \033[33m{c}\033[34m, a soma entre os valores vale \033[33m{n+c}\033[m')
                print('\033[1;32mVITÓRIA!\033[m\n')
                v += 1
            else:
                print(f'\033[1;34mComputador jogou \033[33m{c}\033[34m, a soma entre os valores vale \033[33m{n+c}\033[m')
                print('\033[1;31mVOCÊ PERDEU :(\033[m\n')
                break
        elif e == 'I':
            if (n + c) % 2 != 0:
                print(f'\033[1;34mComputador jogou \033[33m{c}\033[34m, a soma entre os valores vale \033[33m{n+c}\033[m')
                print('\033[1;32mVITÓRIA!\033[m\n')
                v += 1
            else:
                print(f'\033[1;34mComputador jogou \033[33m{c}\033[34m, a soma entre os valores vale \033[33m{n+c}\033[m')
                print('\033[1;31mVOCÊ PERDEU :(\033[m\n')
                break
    else:
        print('\033[1;31mOpção inválida! Tente novamente.\033[m')
print(f'\033[1;33mFIM DE JOGO\033[m\n\033[1;34mVocê ganhou \033[33m{v}\033[34m vez(es)!\033[m')