while True:
    n = int(input('\033[1;34mDigite um número \033[33m(Digite um número negativo para parar)\033[34m: \033[m'))
    if n >= 0:
        print('\033[1;35;40m---TABUADA---\033[m')
        for c in range (1, 11):
            print(f'\033[1;34m{n} x \033[33m{c:2}\033[34m = \033[35m{n*c}\033[m')
        print('\033[1;35;40m-\033[m'*13)
    else:
        print('\033[1;33mVOLTE SEMPRE!!!\033[m')
        break