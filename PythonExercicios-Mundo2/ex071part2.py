ce50 = ce20 = ce10 = ce01 = 0
valor = int(input('\033[1;34mQual valor será sacado? \033[32mR$\033[m'))
while True:
    if valor >= 50:
        ce50 = valor // 50
        valor %= 50
    elif valor >= 20:
        ce20 = valor // 20
        valor %= 20
    elif valor >= 10:
        ce10 = valor // 10
        valor %= 10
    elif valor >= 1:
        ce01 = valor // 1
        valor %= 1
    else:
        break
print(f'\033[1;33m[{ce50}]\033[34m cédulas de \033[32mR$50.00\033[m\n'
      f'\033[1;33m[{ce20}]\033[34m cédulas de \033[32mR$20.00\033[m\n'
      f'\033[1;33m[{ce10}]\033[34m cédulas de \033[32mR$10.00\033[m\n'
      f'\033[1;33m[{ce01}]\033[34m cédulas de \033[32mR$01.00\033[m')