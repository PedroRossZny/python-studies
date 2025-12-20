v = int(input('\033[1;34mVelocidade do carro em Km/h: \033[m'))
if v > 80:
    print('\033[1;31mMULTADO!\033[0;31m Diminua sua velocidade.\033[m')
    m = (v - 80) * 7
    print(f'\033[1;40mA multa foi no valor de \033[32mR${m:.2f}\033[m')
else:
    print(f'\033[1;32mTUDO CERTO!\033[1;32m Continue dirigindo com cuidado!\033[m')