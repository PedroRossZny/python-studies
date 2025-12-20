numeros = []
for c in range(0, 5):
    numeros.append(int(input('\033[1;34mDigite um valor: \033[m')))
print('')
print(f'\033[1;34mMaior valor: \033[33m{max(numeros)}\033[m')
print(f'\033[1;34mMenor valor: \033[33m{min(numeros)}\033[m')
print('')
for c, n in enumerate(numeros):
    print(f'\033[1;33m{n}\033[34m esta na posição \033[35m{c}\033[m')