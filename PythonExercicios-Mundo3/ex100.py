from random import randint

def sorteia(lst):
    for n in range(0, 5):
        lst.append(randint(1, 10))
    print(f'\033[1;34mLista dos 5 valores sorteados: \033[35m{lst}\033[m')

def somapar(lst):
    spar = 0
    for v in lst:
        if v % 2 == 0:
            spar += v
    print(f'\033[1;34mSoma dos valores \033[33mPARES\033[34m da lista: \033[35m{spar}\033[m')


lista = []
sorteia(lista)
somapar(lista)
