palavras = ('olho', 'casa', 'espelho', 'porta', 'janela', 'computador', 'pizza',
            'caderno', 'estojo', 'fone', 'celular', 'camisa', 'sorvete', 'tapete')

for palavra in palavras:
    print(f'\033[1;33m{palavra}\033[34m possui as vogais: \033[m', end='')
    if palavra.count('a') > 0:
        print('\033[1;35ma \033[m', end='')
    if palavra.count('e') > 0:
        print('\033[1;35me \033[m', end='')
    if palavra.count('i') > 0:
        print('\033[1;35mi \033[m', end='')
    if palavra.count('o') > 0:
        print('\033[1;35mo \033[m', end='')
    if palavra.count('u') > 0:
        print('\033[1;35mu \033[m', end='')
    print('')
print('')