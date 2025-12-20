from time import sleep
from random import randint
pare = False
print('\033[1;35mVAMOS JOGAR JOKENPÔ\033[m\n\033[1;33m[1]:\033[34m PEDRA\033[m\n\033[1;33m[2]:\033[34m PAPEL\033[m\n\033[1;33m[3]:\033[34m TESOURA\033[m\n')
player = int(input('\033[1;34mFaça sua escolha: \033[m'))
comp = randint(1,3)
print('\033[1;35mPROCESSANDO...\033[m')
sleep(2)
print('')
if player == 1 and comp == 2:
    print('\033[1;31mVOCÊ PERDEU!!!\033[m')
elif player == 1 and comp == 3:
    print('\033[1;32mVOCÊ GANHOU!!!\033[m')
elif player == 2 and comp == 1:
    print('\033[1;32mVOCÊ GANHOU!!!\033[m')
elif player == 2 and comp == 3:
    print('\033[1;31mVOCÊ PERDEU!!!\033[m')
elif player == 3 and comp == 1:
    print('\033[1;31mVOCÊ PERDEU!!!\033[m')
elif player == 3 and comp == 2:
    print('\033[1;32mVOCÊ GANHOU!!!\033[m')
elif player == comp:
    print('\033[1;33mEMPATE!!!\033[m')
else:
    pare = True
    print('\033[1;31mOpção inválida!\033[m')
if pare == False:
    if comp == 1:
        print('\033[34mO computador escolheu \033[1mPEDRA\033[m')
    elif comp == 2:
        print('\033[34mO computador escolheu \033[1mPAPEL\033[m')
    elif comp == 3:
        print('\033[34mO computador escolheu \033[1mTESOURA\033[m')