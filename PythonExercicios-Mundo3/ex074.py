from random import randint
numeros = (randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10),
           randint(0, 10))
print('\033[1;34mLista de números: \033[m', end='')
for c in numeros:
    print(f'\033[1;33m{c} \033[m', end='')
print('')
print(f'\033[1;34mMenor valor: \033[33m{min(numeros)}\033[m')
print(f'\033[1;34mMaior valor: \033[33m{max(numeros)}\033[m')