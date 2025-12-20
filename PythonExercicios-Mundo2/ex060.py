n = int(input('\033[1;34mDigite um número: \033[m'))
f = n
pn = n - 1
while pn != 0:
    f *= pn
    pn -= 1
print(f'\033[1;40m{n}!= ', end='')
while n != 1:
    if n != 1:
        print(f'{n} x ', end='')
    n -= 1
    if n == 1:
        print(f'{n} ', end='')
print(f'= {f}\033[m')
