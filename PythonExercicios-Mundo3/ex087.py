lista = [[[], [], []],
         [[], [], []],
         [[], [], []]]
pares = col3 = maior = 0
for c, v in enumerate(lista[0]):
    lista[0][c].append(int(input(f'\033[1;34mDigite um valor para \033[33m[0, {c}]\033[34m: \033[m')))
for c, v in enumerate(lista[1]):
    lista[1][c].append(int(input(f'\033[1;34mDigite um valor para \033[33m[1, {c}]\033[34m: \033[m')))
    for n in v:
        if c == 0 or n > maior:
            maior = n
for c, v in enumerate(lista[2]):
    lista[2][c].append(int(input(f'\033[1;34mDigite um valor para \033[33m[2, {c}]\033[34m: \033[m')))
for c1, c2, c3 in lista:
    for v in c1:
        if v % 2 == 0:
            pares += v
    for v in c2:
        if v % 2 == 0:
            pares += v
    for v in c3:
        col3 += v
        if v % 2 == 0:
            pares += v
print()
for l in lista:
    print(f'\033[1;35;40m{l}\033[m')
print(f'\n\033[1;34mSoma de todos os valores pares: \033[33m{pares}\033[m')
print(f'\033[1;34mSoma dos valores da terceira coluna: \033[33m{col3}\033[m')
print(f'\033[1;34mMaior valor da segunda fileira: \033[33m{maior}\033[m')