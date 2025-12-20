def leiaint(valor):
    while True:
        try:
            valor = int(input(valor))
        except Exception as erro:
            print(f'\033[1;31mERRO {erro.__class__}: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    return valor


def leiafloat(valor):
    while True:
        try:
            valor = float(input(valor))
        except Exception as erro:
            print(f'\033[1;31mERRO {erro.__class__}: por favor, digite um número real válido.\033[m')
        else:
            break
    return valor


i = leiaint('\033[1;34mDigite um número inteiro: \033[m')
r = leiafloat('\033[1;34mDigite um número real: \033[m')
print(f'\033[1;34mO valor inteiro digitado foi \033[33m{i}\033[34m e o real foi \033[33m{r:.2f}\033[34m.\033[m')