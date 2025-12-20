a = int(input('\033[1;34mDigite um ano: \033[m'))
if a % 4 == 0 or a % 100 and a % 400 == 0:
    print('\033[32mO ano é \033[1mBISSEXTO\033[0;32m!\033[m')
else:
    print('\033[31mO ano \033[1mNÃO\033[0;31m é \033[1mBISSEXTO\033[0;31m!\033[m')