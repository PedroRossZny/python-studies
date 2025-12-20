valor = float(input('\033[1;34mValor da casa: \033[m'))
salario = float(input('\033[1;34mSalário do comprador: \033[m'))
anos = int(input('\033[1;34mEm quantos anos pretende pagar: \033[m'))
prestacao = (valor / anos) / 12
if prestacao <= salario * (30/100):
    print('\033[32mPrestação concedida com \033[1mSUCESSO!!!\033[m')
else:
    print('\033[31mPrestação \033[1mNEGADA!!!\033[m')
print(f'\033[33;40mValor da prestação mensal: \033[1;32mR${prestacao:.2f}\033[m')