tupla = (int(input('\033[1;34mDigite o primeiro número: \033[m')),
         int(input('\033[1;34mDigite o segundo número: \033[m')),
         int(input('\033[1;34mDigite o terceiro número: \033[m')),
         int(input('\033[1;34mDigite o quarto número: \033[m')))

print('')
print(f'\033[1;34mO valor 9 apareceu \033[33m{tupla.count(9)}\033[34m vez(es)\033[m')

if 3 in tupla:
    print(f'\033[1;34mO primeiro valor 3 aparece na posição \033[33m{tupla.index(3)}\033[m')
else:
    print('\033[1mNão foi digitado o valor 3.\033[m')

i = 0
for con, v in enumerate(tupla):
    if con == 0:
        print('\033[1;34mO(s) número(s) par(es) são/é: \033[m', end='')
    if v % 2 == 0:
        print(f'\033[33m{v} \033[m', end='')
    else:
        i += 1
    if con == 3:
        print('')
    if i == 4:
        print('\033[1mNenhum número par foi digitado.\033[m')