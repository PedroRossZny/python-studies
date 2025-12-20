menu = 0
c = 0
while menu != 5:
    if c == 0:
        v1 = float(input('\033[1;34mPrimeiro valor: \033[m'))
        v2 = float(input('\033[1;34mSegundo valor: \033[m'))
        print('')
        print('\033[1;33m[1]:\033[34m Somar\n'
              '\033[33m[2]:\033[34m Multiplicar\n'
              '\033[33m[3]:\033[34m Maior\n'
              '\033[33m[4]:\033[34m Novos números\n'
              '\033[33m[5]:\033[34m Sair do programa\033[m')
    c = 1
    menu = int(input('\033[1;35mEscolha uma das opções: \033[m'))
    print('')
    if menu == 1:
        print(f'\033[1;34;40mA soma entre \033[33m{v1}\033[34m e \033[33m{v2}\033[34m é igual a \033[33m{v1+v2}\033[m')
    elif menu == 2:
        print(f'\033[1;34;40mAo multiplicar \033[33m{v1}\033[34m com \033[33m{v2}\033[34m temos: \033[33m{v1*v2}\033[m')
    elif menu == 3:
        if v1 > v2:
            print(f'\033[1;34;40mO MAIOR número é \033[33m{v1}\033[m')
        else:
            print(f'\033[1;34;40mO MAIOR número é \033[33m{v2}\033[m')
    elif menu == 4:
        v1 = float(input('\033[1;34mPrimeiro valor: \033[m'))
        v2 = float(input('\033[1;34mSegundo valor: \033[m'))
    elif menu == 5:
        print('\033[1;32mVOLTE SEMPRE!\033[m')
    else:
        print('\033[1;31mOpção inválida! Escolha uma das opções do menu.\033[m')