peso = float(input('\033[1;34mPeso: \033[m'))
altura = float(input('\033[1;34mAltura: \033[m'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\033[1;33mABAIXO DO PESO!!!\033[m')
elif imc < 25:
    print('\033[1;32mPESO IDEIAL!!!\033[m')
elif imc < 30:
    print('\033[1;33mSOBREPESO!!!\033[m')
elif imc < 40:
    print('\033[1;31mOBESIDADE!!!\033[m')
else:
    print('\033[1;31;40mOBESIDADE MÓRBIDA!!!\033[m')