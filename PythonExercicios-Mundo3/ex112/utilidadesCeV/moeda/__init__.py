def aumentar(m=0, p=0, formatado=False):
    m = m + ((m / 100) * p)
    return m if formatado is False else formatar(m)


def diminuir(m=0, p=0, formatado=False):
    m = m - ((m / 100) * p)
    return m if formatado is False else formatar(m)


def dobro(m=0, formatado=False):
    m *= 2
    return m if formatado is False else formatar(m)


def metade(m=0, formatado=False):
    m /= 2
    return m if formatado is False else formatar(m)


def formatar(m=0.0):
    return f'{f"R${m:.2f}"}'