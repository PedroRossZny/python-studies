import moeda

p = float(input('\033[1;34mDigite um preço: \033[1;32mR$\033[m'))
print(f'\033[1;34mAumentando \033[33m10%\033[34m, temos \033[32mR${moeda.aumentar(p, 10):.2f}\033[m')
print(f'\033[1;34mDiminuindo \033[33m13%\033[34m, temos \033[32mR${moeda.diminuir(p, 13):.2f}\033[m')
print(f'\033[1;34mO dobro de \033[32mR${p:.2f}\033[34m é \033[32mR${moeda.dobro(p):.2f}\033[m')
print(f'\033[1;34mA metade de \033[32mR${p:.2f}\033[34m é \033[32mR${moeda.metade(p):.2f}\033[m')