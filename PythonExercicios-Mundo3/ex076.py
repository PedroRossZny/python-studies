produtos =  ('Caderno', 20.00, 'Estojo', 5.99, 'Caneta', 2.50, 'Bolsa', 34.99,
             'Borracha', 2.00, 'Mesa', 699.99, 'Cadeira', 800.00, 'Cama', 1550.00,
             'Computador', 3500.00, 'TV', 2999.99)
print('\033[1;35;40m-\033[m'*27)
print(f'\033[1;35;40m{" TABELA DOS PRODUTOS ":=^27}\033[m')
print('\033[1;33;40m-\033[m'*27)
print('\033[1;33;40m|PRODUTO      |PREÇO      |\033[m')
print('\033[1;33;40m-\033[m'*27)
for pos, produto in enumerate(produtos):
    if pos % 2 == 0:
        print(f'\033[1;33;40m|\033[34m{produto:<13}\033[m', end='')
    else:
        print(f'\033[1;33;40m|\033[32mR${produto:<9.2f}\033[33m|\033[m')
print('\033[1;33;40m-\033[m'*27)