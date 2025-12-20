colocados20 = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo',
               'Bahia', 'Fluminense', 'São Paulo', 'Bragantino', 'Ceará',
               'Vasco', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Internacional',
               'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport')

print('\033[1;35;40m----Os 5 primeiros colocados----\033[m')
for con, colocado in enumerate(colocados20[:5]):
    print(f'\033[1;33;40m       {con+1}º lugar: \033[m', end='')
    print(f'\033[1;34;40m{colocado:9}      \033[m')
print('\033[1;35;40m-\033[m'*32)

print('\n\033[1;35;40m-----Os últimos 4 colocados-----\033[m')
con = 20
for colocado in colocados20[-1:-5:-1]:
    print(f'\033[1;33;40m      {con}º lugar: \033[m', end='')
    print(f'\033[1;34;40m{colocado:9}      \033[m')
    con -= 1
print('\033[1;35;40m-\033[m'*32)

print('\n\033[1;35;40m-------Em ordem alfabética------\033[m')
for colocado in sorted(colocados20):
    print(f'\033[1;32;40m{colocado:<32}\033[m')
print(f'\033[1;35;40m-\033[m'*32)

print('\n\033[1;35;40m-----Posição do Corinthians-----\033[m')
LocalCo = colocados20.index('Corinthians')
print(f'\033[1;33;40m     {LocalCo+1}º lugar:\033[34m {colocados20[LocalCo]}     \033[m')
print('\033[1;35;40m-\033[m'*32)