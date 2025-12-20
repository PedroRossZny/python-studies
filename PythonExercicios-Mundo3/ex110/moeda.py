def aumentar(m=0, p=0, formatado=False):
    m = m + ((m / 100) * p)
    return m if formatado is False else moeda(m)


def diminuir(m=0, p=0, formatado=False):
    m = m - ((m / 100) * p)
    return m if formatado is False else moeda(m)


def dobro(m=0, formatado=False):
    m *= 2
    return m if formatado is False else moeda(m)


def metade(m=0, formatado=False):
    m /= 2
    return m if formatado is False else moeda(m)


def moeda(m=0.0):
    return f'{f"R${m:.2f}"}'


def resumo(m=0, a=0, r=0):
    msg = 'RESUMO DO VALOR'
    print('\033[1;35m-\033[m'*(len(msg)+16))
    print('\033[1;35m \033[m'*8+f'\033[1;35m{msg}\033[m'+'\033[1;35m \033[m'*8)
    print('\033[1;35m-\033[m'*(len(msg)+16))
    print(f'\033[1;34m{"Preço analisado:":<20} \033[32m{moeda(m)}\033[m')
    print(f'\033[1;34m{"Dobro do preço:":<20} \033[32m{dobro(m, True)}\033[m')
    print(f'\033[1;34m{"Metade do preço:":<20} \033[32m{metade(m, True)}\033[m')
    print(f'\033[1;34m{f"{a}% de aumento:":<20} \033[32m{aumentar(m, a, True)}\033[m')
    print(f'\033[1;34m{f"{r}% de redução:":<20} \033[32m{diminuir(m, r, True)}\033[m')
    print('\033[1;35m-\033[m'*(len(msg)+16))
