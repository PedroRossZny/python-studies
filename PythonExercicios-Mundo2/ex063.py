t = int(input('\033[1;34mQuantos termos você quer mostrar em uma sequência de fibonacci? \033[m'))
c = sf = an = 0
while c != t:
    if c == 0:
        print(f'\033[1;40m{sf} -> ', end='')
        sf = 1
    elif c == 1:
        print(f'{sf} -> ', end='')
    else:
        sf += an
        print(f'{sf} -> ', end='')
        an = sf - an
    c += 1
print('\033[32mFIM\033[m')