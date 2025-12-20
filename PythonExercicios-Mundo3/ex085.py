dados = []
numeros = [[], []]
for n in range(0, 7):
    dados.append(int(input('\033[1;34mDigite um número: \033[m')))
    if dados[0] % 2 == 0:
        numeros[0].append(dados[0])
    else:
        numeros[1].append(dados[0])
    dados.clear()
numeros[0].sort()
numeros[1].sort()
print(f'\n\033[1;34mLista dos valores \033[35mPARES\033[34m:\033[33m {numeros[0]}\033[m')
print(f'\033[1;34mLista dos valores \033[35mÍMPARES\033[34m:\033[33m {numeros[1]}\033[m')
