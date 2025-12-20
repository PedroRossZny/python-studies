numero = int(input('\033[1;34mDigite um número inteiro qualquer: \033[m'))
print('\n\033[1;32;40mBASE DE CONVERÇÃO\033[m')
base = int(input('\033[0;34;40mbinário: \033[4;33mdigite 1\033[m\n\033[0;34;40moctal: \033[4;33mdigite 2\033[m\n\033[0;34;40mhexadecimal: \033[4;33mdigite 3\033[m\n'))
if base == 1:
    print(f'\033[40mO número {numero} em \033[1mBINÁRIO\033[0;40m é \033[1;35m{bin(numero)[2:]}\033[m')
elif base == 2:
    print(f'\033[40mO número {numero} em \033[1mOCTAL\033[0;40m é \033[1;35m{oct(numero)[2:]}\033[m')
elif base == 3:
    print(f'\033[40mO número {numero} em \033[1mHEXADECIMAL\033[0;40m é \033[1;35m{hex(numero)[2:]}\033[m')
else:
    print('\n\033[31mNenhum dos números da lista foram apresentados.\033[m')