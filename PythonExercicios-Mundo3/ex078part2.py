numeros = []
for c in range(0, 5):
    numeros.append(int(input('\033[1;34mDigite um valor: \033[m')))
maior = max(numeros)
menor = min(numeros)
print('')
print(f'\033[1;34mO maior valor digitado foi \033[33m{maior}\033[34m nas posições: \033[m', end='')
for c, v in enumerate(numeros):
    if v == maior:
        print(f'\033[1;33m{c} \033[m', end='')
print(f'\033[1;34m\nO menor valor digitado foi \033[33m{menor}\033[34m nas posições: \033[m', end='')
for c, v in enumerate(numeros):
    if v == menor:
        print(f'\033[1;33m{c} \033[m', end='')