l = float(input('\033[1;34mLargura de uma parede em metros: \033[m'))
a = float(input('\033[1;34mAltura da mesma parede em metros: \033[m'))
ar = l * a
print(f'\033[1;40mÁrea da parede: \033[33m{ar}m²\033[m\n'
      f'\033[1;40mQuantidade de tinta necessaria para pinta-la: \033[33m{ar/2}L\033[m')