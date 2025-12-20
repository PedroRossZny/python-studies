from ex109 import moeda

p = float(input('\033[1;34mDigite um preço: \033[1;32mR$\033[m'))
print(f'\033[1;34mAumentando \033[33m10%\033[34m, temos \033[32m{moeda.aumentar(p, 10, True)}\033[m')
print(f'\033[1;34mDiminuindo \033[33m13%\033[34m, temos \033[32m{moeda.diminuir(p, 13, True)}\033[m')
print(f'\033[1;34mO dobro de \033[32m{moeda.moeda(p)}\033[34m é \033[32m{moeda.dobro(p, True)}\033[m')
print(f'\033[1;34mA metade de \033[32m{moeda.moeda(p)}\033[34m é \033[32m{moeda.metade(p, True)}\033[m')