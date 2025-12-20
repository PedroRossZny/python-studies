def pyhelp():
    ajuda = ''
    while ajuda != 'fim':
        print('\033[1;32;40m-\033[m'*25)
        print('\033[1;32;40m SISTEMA DE AJUDA PyHELP \033[m')
        print('\033[1;32;40m-\033[m'*25)
        ajuda = str(input('\033[1;34mFunção ou Biblioteca \033[33m[fim(para sair)]\033[1;34m > \033[m')).strip().lower()
        if ajuda != 'fim':
            frase = f' Acessando o manual do comando {ajuda} '
            print('\033[1;35;40m-\033[m' * len(frase))
            print(f'\033[1;35;40m{frase}\033[m')
            print('\033[1;35;40m-\033[m' * len(frase))
            print('\033[1;35m')
            help(ajuda)
            print('\033[m')
        else:
            print('\033[1;31;40m-\033[m'*11)
            print('\033[1;31;40m ATÉ LOGO! \033[m')
            print('\033[1;31;40m-\033[m'*11)


pyhelp()