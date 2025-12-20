def fatorial(num, show=0):
    """
    → Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    f = 1
    if show:
        seq = []
        for c in range(num, 0, -1):
            seq.append(str(f'\033[1;34m{c}\033[m'))
            f *= c
        print('\033[1;34m x \033[m'.join(seq) + '\033[1;34m = \033[m', end='')
        return f'\033[1;33m{f}\033[m'
    else:
        for c in range(num, 0, -1):
            f *= c
        return f'\033[1;33m{f}\033[m'


print(fatorial(5, True))
help(fatorial)