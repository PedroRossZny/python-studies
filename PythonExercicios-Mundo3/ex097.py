def escreva(txt):
    print('\033[1;35;40m~\033[m' * (len(txt) + 4))
    print(f'\033[1;34;40m{txt:^{(len(txt) + 4)}}\033[m')
    print('\033[1;35;40m~\033[m' * (len(txt) + 4))


texto = str(input('\033[1;34mEscreva um texto qualquer: \033[m'))
escreva(texto)