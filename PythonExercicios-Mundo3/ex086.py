lista = [[[], [], []],
         [[], [], []],
         [[], [], []]]
for c, v in enumerate(lista[0]):
    lista[0][c].append(int(input(f'\033[1;34mDigite um valor para \033[33m[0, {c}]\033[34m: \033[m')))
for c, v in enumerate(lista[1]):
    lista[1][c].append(int(input(f'\033[1;34mDigite um valor para \033[33m[1, {c}]\033[34m: \033[m')))
for c, v in enumerate(lista[2]):
    lista[2][c].append(int(input(f'\033[1;34mDigite um valor para \033[33m[2, {c}]\033[34m: \033[m')))
for l in lista:
    print(f'\033[1;35;40m{l}\033[m')