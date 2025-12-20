v = int(input('\033[1;34mValor a ser sacado: \033[32mR$\033[m'))
cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    if v >= 50:
        cedula50 += 1
        v -= 50
    elif v >= 20:
        cedula20 += 1
        v -= 20
    elif v >= 10:
        cedula10 += 1
        v -= 10
    else:
        cedula1 += 1
        v -= 1
    if v == 0:
        break
print(f'\033[1;33m[{cedula50}]\033[34m Cédula(s) de \033[32mR$50,00\033[m\n'
      f'\033[1;33m[{cedula20}]\033[34m Cédula(s) de \033[32mR$20,00\033[m\n'
      f'\033[1;33m[{cedula10}]\033[34m Cédula(s) de \033[32mR$10,00\033[m\n'
      f'\033[1;33m[{cedula1}]\033[34m Cédula(s) de \033[32mR$1,00\033[m')