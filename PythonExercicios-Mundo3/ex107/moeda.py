def aumentar(m, p=0):
    m = m + ((m / 100) * p)
    return m


def diminuir(m, p=0):
    m = m - ((m / 100) * p)
    return m


def dobro(m):
    m *= 2
    return m


def metade(m):
    m /= 2
    return m
