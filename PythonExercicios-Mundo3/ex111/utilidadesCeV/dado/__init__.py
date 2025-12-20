from ex111.utilidadesCeV import moeda

def resumo(m=0, a=0, r=0):
    msg = 'RESUMO DO VALOR'
    print('\033[1;35m-\033[m'*(len(msg)+16))
    print('\033[1;35m \033[m'*8+f'\033[1;35m{msg}\033[m'+'\033[1;35m \033[m'*8)
    print('\033[1;35m-\033[m'*(len(msg)+16))
    print(f'\033[1;34m{"Preço analisado:":<20} \033[32m{moeda.formatar(m)}\033[m')
    print(f'\033[1;34m{"Dobro do preço:":<20} \033[32m{moeda.dobro(m, True)}\033[m')
    print(f'\033[1;34m{"Metade do preço:":<20} \033[32m{moeda.metade(m, True)}\033[m')
    print(f'\033[1;34m{f"{a}% de aumento:":<20} \033[32m{moeda.aumentar(m, a, True)}\033[m')
    print(f'\033[1;34m{f"{r}% de redução:":<20} \033[32m{moeda.diminuir(m, r, True)}\033[m')
    print('\033[1;35m-\033[m'*(len(msg)+16))
