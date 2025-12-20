c = 0
from time import sleep
from random import randint
while True:
    print('\033[1;35;40mPAR OU ÍMPAR\033[m')
    print('\033[1;34mDigite: \033[33m[P]\033[34m - \033[35m(para PAR)\033[m\n'
          '\033[1;34mDigite: \033[33m[I]\033[34m - \033[35m(para ÍMPAR)\033[m')
    escolha = str(input('\033[1;34mEscolha: \033[m')).strip().upper()
    player = int(input('\033[1;34mDigite um número inteiro de 0 a 10: \033[m'))
    comp = randint(0, 10)
    if escolha[0] == 'P':
        if (player + comp) % 2 == 0:
            print('\033[1;35mPAR\033[m')
            sleep(1)
            print('\033[1;35mOU\033[m')
            sleep(1)
            print('\033[1;35mÍMPAR\033[m')
            sleep(1)
            print(f'\033[1;32mPARABÉNS, VOCÊ GANHOU!!!\033[m\n'
                  f'\033[1;40mO computador escolheu \033[33m{comp}\033[m\033[1;40m.\033[m\n'
                  f'\033[1;40mO jogo acabará depois de uma derrota.\033[m')
            c += 1
        else:
            print('\033[1;35mPAR\033[m')
            sleep(1)
            print('\033[1;35mOU\033[m')
            sleep(1)
            print('\033[1;35mÍMPAR\033[m')
            sleep(1)
            print(f'\033[1;31mVOCÊ PERDEU :(\033[m\n'
                  f'\033[1;40mO computador escolheu \033[33m{comp}\033[m\033[1;40m.\033[m')
            break
    elif escolha[0] == 'I':
        if (player + comp) % 2 != 0:
            print('\033[1;35mPAR\033[m')
            sleep(1)
            print('\033[1;35mOU\033[m')
            sleep(1)
            print('\033[1;35mÍMPAR\033[m')
            sleep(1)
            print(f'\033[1;32mPARABÉNS, VOCÊ GANHOU!!!\033[m\n'
                  f'\033[1;40mO computador escolheu \033[33m{comp}\033[m\033[1;40m.\033[m\n'
                  f'\033[1;40mO jogo acabará depois de uma derrota.\033[m')
            c += 1
        else:
            print('\033[1;35mPAR\033[m')
            sleep(1)
            print('\033[1;35mOU\033[m')
            sleep(1)
            print('\033[1;35mÍMPAR\033[m')
            sleep(1)
            print(f'\033[1;31mVOCÊ PERDEU :(\033[m\n'
                  f'\033[1;40mO computador escolheu \033[33m{comp}\033[m\033[1;40m.\033[m')
            break
    else:
        print('\033[1;31;40mOpção inválida, escolha novamente.\033[m')
    print('\033[1;35;40m-\033[m'*12)
print(f'\n\033[1;34mVocê conquistou \033[33m{c}\033[34m vitórias consecutivas.\033[m')