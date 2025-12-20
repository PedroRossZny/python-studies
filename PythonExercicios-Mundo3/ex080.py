numeros = []
for c in range(0, 5):
    numeros.append(int(input('\033[1;34mDigite um número: \033[m')))
maior = max(numeros)
menor = min(numeros)
del numeros[numeros.index(max(numeros))]
del numeros[numeros.index(min(numeros))]
maior2 = max(numeros)
menor2 = min(numeros)
del numeros[numeros.index(max(numeros))]
del numeros[numeros.index(min(numeros))]
ordenado = [menor, menor2, numeros[0], maior2, maior]
print(f'\n\033[1;34mLista ordenada: \033[31m{ordenado}\033[m')