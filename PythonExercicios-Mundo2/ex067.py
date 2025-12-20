while True:
    n = int(input('\033[1;34mDigite um número para ver sua tabuada,'
                  ' \033[33m(número negativo interrompe o programa)\033[34m: \033[m'))
    if n >= 0:
        c = 1
        print('')
        print('\033[1;32;40m----TABUADA----\033[m')
        while c != 11:
            print(f'\033[1;33;40m{n:3}\033[34m x \033[33m{c:2}\033[34m = \033[33m{n*c:4}\033[m')
            c += 1
        print('\033[1;32;40m-\033[m'*15)
        print('')
    else:
        break
print('\033[1;32mVOLTE SEMPRE!\033[m')