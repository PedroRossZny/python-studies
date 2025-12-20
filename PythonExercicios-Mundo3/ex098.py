from time import sleep
def lin(msg):
    print('\033[1;35m-\033[m' * len(msg))
    print(f'\033[1;35m{msg:^{len(msg)}}\033[m')
    print('\033[1;35m-\033[m' * len(msg))

def contador(i, f, p):
    n = i
    if i < f:
        while True:
            sleep(0.5)
            if n > f:
                print('\033[33mFIM!\033[m')
                break
            else:
                print(f'\033[1;34m{n} ', end='')
                n += p
    else:
        while True:
            sleep(0.5)
            if n < f:
                print('\033[1;33mFIM!\033[m')
                break
            else:
                if p < 0:
                    print(f'\033[1;34m{n} ', end='')
                    n += p
                else:
                    print(f'\033[1;34m{n} ', end='')
                    n -= p


lin('CONTAGEM DE 1 ATÉ 10 DE 1 EM 1')
contador(1, 10, 1)
lin('CONTAGEM DE 10 ATÉ 0 DE 2 EM 2')
contador(10, 0, -2)
lin('AGORA É SUA VEZ DE PERSONALIZAR')
inicio = int(input('\033[1;34mDigite o início de uma contagem: \033[m'))
fim = int(input('\033[1;34mDigite o final da mesma contagem: \033[m'))
passo = int(input('\033[1;34mDigite os passos dessa contagem: \033[m'))
contador(inicio, fim, passo)
